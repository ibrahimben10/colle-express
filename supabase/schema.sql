-- =====================================================================
--  Colle express — schéma de la base Supabase
--  À coller en une fois dans : Supabase > SQL Editor > New query > Run
-- =====================================================================

-- 1. Profils (un par compte) ------------------------------------------
create table if not exists public.profiles (
  id          uuid primary key references auth.users(id) on delete cascade,
  full_name   text not null default '',
  role        text not null default 'eleve' check (role in ('eleve','prof')),
  niveau      int  not null default 1 check (niveau between 1 and 3),
  created_at  timestamptz not null default now(),
  last_seen   timestamptz not null default now()
);

-- 2. Suivi de progression (un document JSON par élève) -----------------
create table if not exists public.suivi (
  user_id     uuid primary key references public.profiles(id) on delete cascade,
  data        jsonb not null default '{}'::jsonb,
  updated_at  timestamptz not null default now()
);

-- 3. Exercices ajoutés par le professeur --------------------------------
create table if not exists public.banque (
  id          uuid primary key default gen_random_uuid(),
  titre       text not null,
  mat         text not null check (mat in ('Maths','Physique','Chimie')),
  chap        text not null default 'Divers',
  niveau      int  not null check (niveau between 1 and 3),
  duree       int  not null default 20,
  enonce      text not null,
  source      text not null default '',
  concours    text not null default '',
  created_by  uuid references public.profiles(id) on delete set null,
  created_at  timestamptz not null default now()
);

-- 4. Configuration de la classe (une seule ligne) -----------------------
create table if not exists public.classe_config (
  id               int primary key default 1 check (id = 1),
  message          text not null default '',
  sel              jsonb not null default '{}'::jsonb,
  updated_at       timestamptz not null default now()
);
insert into public.classe_config (id) values (1) on conflict do nothing;

-- 4 bis. Code d'inscription (secret, lisible seulement par le prof) -----
create table if not exists public.classe_secret (
  id               int primary key default 1 check (id = 1),
  code_inscription text not null default 'MP2026'
);
insert into public.classe_secret (id) values (1) on conflict do nothing;

-- 5. Journal d'usage de l'IA (limite quotidienne) -----------------------
create table if not exists public.ia_usage (
  id         bigserial primary key,
  user_id    uuid not null references public.profiles(id) on delete cascade,
  mode       text not null,
  created_at timestamptz not null default now()
);
create index if not exists ia_usage_user_day on public.ia_usage(user_id, created_at);

-- Fonction utilitaire : l'utilisateur courant est-il professeur ? -------
create or replace function public.is_prof() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'prof');
$$;

-- Création automatique du profil à l'inscription, avec code de classe ---
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
declare
  attendu text;
begin
  select code_inscription into attendu from public.classe_secret where id = 1;
  if coalesce(new.raw_user_meta_data->>'code', '') <> coalesce(attendu, '') then
    raise exception 'Code de classe invalide';
  end if;
  insert into public.profiles (id, full_name, niveau)
  values (new.id,
          left(coalesce(new.raw_user_meta_data->>'full_name', ''), 80),
          greatest(1, least(3, coalesce((new.raw_user_meta_data->>'niveau')::int, 1))));
  insert into public.suivi (user_id, data) values (new.id, '{}'::jsonb);
  return new;
end $$;
drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- Un élève ne peut pas se promouvoir professeur -------------------------
create or replace function public.protect_role() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  -- auth.uid() est nul dans l'éditeur SQL de Supabase : la promotion manuelle y reste possible.
  if new.role is distinct from old.role and auth.uid() is not null and not public.is_prof() then
    new.role := old.role;
  end if;
  return new;
end $$;
drop trigger if exists profiles_protect_role on public.profiles;
create trigger profiles_protect_role before update on public.profiles
  for each row execute function public.protect_role();

-- Sécurité au niveau des lignes (RLS) -----------------------------------
alter table public.profiles      enable row level security;
alter table public.suivi         enable row level security;
alter table public.banque        enable row level security;
alter table public.classe_config enable row level security;
alter table public.ia_usage      enable row level security;

drop policy if exists "profil: lire le sien ou prof" on public.profiles;
create policy "profil: lire le sien ou prof" on public.profiles for select
  using (id = auth.uid() or public.is_prof());
drop policy if exists "profil: modifier le sien ou prof" on public.profiles;
create policy "profil: modifier le sien ou prof" on public.profiles for update
  using (id = auth.uid() or public.is_prof());

drop policy if exists "suivi: lire le sien ou prof" on public.suivi;
create policy "suivi: lire le sien ou prof" on public.suivi for select
  using (user_id = auth.uid() or public.is_prof());
drop policy if exists "suivi: écrire le sien" on public.suivi;
create policy "suivi: écrire le sien" on public.suivi for insert
  with check (user_id = auth.uid());
drop policy if exists "suivi: modifier le sien" on public.suivi;
create policy "suivi: modifier le sien" on public.suivi for update
  using (user_id = auth.uid());

drop policy if exists "banque: lecture" on public.banque;
create policy "banque: lecture" on public.banque for select using (auth.role() = 'authenticated');
drop policy if exists "banque: ajout prof" on public.banque;
create policy "banque: ajout prof" on public.banque for insert with check (public.is_prof());
drop policy if exists "banque: suppression prof" on public.banque;
create policy "banque: suppression prof" on public.banque for delete using (public.is_prof());

drop policy if exists "config: lecture" on public.classe_config;
create policy "config: lecture" on public.classe_config for select using (auth.role() = 'authenticated');
drop policy if exists "config: prof" on public.classe_config;
create policy "config: prof" on public.classe_config for update using (public.is_prof());

drop policy if exists "ia: lire le sien" on public.ia_usage;
create policy "ia: lire le sien" on public.ia_usage for select using (user_id = auth.uid() or public.is_prof());

-- Le code d'inscription : lecture et modification par le prof seulement
alter table public.classe_secret enable row level security;
drop policy if exists "secret: prof lit" on public.classe_secret;
create policy "secret: prof lit" on public.classe_secret for select using (public.is_prof());
drop policy if exists "secret: prof modifie" on public.classe_secret;
create policy "secret: prof modifie" on public.classe_secret for update using (public.is_prof());

-- Temps réel sur le suivi (tableau de bord du prof) ---------------------
do $$ begin
  alter publication supabase_realtime add table public.suivi;
exception when duplicate_object then null; end $$;
do $$ begin
  alter publication supabase_realtime add table public.classe_config;
exception when duplicate_object then null; end $$;
do $$ begin
  alter publication supabase_realtime add table public.banque;
exception when duplicate_object then null; end $$;

-- =====================================================================
--  GROUPES D'ÉTUDIANTS, RÉPONSES SUR L'HONNEUR, NOTATION PAR LES PAIRS
-- =====================================================================

-- 6. Groupes --------------------------------------------------------------
create table if not exists public.groupes (
  id          uuid primary key default gen_random_uuid(),
  nom         text not null check (char_length(nom) between 2 and 60),
  description text not null default '' check (char_length(description) <= 300),
  code        text not null unique default upper(substr(md5(random()::text || clock_timestamp()::text), 1, 6)),
  created_by  uuid references public.profiles(id) on delete set null,
  created_at  timestamptz not null default now()
);

-- Rôles : responsable (gère le groupe et les rôles), modérateur (supprime
-- réponses et commentaires, exclut des membres simples), membre.
create table if not exists public.groupe_membres (
  groupe_id  uuid not null references public.groupes(id) on delete cascade,
  user_id    uuid not null references public.profiles(id) on delete cascade,
  role       text not null default 'membre' check (role in ('responsable','moderateur','membre')),
  joined_at  timestamptz not null default now(),
  primary key (groupe_id, user_id)
);
create index if not exists groupe_membres_user on public.groupe_membres(user_id);

-- Fonctions d'autorisation (security definer : pas de récursion RLS) --------
create or replace function public.role_groupe(g uuid) returns text
language sql stable security definer set search_path = public as $$
  select role from public.groupe_membres where groupe_id = g and user_id = auth.uid();
$$;
create or replace function public.est_membre(g uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select public.role_groupe(g) is not null or public.is_prof();
$$;
create or replace function public.peut_moderer(g uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce(public.role_groupe(g) in ('responsable','moderateur'), false) or public.is_prof();
$$;
create or replace function public.est_responsable(g uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce(public.role_groupe(g) = 'responsable', false) or public.is_prof();
$$;
create or replace function public.partage_groupe(u uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.groupe_membres a join public.groupe_membres b on a.groupe_id = b.groupe_id
                 where a.user_id = auth.uid() and b.user_id = u);
$$;

-- Actions sur les groupes (RPC) --------------------------------------------
create or replace function public.creer_groupe(p_nom text, p_description text default '') returns uuid
language plpgsql security definer set search_path = public as $$
declare g uuid;
begin
  if auth.uid() is null then raise exception 'Connexion requise'; end if;
  insert into public.groupes (nom, description, created_by)
  values (left(trim(p_nom), 60), left(coalesce(trim(p_description), ''), 300), auth.uid()) returning id into g;
  insert into public.groupe_membres (groupe_id, user_id, role) values (g, auth.uid(), 'responsable');
  return g;
end $$;

create or replace function public.rejoindre_groupe(p_code text) returns uuid
language plpgsql security definer set search_path = public as $$
declare g uuid;
begin
  if auth.uid() is null then raise exception 'Connexion requise'; end if;
  select id into g from public.groupes where code = upper(trim(p_code));
  if g is null then raise exception 'Code de groupe inconnu'; end if;
  insert into public.groupe_membres (groupe_id, user_id) values (g, auth.uid()) on conflict do nothing;
  return g;
end $$;

-- Garantit qu'un groupe non vide garde au moins un responsable.
create or replace function public._assurer_responsable(g uuid) returns void
language plpgsql security definer set search_path = public as $$
declare u uuid;
begin
  if not exists (select 1 from public.groupe_membres where groupe_id = g) then
    delete from public.groupes where id = g; return;
  end if;
  if not exists (select 1 from public.groupe_membres where groupe_id = g and role = 'responsable') then
    select user_id into u from public.groupe_membres where groupe_id = g
      order by (role = 'moderateur') desc, joined_at limit 1;
    update public.groupe_membres set role = 'responsable' where groupe_id = g and user_id = u;
  end if;
end $$;

create or replace function public.quitter_groupe(g uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  delete from public.groupe_membres where groupe_id = g and user_id = auth.uid();
  perform public._assurer_responsable(g);
end $$;

create or replace function public.definir_role(g uuid, u uuid, r text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.est_responsable(g) then raise exception 'Réservé au responsable du groupe'; end if;
  if r not in ('responsable','moderateur','membre') then raise exception 'Rôle invalide'; end if;
  update public.groupe_membres set role = r where groupe_id = g and user_id = u;
  if not exists (select 1 from public.groupe_membres where groupe_id = g and role = 'responsable') then
    raise exception 'Le groupe doit garder au moins un responsable';
  end if;
end $$;

create or replace function public.exclure_membre(g uuid, u uuid) returns void
language plpgsql security definer set search_path = public as $$
declare cible text;
begin
  select role into cible from public.groupe_membres where groupe_id = g and user_id = u;
  if cible is null then return; end if;
  if u = auth.uid() then raise exception 'Utilise « Quitter le groupe »'; end if;
  if not (public.est_responsable(g) or (public.peut_moderer(g) and cible = 'membre')) then
    raise exception 'Droits insuffisants';
  end if;
  delete from public.groupe_membres where groupe_id = g and user_id = u;
  perform public._assurer_responsable(g);
end $$;

create or replace function public.regenerer_code(g uuid) returns text
language plpgsql security definer set search_path = public as $$
declare c text;
begin
  if not public.est_responsable(g) then raise exception 'Réservé au responsable du groupe'; end if;
  c := upper(substr(md5(random()::text || clock_timestamp()::text), 1, 6));
  update public.groupes set code = c where id = g;
  return c;
end $$;

-- 7. Réponses déclarées sur l'honneur ---------------------------------------
create table if not exists public.reponses (
  id               uuid primary key default gen_random_uuid(),
  groupe_id        uuid not null references public.groupes(id) on delete cascade,
  exercice_id      text not null check (char_length(exercice_id) between 1 and 80),
  user_id          uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  contenu          text not null default '' check (char_length(contenu) <= 20000),
  photos           text[] not null default '{}' check (cardinality(photos) <= 4),
  engagement       boolean not null check (engagement),
  engagement_texte text not null check (char_length(engagement_texte) between 10 and 600),
  aide_consultee   boolean not null default false,
  created_at       timestamptz not null default now(),
  unique (groupe_id, exercice_id, user_id),
  check (char_length(trim(contenu)) > 0 or cardinality(photos) > 0)
);
create index if not exists reponses_ex on public.reponses(groupe_id, exercice_id);

create or replace function public.reponse_avant_insert() returns trigger
language plpgsql security definer set search_path = public as $$
declare p text;
begin
  new.user_id := auth.uid();
  new.created_at := now();
  foreach p in array new.photos loop
    if p not like new.groupe_id::text || '/' || new.user_id::text || '/%' then
      raise exception 'Chemin de photo invalide';
    end if;
  end loop;
  return new;
end $$;
drop trigger if exists reponses_avant_insert on public.reponses;
create trigger reponses_avant_insert before insert on public.reponses
  for each row execute function public.reponse_avant_insert();

-- 8. Notes de 0 à 10 par les pairs --------------------------------------------
create table if not exists public.notes (
  reponse_id    uuid not null references public.reponses(id) on delete cascade,
  evaluateur_id uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  note          smallint not null check (note between 0 and 10),
  updated_at    timestamptz not null default now(),
  primary key (reponse_id, evaluateur_id)
);

create or replace function public.groupe_de_reponse(r uuid) returns uuid
language sql stable security definer set search_path = public as $$
  select groupe_id from public.reponses where id = r;
$$;
-- Peut noter : membre du groupe de la réponse, et pas son auteur.
create or replace function public.peut_noter(r uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.reponses x
                 where x.id = r and x.user_id <> auth.uid() and public.role_groupe(x.groupe_id) is not null);
$$;

-- 9. Fil de discussion sous chaque exercice ------------------------------------
create table if not exists public.commentaires (
  id          uuid primary key default gen_random_uuid(),
  groupe_id   uuid not null references public.groupes(id) on delete cascade,
  exercice_id text not null check (char_length(exercice_id) between 1 and 80),
  reponse_id  uuid references public.reponses(id) on delete cascade,
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  contenu     text not null check (char_length(trim(contenu)) between 1 and 4000),
  created_at  timestamptz not null default now(),
  edited_at   timestamptz
);
create index if not exists commentaires_ex on public.commentaires(groupe_id, exercice_id, created_at);

create or replace function public.commentaire_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    new.user_id := auth.uid(); new.created_at := now(); new.edited_at := null;
    if new.reponse_id is not null and not exists (select 1 from public.reponses r where r.id = new.reponse_id
         and r.groupe_id = new.groupe_id and r.exercice_id = new.exercice_id) then
      raise exception 'Réponse visée invalide';
    end if;
  else  -- seule la modification du texte est permise
    new.groupe_id := old.groupe_id; new.exercice_id := old.exercice_id; new.reponse_id := old.reponse_id;
    new.user_id := old.user_id; new.created_at := old.created_at; new.edited_at := now();
  end if;
  return new;
end $$;
drop trigger if exists commentaires_avant_ecriture on public.commentaires;
create trigger commentaires_avant_ecriture before insert or update on public.commentaires
  for each row execute function public.commentaire_avant_ecriture();

-- Sécurité (RLS) ------------------------------------------------------------
alter table public.groupes        enable row level security;
alter table public.groupe_membres enable row level security;
alter table public.reponses       enable row level security;
alter table public.notes          enable row level security;
alter table public.commentaires   enable row level security;

drop policy if exists "profil: lire co-membres" on public.profiles;
create policy "profil: lire co-membres" on public.profiles for select using (public.partage_groupe(id));

drop policy if exists "groupes: lire" on public.groupes;
create policy "groupes: lire" on public.groupes for select using (public.est_membre(id));
drop policy if exists "groupes: modifier" on public.groupes;
create policy "groupes: modifier" on public.groupes for update using (public.est_responsable(id));
drop policy if exists "groupes: supprimer" on public.groupes;
create policy "groupes: supprimer" on public.groupes for delete using (public.est_responsable(id));

drop policy if exists "membres: lire" on public.groupe_membres;
create policy "membres: lire" on public.groupe_membres for select using (public.est_membre(groupe_id));

drop policy if exists "réponses: lire" on public.reponses;
create policy "réponses: lire" on public.reponses for select using (public.est_membre(groupe_id));
drop policy if exists "réponses: soumettre" on public.reponses;
create policy "réponses: soumettre" on public.reponses for insert
  with check (user_id = auth.uid() and public.role_groupe(groupe_id) is not null and engagement);
drop policy if exists "réponses: modérer" on public.reponses;
create policy "réponses: modérer" on public.reponses for delete using (public.peut_moderer(groupe_id));

drop policy if exists "notes: lire" on public.notes;
create policy "notes: lire" on public.notes for select using (public.est_membre(public.groupe_de_reponse(reponse_id)));
drop policy if exists "notes: donner" on public.notes;
create policy "notes: donner" on public.notes for insert
  with check (evaluateur_id = auth.uid() and public.peut_noter(reponse_id));
drop policy if exists "notes: changer" on public.notes;
create policy "notes: changer" on public.notes for update
  using (evaluateur_id = auth.uid()) with check (evaluateur_id = auth.uid() and public.peut_noter(reponse_id));
drop policy if exists "notes: retirer" on public.notes;
create policy "notes: retirer" on public.notes for delete using (evaluateur_id = auth.uid());

drop policy if exists "commentaires: lire" on public.commentaires;
create policy "commentaires: lire" on public.commentaires for select using (public.est_membre(groupe_id));
drop policy if exists "commentaires: écrire" on public.commentaires;
create policy "commentaires: écrire" on public.commentaires for insert
  with check (user_id = auth.uid() and public.role_groupe(groupe_id) is not null);
drop policy if exists "commentaires: modifier le sien" on public.commentaires;
create policy "commentaires: modifier le sien" on public.commentaires for update using (user_id = auth.uid());
drop policy if exists "commentaires: supprimer" on public.commentaires;
create policy "commentaires: supprimer" on public.commentaires for delete
  using (user_id = auth.uid() or public.peut_moderer(groupe_id));

-- Photos des réponses : stockage privé, chemin <groupe>/<auteur>/<fichier>.jpg
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('reponses', 'reponses', false, 2097152, array['image/jpeg'])
on conflict (id) do nothing;

create or replace function public.groupe_du_chemin(p text) returns uuid
language plpgsql immutable as $$
begin return (string_to_array(p, '/'))[1]::uuid; exception when others then return null; end $$;

drop policy if exists "photos réponses: déposer" on storage.objects;
create policy "photos réponses: déposer" on storage.objects for insert to authenticated
  with check (bucket_id = 'reponses' and (string_to_array(name, '/'))[2] = auth.uid()::text
              and public.role_groupe(public.groupe_du_chemin(name)) is not null);
drop policy if exists "photos réponses: voir" on storage.objects;
create policy "photos réponses: voir" on storage.objects for select to authenticated
  using (bucket_id = 'reponses' and public.est_membre(public.groupe_du_chemin(name)));
drop policy if exists "photos réponses: supprimer" on storage.objects;
create policy "photos réponses: supprimer" on storage.objects for delete to authenticated
  using (bucket_id = 'reponses' and ((string_to_array(name, '/'))[2] = auth.uid()::text
         or public.peut_moderer(public.groupe_du_chemin(name))));

-- Temps réel : réponses, notes et commentaires apparaissent sans recharger
do $$ begin alter publication supabase_realtime add table public.reponses;       exception when duplicate_object then null; end $$;
do $$ begin alter publication supabase_realtime add table public.notes;          exception when duplicate_object then null; end $$;
do $$ begin alter publication supabase_realtime add table public.commentaires;   exception when duplicate_object then null; end $$;
do $$ begin alter publication supabase_realtime add table public.groupe_membres; exception when duplicate_object then null; end $$;

-- =====================================================================
--  APRÈS avoir créé ton propre compte sur le site, exécute ceci
--  (remplace l'adresse) pour devenir professeur :
--
--  update public.profiles set role = 'prof'
--  where id = (select id from auth.users where email = 'ton.email@exemple.fr');
-- =====================================================================
