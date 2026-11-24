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
--  PROFILS, ACTIVITÉ, ÉTOILES, CONTRIBUTIONS, COMMENTAIRES PUBLICS
--  Principe : profil privé par défaut ; visible des SEULS membres connectés
--  quand l'élève le rend public ; chaque section a sa propre visibilité.
--  Aucune adresse e-mail n'est jamais renvoyée par ces fonctions.
-- =====================================================================

-- 10. Profil personnel (séparé de "profiles" pour ne rien exposer aux co-membres)
create table if not exists public.profils (
  user_id       uuid primary key references public.profiles(id) on delete cascade,
  username      text unique check (username ~ '^[a-z0-9][a-z0-9_]{2,19}$'),
  bio           text not null default '' check (char_length(bio) <= 280),
  etablissement text not null default '' check (char_length(etablissement) <= 80),
  filiere       text not null default '' check (filiere in ('','MPSI','MP2I','MP','MP*','PCSI','PC','PC*','PSI','PSI*','PT','PT*','TSI','BCPST','Autre')),
  annee         smallint check (annee between 1 and 5),
  matieres      text[] not null default '{}' check (cardinality(matieres) <= 8),
  objectif      text not null default '' check (char_length(objectif) <= 160),
  lien_github   text not null default '' check (lien_github = '' or lien_github ~ '^https://(www\.)?github\.com/[A-Za-z0-9_.-]{1,60}/?$'),
  lien_linkedin text not null default '' check (lien_linkedin = '' or lien_linkedin ~ '^https://([a-z]{2,3}\.)?linkedin\.com/in/[A-Za-z0-9_%-]{1,100}/?$'),
  lien_site     text not null default '' check (lien_site = '' or (lien_site ~ '^https://[^\s<>"]{4,200}$')),
  public        boolean not null default false,
  vis_stats     boolean not null default true,
  vis_activite  boolean not null default true,
  vis_parcours  boolean not null default true,
  vis_favoris   boolean not null default true,
  vis_commentaires boolean not null default true,
  vis_etoiles   boolean not null default true,
  updated_at    timestamptz not null default now()
);

-- Identifiant proposé à partir du nom : "Chloé Martin" -> "chloe_martin", puis _2, _3… si déjà pris
create or replace function public._username_libre(nom text, uid uuid) returns text
language plpgsql security definer set search_path = public as $$
declare b text; c text; i int := 1;
begin
  b := lower(translate(coalesce(nom, ''), 'ÀÁÂÃÄÅàáâãäåÇçÈÉÊËèéêëÌÍÎÏìíîïÑñÒÓÔÕÖòóôõöÙÚÛÜùúûüÝýÿŒœÆæ', 'AAAAAAaaaaaaCcEEEEeeeeIIIIiiiiNnOOOOOoooooUUUUuuuuYyyOoAa'));
  b := trim(both '_' from regexp_replace(b, '[^a-z0-9]+', '_', 'g'));
  b := left(b, 16);
  if char_length(b) < 3 then b := 'eleve_' || left(replace(uid::text, '-', ''), 6); end if;
  if b !~ '^[a-z0-9]' then b := 'e' || b; end if;
  c := b;
  while exists (select 1 from public.profils where username = c and user_id <> uid) loop
    i := i + 1; c := left(b, 16) || '_' || i;
  end loop;
  return c;
end $$;

-- Création automatique du profil pour les nouveaux comptes et pour les comptes existants
create or replace function public.profil_auto() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profils (user_id, username) values (new.id, public._username_libre(new.full_name, new.id))
  on conflict (user_id) do nothing;
  return new;
end $$;
drop trigger if exists profiles_profil_auto on public.profiles;
create trigger profiles_profil_auto after insert on public.profiles
  for each row execute function public.profil_auto();
insert into public.profils (user_id, username)
  select p.id, public._username_libre(p.full_name, p.id) from public.profiles p
  where not exists (select 1 from public.profils x where x.user_id = p.id)
  order by p.created_at;

create or replace function public.profil_avant_maj() returns trigger
language plpgsql as $$
begin
  new.user_id := old.user_id; new.updated_at := now();
  new.username := lower(trim(new.username));
  new.bio := trim(new.bio); new.objectif := trim(new.objectif); new.etablissement := trim(new.etablissement);
  return new;
end $$;
drop trigger if exists profils_avant_maj on public.profils;
create trigger profils_avant_maj before update on public.profils
  for each row execute function public.profil_avant_maj();

alter table public.profils enable row level security;
drop policy if exists "profils: lire le sien ou admin" on public.profils;
create policy "profils: lire le sien ou admin" on public.profils for select using (user_id = auth.uid() or public.is_prof());
drop policy if exists "profils: modifier le sien" on public.profils;
create policy "profils: modifier le sien" on public.profils for update using (user_id = auth.uid()) with check (user_id = auth.uid());

-- 11. Journal d'activité réel (une ligne par exercice, type et jour) -----------
--  vu = exercice ouvert ; indice = indice demandé ; corrige = corrigé ouvert ; reponse = réponse soumise
create table if not exists public.activite (
  id          bigint generated always as identity primary key,
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  exercice_id text not null check (char_length(exercice_id) between 1 and 80),
  kind        text not null check (kind in ('vu','indice','corrige','reponse')),
  jour        date not null default (now() at time zone 'Europe/Paris')::date,
  created_at  timestamptz not null default now(),
  unique (user_id, exercice_id, kind, jour)
);
create index if not exists activite_user_jour on public.activite(user_id, jour);

-- Le navigateur ne peut ni antidater ni écrire pour un autre (l'éditeur SQL, lui, peut reprendre l'historique)
create or replace function public.activite_avant_insert() returns trigger
language plpgsql as $$
begin
  if auth.uid() is not null then
    new.user_id := auth.uid(); new.created_at := now(); new.jour := (now() at time zone 'Europe/Paris')::date;
  end if;
  return new;
end $$;
drop trigger if exists activite_avant_insert on public.activite;
create trigger activite_avant_insert before insert on public.activite
  for each row execute function public.activite_avant_insert();

alter table public.activite enable row level security;
drop policy if exists "activité: lire la sienne ou admin" on public.activite;
create policy "activité: lire la sienne ou admin" on public.activite for select using (user_id = auth.uid() or public.is_prof());
drop policy if exists "activité: enregistrer la sienne" on public.activite;
create policy "activité: enregistrer la sienne" on public.activite for insert with check (user_id = auth.uid());

-- Reprise de l'historique RÉEL déjà enregistré (réponses soumises et journal de suivi), sans rien inventer
insert into public.activite (user_id, exercice_id, kind, jour, created_at)
  select r.user_id, r.exercice_id, 'reponse', (r.created_at at time zone 'Europe/Paris')::date, r.created_at from public.reponses r
on conflict do nothing;
insert into public.activite (user_id, exercice_id, kind, jour, created_at)
  select s.user_id, left(j->>'id', 80),
         case j->>'k' when 'indice' then 'indice' when 'corrige' then 'corrige' else 'reponse' end,
         (to_timestamp((j->>'d')::double precision / 1000) at time zone 'Europe/Paris')::date,
         to_timestamp((j->>'d')::double precision / 1000)
  from public.suivi s, jsonb_array_elements(case when jsonb_typeof(s.data->'journal') = 'array' then s.data->'journal' else '[]'::jsonb end) j
  where coalesce(j->>'id', '') <> '' and (j->>'d') ~ '^[0-9]+(\.[0-9]+)?$'
    and j->>'k' in ('indice','corrige','reponse','copie')
on conflict do nothing;

-- 12. Étoiles (1 à 5) données par les membres connectés à un profil public -----
create table if not exists public.etoiles (
  cible_id    uuid not null references public.profiles(id) on delete cascade,
  auteur_id   uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  note        smallint not null check (note between 1 and 5),
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  primary key (cible_id, auteur_id),
  check (cible_id <> auteur_id)
);
create or replace function public.etoile_avant_ecriture() returns trigger
language plpgsql as $$
begin
  new.auteur_id := coalesce(auth.uid(), new.auteur_id); new.updated_at := now();
  if tg_op = 'UPDATE' then new.cible_id := old.cible_id; new.created_at := old.created_at; end if;
  return new;
end $$;
drop trigger if exists etoiles_avant_ecriture on public.etoiles;
create trigger etoiles_avant_ecriture before insert or update on public.etoiles
  for each row execute function public.etoile_avant_ecriture();
alter table public.etoiles enable row level security;
-- Chacun ne lit que SES notes (les autres restent anonymes) ; l'administrateur voit tout pour modérer
drop policy if exists "étoiles: lire les siennes ou admin" on public.etoiles;
create policy "étoiles: lire les siennes ou admin" on public.etoiles for select using (auteur_id = auth.uid() or public.is_prof());
drop policy if exists "étoiles: donner" on public.etoiles;
create or replace function public.accepte_etoiles(u uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profils p where p.user_id = u and p.public and p.vis_etoiles);
$$;
create policy "étoiles: donner" on public.etoiles for insert with check (
  auteur_id = auth.uid() and cible_id <> auth.uid() and public.accepte_etoiles(cible_id));
drop policy if exists "étoiles: changer" on public.etoiles;
create policy "étoiles: changer" on public.etoiles for update using (auteur_id = auth.uid()) with check (auteur_id = auth.uid());
drop policy if exists "étoiles: retirer" on public.etoiles;
create policy "étoiles: retirer" on public.etoiles for delete using (auteur_id = auth.uid() or public.is_prof());

-- 13. Contributions : sujets PDF envoyés à l'administrateur (seul le fait est enregistré, pas le fichier)
create table if not exists public.contributions (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  titre       text not null default '' check (char_length(titre) <= 120),
  created_at  timestamptz not null default now()
);
create or replace function public.contribution_avant_insert() returns trigger
language plpgsql as $$
begin
  if auth.uid() is not null then new.user_id := auth.uid(); new.created_at := now(); end if;
  if (select count(*) from public.contributions c where c.user_id = new.user_id and c.created_at > now() - interval '1 day') >= 10 then
    raise exception 'Trop de contributions aujourd''hui';
  end if;
  return new;
end $$;
drop trigger if exists contributions_avant_insert on public.contributions;
create trigger contributions_avant_insert before insert on public.contributions
  for each row execute function public.contribution_avant_insert();
alter table public.contributions enable row level security;
drop policy if exists "contributions: lire les siennes ou admin" on public.contributions;
create policy "contributions: lire les siennes ou admin" on public.contributions for select using (user_id = auth.uid() or public.is_prof());
drop policy if exists "contributions: déclarer" on public.contributions;
create policy "contributions: déclarer" on public.contributions for insert with check (user_id = auth.uid());
drop policy if exists "contributions: supprimer admin" on public.contributions;
create policy "contributions: supprimer admin" on public.contributions for delete using (public.is_prof());

-- 14. Commentaires publics : visibles de tous les membres connectés et sur le profil de l'auteur
alter table public.commentaires add column if not exists public boolean not null default false;
create index if not exists commentaires_public on public.commentaires(exercice_id, created_at) where public;
create index if not exists commentaires_auteur_public on public.commentaires(user_id, created_at) where public;
create or replace function public.commentaire_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    new.user_id := auth.uid(); new.created_at := now(); new.edited_at := null;
    if new.reponse_id is not null and not exists (select 1 from public.reponses r where r.id = new.reponse_id
         and r.groupe_id = new.groupe_id and r.exercice_id = new.exercice_id) then
      raise exception 'Réponse visée invalide';
    end if;
    -- Un commentaire public ne peut pas viser une réponse privée du groupe
    if new.public and new.reponse_id is not null then new.public := false; end if;
  else  -- seule la modification du texte est permise (la visibilité est fixée à la publication)
    new.groupe_id := old.groupe_id; new.exercice_id := old.exercice_id; new.reponse_id := old.reponse_id;
    new.user_id := old.user_id; new.created_at := old.created_at; new.edited_at := now(); new.public := old.public;
  end if;
  return new;
end $$;
drop policy if exists "commentaires: lire" on public.commentaires;
create policy "commentaires: lire" on public.commentaires for select
  using (public.est_membre(groupe_id) or (public and auth.uid() is not null));
drop policy if exists "commentaires: supprimer" on public.commentaires;
create policy "commentaires: supprimer" on public.commentaires for delete
  using (user_id = auth.uid() or public.peut_moderer(groupe_id) or public.is_prof());

-- 15. Lecture d'un profil : une seule porte d'entrée, qui applique la confidentialité ----
-- p_ref : @identifiant ou identifiant interne ; p_apercu : voir son propre profil "comme les autres"
create or replace function public.profil_public(p_ref text, p_apercu boolean default false) returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare
  me uuid := auth.uid(); u uuid; pr public.profils; pf public.profiles; sv jsonb;
  self boolean; admin boolean; tout boolean; r jsonb; ref text := lower(trim(both '@ ' from coalesce(p_ref, '')));
  et record; mine smallint;
begin
  if me is null then return null; end if;
  if ref ~ '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$' then u := ref::uuid;
  else select user_id into u from public.profils where username = ref; end if;
  if u is null then return null; end if;
  select * into pr from public.profils where user_id = u;
  select * into pf from public.profiles where id = u;
  if pf.id is null then return null; end if;
  if pr.user_id is null then
    insert into public.profils (user_id, username) values (u, public._username_libre(pf.full_name, u)) on conflict do nothing;
    select * into pr from public.profils where user_id = u;
  end if;
  self := (u = me) and not p_apercu;
  admin := public.is_prof() and not p_apercu;
  tout := self or admin;
  if not (pr.public or tout or u = me) then
    return jsonb_build_object('id', u, 'username', pr.username, 'nom', pf.full_name, 'prive', true);
  end if;
  select data into sv from public.suivi where user_id = u;
  r := jsonb_build_object(
    'id', u, 'username', pr.username, 'nom', pf.full_name, 'photo', coalesce(sv->>'photo', ''),
    'bio', pr.bio, 'etablissement', pr.etablissement, 'filiere', pr.filiere, 'annee', pr.annee,
    'matieres', to_jsonb(pr.matieres), 'objectif', pr.objectif,
    'liens', jsonb_build_object('github', pr.lien_github, 'linkedin', pr.lien_linkedin, 'site', pr.lien_site),
    'public', pr.public, 'self', self, 'admin', public.is_prof(), 'membre_depuis', pf.created_at,
    'role', case when pf.role = 'prof' then 'admin' else 'eleve' end,
    'contributions', (select count(*) from public.contributions c where c.user_id = u));
  if tout then
    r := r || jsonb_build_object('vis', jsonb_build_object('stats', pr.vis_stats, 'activite', pr.vis_activite, 'parcours', pr.vis_parcours,
      'favoris', pr.vis_favoris, 'commentaires', pr.vis_commentaires, 'etoiles', pr.vis_etoiles));
  end if;
  if tout or pr.vis_stats or pr.vis_parcours then
    r := r || jsonb_build_object(
      'vus',       (select coalesce(jsonb_agg(distinct exercice_id), '[]') from public.activite where user_id = u and kind = 'vu'),
      'travailles',(select coalesce(jsonb_agg(distinct x), '[]') from (
                      select exercice_id x from public.activite where user_id = u and kind in ('indice','reponse')
                      union select exercice_id from public.reponses where user_id = u) t),
      'termines',  (select coalesce(jsonb_agg(distinct exercice_id), '[]') from public.reponses where user_id = u),
      'sans_aide', (select coalesce(jsonb_agg(distinct exercice_id), '[]') from public.reponses where user_id = u and not aide_consultee),
      'reussis',   (select coalesce(jsonb_agg(distinct r2.exercice_id), '[]') from public.reponses r2
                     where r2.user_id = u and (select count(*) from public.notes n where n.reponse_id = r2.id) >= 2
                       and (select avg(n.note) from public.notes n where n.reponse_id = r2.id) >= 6));
  end if;
  if tout or pr.vis_activite then
    r := r || jsonb_build_object('jours', (select coalesce(jsonb_agg(jsonb_build_object('j', jour, 'ids', ids) order by jour), '[]') from (
      select jour, jsonb_agg(distinct exercice_id) ids from public.activite
      where user_id = u and kind in ('indice','reponse') and jour > (now() at time zone 'Europe/Paris')::date - 371
      group by jour) d));
  end if;
  if tout or pr.vis_favoris then
    r := r || jsonb_build_object('favoris', case when jsonb_typeof(sv->'fav') = 'array' then sv->'fav' else '[]'::jsonb end);
  end if;
  if tout or pr.vis_commentaires then
    r := r || jsonb_build_object('commentaires', (select coalesce(jsonb_agg(jsonb_build_object('id', c.id, 'ex', c.exercice_id, 'contenu', c.contenu, 'd', c.created_at) order by c.created_at desc), '[]')
      from (select * from public.commentaires where user_id = u and public order by created_at desc limit 30) c));
  end if;
  if tout or pr.vis_etoiles then
    select count(*) n, round(avg(note)::numeric, 1) moy into et from public.etoiles where cible_id = u;
    select note into mine from public.etoiles where cible_id = u and auteur_id = me;
    -- La moyenne n'apparaît qu'à partir de 3 notes, pour préserver l'anonymat des auteurs
    r := r || jsonb_build_object('etoiles', jsonb_build_object('n', et.n, 'moy', case when et.n >= 3 or admin then et.moy end,
      'mienne', mine, 'peut_noter', (u <> me and pr.public and pr.vis_etoiles)));
  end if;
  return r || public._profil_extras(u, tout) || public._profil_social(u, tout);
end $$;

-- Liste des notes reçues par un profil, pour la modération (administrateur seulement)
create or replace function public.etoiles_moderation(p_cible uuid) returns table(auteur_id uuid, auteur text, note smallint, updated_at timestamptz)
language sql stable security definer set search_path = public as $$
  select e.auteur_id, p.full_name, e.note, e.updated_at from public.etoiles e join public.profiles p on p.id = e.auteur_id
  where public.is_prof() and e.cible_id = p_cible order by e.updated_at desc;
$$;

-- =====================================================================
--  PHASE 3 : collections, carnet de progression, objectifs, badges
--  Badges et progression des objectifs sont CALCULÉS par le serveur à partir
--  de l'activité réelle : ils ne peuvent pas être saisis ni gonflés depuis le site.
-- =====================================================================
-- 16. Métadonnées des exercices du site (matière, chapitre, niveau), pour que le serveur
--     calcule lui-même badges et objectifs. Régénérée par tools/build_meta.py.
create table if not exists public.exercices_meta (
  id text primary key, mat text not null, chap text not null, niveau int not null
);
insert into public.exercices_meta (id, mat, chap, niveau) values
  ('m-ccmp-01a','Maths','Topologie & convexité',2),
  ('m-ccmp-01b','Maths','Probabilités',2),
  ('m-ccmp-02a','Maths','Équations différentielles',1),
  ('m-ccmp-02b','Maths','Réduction',2),
  ('m-ccmp-03a','Maths','Algèbre & arithmétique',3),
  ('m-ccmp-03b','Maths','Séries',2),
  ('m-ccmp-04a','Maths','Séries entières',2),
  ('m-ccmp-04b','Maths','Groupes',3),
  ('m-ccmp-04c','Maths','Probabilités',1),
  ('m-ccmp-05a','Maths','Probabilités',2),
  ('m-ccmp-05b','Maths','Algèbre linéaire',2),
  ('m-ccmp-06a','Maths','Réduction',1),
  ('m-ccmp-06b','Maths','Probabilités',2),
  ('m-ccmp-07a','Maths','Séries',2),
  ('m-ccmp-07b','Maths','Algèbre euclidienne',2),
  ('m-ccmp-08a','Maths','Arithmétique',2),
  ('m-ccmp-08b','Maths','Séries',1),
  ('m-ccmp-09','Maths','Intégration',2),
  ('m-ccmp-10b','Maths','Réduction',2),
  ('m-ccmp-11a','Maths','Algèbre euclidienne',2),
  ('m-ccmp-11b','Maths','Approximation',3),
  ('m-ccmp-12a','Maths','Intégration',2),
  ('m-ccmp-12b','Maths','Réduction',2),
  ('m-ccmp-13a','Maths','Réduction',1),
  ('m-ccmp-13b','Maths','Intégration',2),
  ('m-ccmp-14a','Maths','Algèbre euclidienne',2),
  ('m-ccmp-14b','Maths','Intégrales à paramètre',1),
  ('m-ccmp-15a','Maths','Réduction',3),
  ('m-ccmp-15b','Maths','Topologie & convexité',1),
  ('m-ccmp-17a','Maths','Probabilités',2),
  ('m-ccmp-17b','Maths','Analyse asymptotique',2),
  ('m-ccmp-17c','Maths','Réduction',2),
  ('m-ccmp-19a','Maths','Algèbre linéaire',2),
  ('m-ccmp-19b','Maths','Intégrales à paramètre',1),
  ('m-ccmp-20a','Maths','Séries de fonctions',1),
  ('m-ccmp-20b','Maths','Réduction',2),
  ('m-ccmp-21b','Maths','Géométrie euclidienne',1),
  ('m-ccmp-24b','Maths','Algèbre linéaire',3),
  ('m-ccmp-25a','Maths','Intégration',3),
  ('m-ccmp-26a','Maths','Polynômes',1),
  ('m-ccmp-27a','Maths','Calcul différentiel',1),
  ('m-ccmp-27b','Maths','Réduction',1),
  ('m-ccmp-27c','Maths','Probabilités',1),
  ('m-ccmp-28a','Maths','Groupes & représentations',2),
  ('m-ccmp-28b','Maths','Intégrales à paramètre',2),
  ('m-ccs-01','Maths','Topologie matricielle',2),
  ('m-ccs-02','Maths','Séries de fonctions',1),
  ('m-ccs-03','Maths','Probabilités',2),
  ('m-ccs-05','Maths','Polynômes',3),
  ('m-ccs-06','Maths','Séries entières',2),
  ('m-ccs-07','Maths','Séries de Fourier & EDP',2),
  ('m-ccs-10','Maths','Séries entières',2),
  ('m-ccs-11','Maths','Intégrales à paramètre',2),
  ('m-ccs-12','Maths','Probabilités',1),
  ('m-ccs-14','Maths','Algèbre & arithmétique',3),
  ('m-ccs-15','Maths','Calcul différentiel',2),
  ('m-ccs-mi8','Maths','Séries entières',2),
  ('x-g-1','Maths','Groupes',3),
  ('x-g-2','Maths','Groupes',3),
  ('x-a-1','Maths','Anneaux',3),
  ('x-ar-1','Maths','Arithmétique',3),
  ('x-ar-2','Maths','Arithmétique',3),
  ('x-p-1','Maths','Polynômes',3),
  ('x-al-1','Maths','Algèbre linéaire',3),
  ('x-al-2','Maths','Déterminants',3),
  ('x-al-3','Maths','Déterminants',3),
  ('x-al-4','Maths','Déterminants',3),
  ('x-r-1','Maths','Réduction',3),
  ('x-r-2','Maths','Réduction',3),
  ('x-r-3','Maths','Réduction',3),
  ('x-r-4','Maths','Exponentielle de matrices',3),
  ('x-r-5','Maths','Groupes de matrices',3),
  ('x-an-1','Maths','Intégration',3),
  ('x-an-2','Maths','Intégration',3),
  ('x-an-3','Maths','Suites de fonctions',3),
  ('x-s-1','Maths','Suites',3),
  ('x-s-2','Maths','Suites',3),
  ('x-s-3','Maths','Suites',3),
  ('x-se-1','Maths','Séries',3),
  ('x-se-2','Maths','Séries',3),
  ('x-f-1','Maths','Fonctions d''une variable',3),
  ('x-f-2','Maths','Fonctions d''une variable',3),
  ('x-f-3','Maths','Fonctions d''une variable',3),
  ('x-fo-1','Maths','Séries de Fourier',3),
  ('c-thermo-1','Chimie','Thermochimie',1),
  ('c-sol-2','Chimie','Solutions aqueuses',2),
  ('c-redox-3','Chimie','Oxydoréduction',2),
  ('c-thermo-4','Chimie','Thermochimie',2),
  ('c-thermo-6','Chimie','Thermochimie',2),
  ('c-electro-3','Chimie','Électrochimie',2),
  ('c-electro-5','Chimie','Électrochimie',2),
  ('c-cin-2','Chimie','Cinétique',1),
  ('c-cristallo-1','Chimie','Cristallographie',1),
  ('c-cristallo-2','Chimie','Cristallographie',2),
  ('p-em-1','Physique','Électrostatique',1),
  ('p-em-2','Physique','Électrostatique',2),
  ('p-em-3','Physique','Magnétostatique',1),
  ('p-max-1','Physique','Équations de Maxwell',1),
  ('p-max-2','Physique','Équations de Maxwell',2),
  ('p-max-3','Physique','Équations de Maxwell',2),
  ('p-ind-2','Physique','Induction',2),
  ('p-ind-3','Physique','Induction',1),
  ('p-ondes-1','Physique','Ondes mécaniques',1),
  ('p-ondes-2','Physique','Ondes mécaniques',2),
  ('p-oem-2','Physique','Ondes électromagnétiques',1),
  ('p-oem-3','Physique','Ondes électromagnétiques',2),
  ('p-oem-4','Physique','Ondes électromagnétiques',2),
  ('p-oem-5','Physique','Ondes électromagnétiques',2),
  ('p-meca-1','Physique','Mécanique',1),
  ('p-meca-2','Physique','Mécanique',2),
  ('p-meca-3','Physique','Mécanique',2),
  ('p-meca-4','Physique','Mécanique',3),
  ('p-meca-5','Physique','Mécanique',3),
  ('p-meca-6','Physique','Mécanique',2),
  ('p-meca-7','Physique','Mécanique',2),
  ('p-meca-8','Physique','Mécanique',2),
  ('p-meca-9','Physique','Mécanique',3),
  ('p-meca-10','Physique','Mécanique',3),
  ('p-meca-ccmp2','Physique','Mécanique',2),
  ('p-meca-ccmp13','Physique','Mécanique',2),
  ('p-meca-ccs1','Physique','Mécanique',2),
  ('p-meca-ccs3','Physique','Mécanique',2),
  ('p-meca-ccs-ressort','Physique','Mécanique',1),
  ('p-opt-2','Physique','Optique géométrique',2),
  ('p-opt-3','Physique','Optique géométrique',1),
  ('p-opt-4','Physique','Optique ondulatoire',2),
  ('p-opt-5','Physique','Optique ondulatoire',1),
  ('p-opt-6','Physique','Optique ondulatoire',1),
  ('p-opt-7','Physique','Optique ondulatoire',2),
  ('p-opt-8','Physique','Optique ondulatoire',3),
  ('p-opt-ccmp1','Physique','Optique ondulatoire',1),
  ('p-q-1','Physique','Mécanique quantique',1),
  ('p-q-2','Physique','Mécanique quantique',2),
  ('p-q-3','Physique','Mécanique quantique',2),
  ('p-q-4','Physique','Mécanique quantique',2),
  ('p-stat-1','Physique','Physique statistique',2),
  ('p-stat-3','Physique','Physique statistique',3),
  ('p-th-1','Physique','Thermodynamique',1),
  ('p-th-4','Physique','Thermodynamique',2),
  ('p-th-spe1','Physique','Diffusion thermique',2),
  ('p-th-spe2','Physique','Rayonnement',1),
  ('p-th-spe3','Physique','Rayonnement',3),
  ('p-th-spe4','Physique','Rayonnement',3),
  ('p-th-spe5','Physique','Diffusion thermique',2),
  ('p-th-spe6','Physique','Diffusion thermique',1),
  ('p-th-ccs4','Physique','Diffusion thermique',1),
  ('p-th-ccmp4','Physique','Diffusion thermique',2),
  ('p-th-ccmp15','Physique','Diffusion thermique',2),
  ('p-chim-ccs6','Chimie','Thermochimie',1),
  ('p-ccs-bulle','Physique','Mécanique des fluides',1),
  ('p-ccs-plan','Physique','Électrostatique',2),
  ('n-p1-rc','Physique','Électrocinétique',1),
  ('n-p1-rlc','Physique','Électrocinétique',1),
  ('n-p1-passebas','Physique','Électrocinétique',1),
  ('n-p1-passebande','Physique','Électrocinétique',1),
  ('n-p1-corde','Physique','Ondes mécaniques',1),
  ('n-p1-ultrasons','Physique','Ondes mécaniques',1),
  ('n-p1-fente','Physique','Optique ondulatoire',1),
  ('n-p1-projecteur','Physique','Optique géométrique',1),
  ('n-p1-lunette','Physique','Optique géométrique',1),
  ('n-p1-prisme','Physique','Optique géométrique',1),
  ('n-p1-photo','Physique','Mécanique quantique',1),
  ('n-p1-debroglie','Physique','Mécanique quantique',1),
  ('n-p1-puits','Physique','Mécanique quantique',1),
  ('n-p1-chute','Physique','Mécanique',1),
  ('n-p1-geostat','Physique','Mécanique',1),
  ('n-p1-pendule','Physique','Mécanique',1),
  ('n-p1-rails','Physique','Induction',1),
  ('n-p1-transfo','Physique','Induction',1),
  ('n-p1-adiab','Physique','Thermodynamique',1),
  ('n-p1-frigo','Physique','Thermodynamique',1),
  ('n-p1-glacon','Physique','Thermodynamique',1),
  ('n-p1-atmo','Physique','Mécanique des fluides',1),
  ('n-p1-bobine','Physique','Induction',1),
  ('n-p2-ailette','Physique','Diffusion thermique',2),
  ('n-p2-isolant','Physique','Diffusion thermique',2),
  ('n-p2-peau','Physique','Équations de Maxwell',2),
  ('n-p2-bohr','Physique','Mécanique quantique',2),
  ('n-p2-marche','Physique','Mécanique quantique',2),
  ('n-p2-doublet','Physique','Optique ondulatoire',2),
  ('n-p2-reseau','Physique','Optique ondulatoire',2),
  ('n-p2-tige','Physique','Mécanique',2),
  ('n-p2-resonance','Physique','Mécanique',2),
  ('n-p2-fourier','Physique','Électrocinétique',2),
  ('n-p2-coax','Physique','Électrostatique',2),
  ('n-p2-serre','Physique','Rayonnement',2),
  ('n-p2-dipole','Physique','Électrostatique',2),
  ('n-p2-plasma','Physique','Ondes électromagnétiques',2),
  ('n-p2-roulement','Physique','Mécanique',2),
  ('n-p2-beau','Physique','Thermodynamique',2),
  ('n-p2-vdw','Physique','Thermodynamique',2),
  ('n-p2-voile','Physique','Ondes électromagnétiques',2),
  ('n-p2-alternateur','Physique','Induction',2),
  ('n-p2-diffusion','Physique','Diffusion thermique',2),
  ('n-p3-neutron','Physique','Mécanique quantique',3),
  ('n-c-fer','Chimie','Atomistique',1),
  ('n-c-vsepr','Chimie','Structure des molécules',1),
  ('n-c-h2o2','Chimie','Cinétique',1),
  ('n-c-arrhenius','Chimie','Cinétique',1),
  ('n-c-vitinit','Chimie','Cinétique',1),
  ('n-c-ethanoique','Chimie','Acide-base',1),
  ('n-c-tampon','Chimie','Acide-base',1),
  ('n-c-agcl','Chimie','Solubilité',1),
  ('n-c-mgoh2','Chimie','Solubilité',2),
  ('n-c-nacl','Chimie','Cristallographie',1),
  ('n-c-daniell','Chimie','Oxydoréduction',1),
  ('n-c-permanganate','Chimie','Oxydoréduction',1),
  ('n-c-conducti','Chimie','Acide-base',1),
  ('n-c-epH','Chimie','Oxydoréduction',2),
  ('n-c-flamme','Chimie','Thermochimie',2),
  ('n-c-ellingham','Chimie','Thermochimie',2),
  ('n-c-electrolyse','Chimie','Électrochimie',2),
  ('n-c-aeqs','Chimie','Cinétique',2),
  ('n-m-max','Maths','Probabilités',1),
  ('n-m-euler','Maths','Équations différentielles',1),
  ('n-m-abb','Maths','Algèbre euclidienne',1),
  ('n-m-antisym','Maths','Algèbre euclidienne',1),
  ('n-m-phiX1','Maths','Réduction',1),
  ('n-m-ln1t','Maths','Séries entières',1),
  ('n-m-wallis','Maths','Séries',1),
  ('n-m-arctanx2','Maths','Intégration',1),
  ('n-m-symk','Maths','Réduction',1),
  ('n-m-chth','Maths','Séries',1),
  ('n-m-extrema','Maths','Calcul différentiel',2),
  ('n-m-In','Maths','Séries entières',2),
  ('n-m-double','Maths','Séries',2),
  ('n-m-blocs','Maths','Réduction',2),
  ('n-m-pieces','Maths','Probabilités',2),
  ('n-m-Jn','Maths','Intégration',2),
  ('n-m-sintx','Maths','Intégrales à paramètre',2),
  ('n-m-arctantx','Maths','Intégrales à paramètre',2),
  ('n-m-geodiff','Maths','Probabilités',2),
  ('n-m-kerf2','Maths','Algèbre linéaire',2)
on conflict (id) do update set mat = excluded.mat, chap = excluded.chap, niveau = excluded.niveau;
alter table public.exercices_meta enable row level security;
drop policy if exists "méta: lecture" on public.exercices_meta;
create policy "méta: lecture" on public.exercices_meta for select using (auth.uid() is not null);

-- Domaine scientifique d'un exercice (même règle que js/profil.js)
create or replace function public.domaine(p_mat text, p_chap text) returns text
language sql immutable as $$
  select case
    when p_mat = 'Chimie' then 'Chimie'
    when p_mat = 'Maths' then case
      when p_chap ~* 'proba' then 'Probabilités'
      when p_chap ~* '(r[ée]duction|alg[èe]bre|groupe|arithm|polyn|d[ée]terminant|matric|espaces? vect)' then 'Algèbre'
      else 'Analyse' end
    else case
      when p_chap ~* 'quantique' then 'Physique quantique'
      when p_chap ~* '(thermo|diffusion|statistique)' then 'Thermodynamique'
      when p_chap ~* '(optique|ondes m[ée]ca|interf|diffraction)' then 'Optique & ondes'
      when p_chap ~* '(lectro|induction|maxwell|magn[ée]t|rayonnement)' then 'Électromagnétisme'
      else 'Mécanique' end
  end;
$$;
create or replace function public.ex_meta(p_id text) returns table(mat text, chap text, dom text)
language sql stable security definer set search_path = public as $$
  select m.mat, m.chap, public.domaine(m.mat, m.chap) from public.exercices_meta m where m.id = p_id
  union all
  select b.mat, b.chap, public.domaine(b.mat, b.chap) from public.banque b where b.id::text = p_id
  limit 1;
$$;

alter table public.profils add column if not exists vis_collections boolean not null default true;
alter table public.profils add column if not exists vis_carnet      boolean not null default true;
alter table public.profils add column if not exists vis_badges      boolean not null default true;

-- 17. Collections d'exercices ----------------------------------------------------
create table if not exists public.collections (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  titre       text not null check (char_length(trim(titre)) between 1 and 80),
  description text not null default '' check (char_length(description) <= 300),
  public      boolean not null default false,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create index if not exists collections_user on public.collections(user_id, created_at);
create table if not exists public.collection_items (
  collection_id uuid not null references public.collections(id) on delete cascade,
  exercice_id   text not null check (char_length(exercice_id) between 1 and 80),
  position      int  not null default 0,
  added_at      timestamptz not null default now(),
  primary key (collection_id, exercice_id)
);
create or replace function public.collection_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    if auth.uid() is not null then new.user_id := auth.uid(); new.created_at := now(); end if;
    if (select count(*) from public.collections where user_id = new.user_id) >= 50 then raise exception 'Limite de 50 collections atteinte'; end if;
  else new.user_id := old.user_id; new.created_at := old.created_at; end if;
  new.titre := trim(new.titre); new.updated_at := now();
  return new;
end $$;
drop trigger if exists collections_avant_ecriture on public.collections;
create trigger collections_avant_ecriture before insert or update on public.collections
  for each row execute function public.collection_avant_ecriture();
create or replace function public.est_ma_collection(c uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.collections where id = c and user_id = auth.uid());
$$;
create or replace function public.item_avant_insert() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  new.added_at := now();
  if (select count(*) from public.collection_items where collection_id = new.collection_id) >= 200 then raise exception 'Limite de 200 exercices par collection'; end if;
  return new;
end $$;
drop trigger if exists items_avant_insert on public.collection_items;
create trigger items_avant_insert before insert on public.collection_items
  for each row execute function public.item_avant_insert();

alter table public.collections enable row level security;
alter table public.collection_items enable row level security;
drop policy if exists "collections: lire les siennes" on public.collections;
create policy "collections: lire les siennes" on public.collections for select using (user_id = auth.uid() or public.is_prof());
drop policy if exists "collections: créer" on public.collections;
create policy "collections: créer" on public.collections for insert with check (user_id = auth.uid());
drop policy if exists "collections: modifier" on public.collections;
create policy "collections: modifier" on public.collections for update using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists "collections: supprimer" on public.collections;
create policy "collections: supprimer" on public.collections for delete using (user_id = auth.uid() or public.is_prof());
drop policy if exists "items: lire" on public.collection_items;
create policy "items: lire" on public.collection_items for select using (public.est_ma_collection(collection_id) or public.is_prof());
drop policy if exists "items: ajouter" on public.collection_items;
create policy "items: ajouter" on public.collection_items for insert with check (public.est_ma_collection(collection_id));
drop policy if exists "items: déplacer" on public.collection_items;
create policy "items: déplacer" on public.collection_items for update using (public.est_ma_collection(collection_id)) with check (public.est_ma_collection(collection_id));
drop policy if exists "items: retirer" on public.collection_items;
create policy "items: retirer" on public.collection_items for delete using (public.est_ma_collection(collection_id));

-- 18. Carnet de progression (privé par défaut ; certaines notes peuvent être publiées)
create table if not exists public.carnet (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  type        text not null check (type in ('difficile','erreur','theoreme','demo','note','refaire','appris')),
  titre       text not null check (char_length(trim(titre)) between 1 and 120),
  contenu     text not null default '' check (char_length(contenu) <= 8000),
  exercice_id text check (exercice_id is null or char_length(exercice_id) between 1 and 80),
  public      boolean not null default false,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create index if not exists carnet_user on public.carnet(user_id, created_at desc);
create or replace function public.carnet_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    if auth.uid() is not null then new.user_id := auth.uid(); new.created_at := now(); end if;
    if (select count(*) from public.carnet where user_id = new.user_id) >= 500 then raise exception 'Le carnet est plein (500 notes)'; end if;
  else new.user_id := old.user_id; new.created_at := old.created_at; end if;
  new.titre := trim(new.titre); new.updated_at := now();
  return new;
end $$;
drop trigger if exists carnet_avant_ecriture on public.carnet;
create trigger carnet_avant_ecriture before insert or update on public.carnet
  for each row execute function public.carnet_avant_ecriture();
alter table public.carnet enable row level security;
-- Notes privées : lisibles par leur auteur SEUL (pas même l'administrateur)
drop policy if exists "carnet: lire le sien" on public.carnet;
create policy "carnet: lire le sien" on public.carnet for select using (user_id = auth.uid() or (public and public.is_prof()));
drop policy if exists "carnet: écrire" on public.carnet;
create policy "carnet: écrire" on public.carnet for insert with check (user_id = auth.uid());
drop policy if exists "carnet: modifier" on public.carnet;
create policy "carnet: modifier" on public.carnet for update using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists "carnet: supprimer" on public.carnet;
create policy "carnet: supprimer" on public.carnet for delete using (user_id = auth.uid() or (public and public.is_prof()));

-- 19. Objectifs personnels (progression calculée sur l'activité réelle) ------------
create table if not exists public.objectifs (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  type        text not null check (type in ('exercices','chapitres','refaire','autonomie')),
  titre       text not null check (char_length(trim(titre)) between 1 and 140),
  cible       smallint not null check (cible between 1 and 200),
  domaine     text not null default '' check (domaine in ('','Analyse','Algèbre','Probabilités','Mécanique','Électromagnétisme','Thermodynamique','Optique & ondes','Physique quantique','Chimie')),
  debut       date not null default (now() at time zone 'Europe/Paris')::date,
  fin         date not null,
  partage     boolean not null default false,
  archive     boolean not null default false,
  created_at  timestamptz not null default now(),
  check (fin >= debut and fin <= debut + 180)
);
create or replace function public.objectif_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    if auth.uid() is not null then new.user_id := auth.uid(); new.created_at := now(); end if;
    if (select count(*) from public.objectifs where user_id = new.user_id and not archive) >= 12 then raise exception 'Douze objectifs en cours au plus'; end if;
  else new.user_id := old.user_id; new.created_at := old.created_at; new.debut := old.debut; new.type := old.type; end if;
  return new;
end $$;
drop trigger if exists objectifs_avant_ecriture on public.objectifs;
create trigger objectifs_avant_ecriture before insert or update on public.objectifs
  for each row execute function public.objectif_avant_ecriture();
alter table public.objectifs enable row level security;
drop policy if exists "objectifs: les siens" on public.objectifs;
create policy "objectifs: les siens" on public.objectifs for all using (user_id = auth.uid()) with check (user_id = auth.uid());

create or replace function public.objectif_progression(o public.objectifs) returns int
language sql stable security definer set search_path = public as $$
  with trav as (   -- exercices travaillés (indice ou réponse) pendant la période
    select distinct a.exercice_id, min(a.jour) j from public.activite a
    where a.user_id = o.user_id and a.kind in ('indice','reponse') and a.jour between o.debut and o.fin
    group by a.exercice_id),
  m as (select t.exercice_id, t.j, x.chap, x.dom from trav t cross join lateral public.ex_meta(t.exercice_id) x)
  select case o.type
    when 'exercices' then (select count(*) from m where o.domaine = '' or m.dom = o.domaine)
    when 'chapitres' then (select count(distinct chap) from m where o.domaine = '' or m.dom = o.domaine)
    when 'autonomie' then (select count(distinct r.exercice_id) from public.reponses r cross join lateral public.ex_meta(r.exercice_id) x
                           where r.user_id = o.user_id and not r.aide_consultee
                             and (r.created_at at time zone 'Europe/Paris')::date between o.debut and o.fin
                             and (o.domaine = '' or x.dom = o.domaine))
    when 'refaire' then (select count(distinct c.exercice_id) from public.carnet c
                         where c.user_id = o.user_id and c.type in ('refaire','difficile') and c.exercice_id is not null
                           and exists (select 1 from public.activite a where a.user_id = o.user_id and a.exercice_id = c.exercice_id
                                       and a.kind in ('indice','reponse') and a.created_at > c.created_at
                                       and a.jour between o.debut and o.fin))
  end::int;
$$;
create or replace function public.mes_objectifs() returns jsonb
language sql stable security definer set search_path = public as $$
  select coalesce(jsonb_agg(to_jsonb(o) || jsonb_build_object('progression', public.objectif_progression(o)) order by o.archive, o.fin), '[]')
  from public.objectifs o where o.user_id = auth.uid();
$$;

-- 20. Badges : critères transparents, recalculés à chaque lecture -------------------
create or replace function public.badges(u uuid) returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare
  termines int; sans_aide int; reussis int; chapitres int; domaines3 int; serie int; refaits int; contrib int; meilleur record;
begin
  select count(distinct exercice_id) into termines from public.reponses where user_id = u;
  select count(distinct exercice_id) into sans_aide from public.reponses where user_id = u and not aide_consultee;
  select count(distinct r.exercice_id) into reussis from public.reponses r
    where r.user_id = u and (select count(*) from public.notes n where n.reponse_id = r.id) >= 2
      and (select avg(n.note) from public.notes n where n.reponse_id = r.id) >= 6;
  with t as (select distinct exercice_id from public.activite where user_id = u and kind in ('indice','reponse')
             union select exercice_id from public.reponses where user_id = u)
  select count(distinct x.chap), (select count(*) from (select x2.dom from t t2 cross join lateral public.ex_meta(t2.exercice_id) x2 group by x2.dom having count(*) >= 3) d)
    into chapitres, domaines3 from t cross join lateral public.ex_meta(t.exercice_id) x;
  with j as (select distinct jour from public.activite where user_id = u and kind in ('indice','reponse')),
       g as (select jour, jour - (row_number() over (order by jour))::int grp from j)
  select coalesce(max(n), 0) into serie from (select count(*) n from g group by grp) s;
  select count(distinct c.exercice_id) into refaits from public.carnet c
    where c.user_id = u and c.type in ('refaire','difficile') and c.exercice_id is not null
      and exists (select 1 from public.activite a where a.user_id = u and a.exercice_id = c.exercice_id and a.kind in ('indice','reponse') and a.created_at > c.created_at + interval '1 day');
  select count(*) into contrib from public.contributions where user_id = u;
  select x.dom, count(distinct r.exercice_id) n into meilleur from public.reponses r cross join lateral public.ex_meta(r.exercice_id) x
    where r.user_id = u group by x.dom order by 2 desc limit 1;
  return jsonb_build_array(
    jsonb_build_object('id','premier_pas','titre','Premier pas','critere','Soumettre sa première réponse sur l’honneur','val',termines,'cible',1),
    jsonb_build_object('id','regularite','titre','Régularité','critere','Travailler 7 jours d’affilée (au moins un indice ou une réponse par jour)','val',serie,'cible',7),
    jsonb_build_object('id','explorateur','titre','Explorateur','critere','Travailler des exercices dans 5 chapitres différents','val',chapitres,'cible',5),
    jsonb_build_object('id','polyvalent','titre','Polyvalent','critere','Travailler au moins 3 exercices dans 3 domaines différents','val',domaines3,'cible',3),
    jsonb_build_object('id','autonome','titre','Autonome','critere','Soumettre 10 réponses sans avoir consulté d’indice ni de corrigé','val',sans_aide,'cible',10),
    jsonb_build_object('id','reconnu','titre','Reconnu par ses pairs','critere','5 exercices réussis : au moins 2 notes de camarades, moyenne ≥ 6/10','val',reussis,'cible',5),
    jsonb_build_object('id','perseverant','titre','Persévérant','critere','Retravailler 5 exercices notés « à refaire » ou « difficile » dans son carnet, au moins un jour plus tard','val',refaits,'cible',5),
    jsonb_build_object('id','specialiste','titre','Passionné · ' || coalesce(meilleur.dom, 'un domaine'),'critere','Terminer 15 exercices d’un même domaine','val',coalesce(meilleur.n, 0),'cible',15),
    jsonb_build_object('id','contributeur','titre','Contributeur','critere','Envoyer un sujet d’oral en PDF pour enrichir la plateforme','val',contrib,'cible',1));
end $$;

-- 21. Sections publiques supplémentaires du profil -----------------------------------
create or replace function public._profil_extras(u uuid, tout boolean) returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare pr public.profils; r jsonb := '{}'::jsonb; b jsonb;
begin
  select * into pr from public.profils where user_id = u;
  if tout then r := r || jsonb_build_object('vis3', jsonb_build_object('collections', pr.vis_collections, 'carnet', pr.vis_carnet, 'badges', pr.vis_badges)); end if;
  if tout or pr.vis_collections then
    r := r || jsonb_build_object('collections', (select coalesce(jsonb_agg(jsonb_build_object('id', c.id, 'titre', c.titre, 'description', c.description, 'public', c.public,
        'n', (select count(*) from public.collection_items i where i.collection_id = c.id)) order by c.created_at), '[]')
      from public.collections c where c.user_id = u and (tout or c.public)));
  end if;
  if tout or pr.vis_carnet then
    r := r || jsonb_build_object('carnet', (select coalesce(jsonb_agg(jsonb_build_object('id', c.id, 'type', c.type, 'titre', c.titre, 'contenu', left(c.contenu, 1200), 'ex', c.exercice_id, 'd', c.created_at) order by c.created_at desc), '[]')
      from (select * from public.carnet where user_id = u and public order by created_at desc limit 20) c));
  end if;
  r := r || jsonb_build_object('objectifs', (select coalesce(jsonb_agg(jsonb_build_object('titre', o.titre, 'type', o.type, 'cible', o.cible, 'domaine', o.domaine, 'debut', o.debut, 'fin', o.fin,
      'progression', public.objectif_progression(o)) order by o.fin), '[]')
    from public.objectifs o where o.user_id = u and o.partage and not o.archive and o.fin >= (now() at time zone 'Europe/Paris')::date - 7));
  if tout or pr.vis_badges then
    b := public.badges(u);
    if not tout then b := (select coalesce(jsonb_agg(x), '[]') from jsonb_array_elements(b) x where (x->>'val')::int >= (x->>'cible')::int); end if;
    r := r || jsonb_build_object('badges', b);
  end if;
  return r;
end $$;

-- Lecture d'une collection partagée : publique ET profil public, ou propriétaire, ou administrateur
create or replace function public.collection_publique(p_id uuid) returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare c public.collections; pr public.profils; nom text; me uuid := auth.uid();
begin
  if me is null then return null; end if;
  select * into c from public.collections where id = p_id;
  if c.id is null then return null; end if;
  select * into pr from public.profils where user_id = c.user_id;
  if not (c.user_id = me or public.is_prof() or (c.public and pr.public and pr.vis_collections)) then return jsonb_build_object('prive', true); end if;
  select full_name into nom from public.profiles where id = c.user_id;
  return jsonb_build_object('id', c.id, 'titre', c.titre, 'description', c.description, 'public', c.public, 'self', c.user_id = me,
    'auteur', jsonb_build_object('id', c.user_id, 'nom', nom, 'username', pr.username),
    'items', (select coalesce(jsonb_agg(i.exercice_id order by i.position, i.added_at), '[]') from public.collection_items i where i.collection_id = c.id));
end $$;

-- =====================================================================
--  PHASE 4 : annuaire, abonnements, solutions d'élèves, signalements, modération
-- =====================================================================
alter table public.profils add column if not exists annuaire boolean not null default false;

-- Limite anti-spam générique : n lignes au plus par auteur sur une fenêtre de temps
create or replace function public._limite(tbl regclass, col text, u uuid, n int, fenetre interval) returns void
language plpgsql security definer set search_path = public as $$
declare c int;
begin
  if u is null then return; end if;
  execute format('select count(*) from %s where %I = $1 and created_at > now() - $2', tbl, col) into c using u, fenetre;
  if c >= n then raise exception 'Trop de publications en peu de temps : réessaie plus tard.'; end if;
end $$;
create or replace function public.commentaire_antispam() returns trigger
language plpgsql security definer set search_path = public as $$
begin perform public._limite('public.commentaires', 'user_id', auth.uid(), 40, interval '1 hour'); return new; end $$;
drop trigger if exists commentaires_antispam on public.commentaires;
create trigger commentaires_antispam before insert on public.commentaires for each row execute function public.commentaire_antispam();

create or replace function public.profil_est_public(u uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profils p where p.user_id = u and p.public);
$$;

-- 22. Abonnements ----------------------------------------------------------------
create table if not exists public.abonnements (
  suiveur_id  uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  suivi_id    uuid not null references public.profiles(id) on delete cascade,
  created_at  timestamptz not null default now(),
  primary key (suiveur_id, suivi_id),
  check (suiveur_id <> suivi_id)
);
create index if not exists abonnements_suivi on public.abonnements(suivi_id);
alter table public.abonnements enable row level security;
drop policy if exists "abonnements: les miens" on public.abonnements;
create policy "abonnements: les miens" on public.abonnements for select using (suiveur_id = auth.uid() or public.is_prof());
drop policy if exists "abonnements: suivre" on public.abonnements;
create policy "abonnements: suivre" on public.abonnements for insert
  with check (suiveur_id = auth.uid() and suivi_id <> auth.uid() and public.profil_est_public(suivi_id));
drop policy if exists "abonnements: ne plus suivre" on public.abonnements;
create policy "abonnements: ne plus suivre" on public.abonnements for delete using (suiveur_id = auth.uid());

-- 23. Solutions publiées volontairement par des élèves --------------------------------
create table if not exists public.solutions (
  id          uuid primary key default gen_random_uuid(),
  exercice_id text not null check (char_length(exercice_id) between 1 and 80),
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  contenu     text not null check (char_length(trim(contenu)) between 20 and 20000),
  statut      text not null default 'publiee' check (statut in ('publiee','masquee')),
  verifiee    boolean not null default false,   -- relue et validée par l'administrateur
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  unique (exercice_id, user_id)
);
create index if not exists solutions_ex on public.solutions(exercice_id, created_at);
create or replace function public.solution_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    if auth.uid() is not null then new.user_id := auth.uid(); new.created_at := now(); end if;
    perform public._limite('public.solutions', 'user_id', new.user_id, 10, interval '1 day');
    if not public.is_prof() then new.statut := 'publiee'; new.verifiee := false; end if;
  else
    new.user_id := old.user_id; new.exercice_id := old.exercice_id; new.created_at := old.created_at;
    if not public.is_prof() then
      new.statut := old.statut; new.verifiee := old.verifiee;
      if new.contenu is distinct from old.contenu then new.verifiee := false; end if;   -- toute modification retire la validation
    end if;
  end if;
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists solutions_avant_ecriture on public.solutions;
create trigger solutions_avant_ecriture before insert or update on public.solutions
  for each row execute function public.solution_avant_ecriture();
alter table public.solutions enable row level security;
drop policy if exists "solutions: lire" on public.solutions;
create policy "solutions: lire" on public.solutions for select
  using (auth.uid() is not null and (statut = 'publiee' or user_id = auth.uid() or public.is_prof()));
drop policy if exists "solutions: publier" on public.solutions;
create policy "solutions: publier" on public.solutions for insert with check (user_id = auth.uid());
drop policy if exists "solutions: modifier" on public.solutions;
create policy "solutions: modifier" on public.solutions for update using (user_id = auth.uid() or public.is_prof());
drop policy if exists "solutions: supprimer" on public.solutions;
create policy "solutions: supprimer" on public.solutions for delete using (user_id = auth.uid() or public.is_prof());

create table if not exists public.solution_commentaires (
  id          uuid primary key default gen_random_uuid(),
  solution_id uuid not null references public.solutions(id) on delete cascade,
  user_id     uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  type        text not null default 'commentaire' check (type in ('commentaire','erreur')),
  contenu     text not null check (char_length(trim(contenu)) between 1 and 4000),
  created_at  timestamptz not null default now(),
  edited_at   timestamptz
);
create index if not exists solcom_sol on public.solution_commentaires(solution_id, created_at);
create or replace function public.solcom_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    if auth.uid() is not null then new.user_id := auth.uid(); new.created_at := now(); end if;
    new.edited_at := null;
    perform public._limite('public.solution_commentaires', 'user_id', new.user_id, 40, interval '1 hour');
  else new.solution_id := old.solution_id; new.user_id := old.user_id; new.type := old.type; new.created_at := old.created_at; new.edited_at := now(); end if;
  return new;
end $$;
drop trigger if exists solcom_avant_ecriture on public.solution_commentaires;
create trigger solcom_avant_ecriture before insert or update on public.solution_commentaires
  for each row execute function public.solcom_avant_ecriture();
create or replace function public.solution_visible(s uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.solutions x where x.id = s and (x.statut = 'publiee' or x.user_id = auth.uid() or public.is_prof()));
$$;
alter table public.solution_commentaires enable row level security;
drop policy if exists "solcom: lire" on public.solution_commentaires;
create policy "solcom: lire" on public.solution_commentaires for select using (auth.uid() is not null and public.solution_visible(solution_id));
drop policy if exists "solcom: écrire" on public.solution_commentaires;
create policy "solcom: écrire" on public.solution_commentaires for insert with check (user_id = auth.uid() and public.solution_visible(solution_id));
drop policy if exists "solcom: modifier" on public.solution_commentaires;
create policy "solcom: modifier" on public.solution_commentaires for update using (user_id = auth.uid());
drop policy if exists "solcom: supprimer" on public.solution_commentaires;
create policy "solcom: supprimer" on public.solution_commentaires for delete using (user_id = auth.uid() or public.is_prof());

-- 24. Signalements (contenu inapproprié, spam, erreur…) -----------------------------
create table if not exists public.signalements (
  id          uuid primary key default gen_random_uuid(),
  auteur_id   uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  cible_type  text not null check (cible_type in ('commentaire','solution','solution_commentaire','profil','carnet','collection')),
  cible_id    text not null check (char_length(cible_id) between 1 and 80),
  motif       text not null check (motif in ('spam','insulte','inapproprie','donnees','autre')),
  details     text not null default '' check (char_length(details) <= 500),
  traite      boolean not null default false,
  decision    text not null default '' check (char_length(decision) <= 200),
  created_at  timestamptz not null default now(),
  unique (auteur_id, cible_type, cible_id)
);
create or replace function public.signalement_avant_ecriture() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' then
    if auth.uid() is not null then new.auteur_id := auth.uid(); new.created_at := now(); end if;
    new.traite := false; new.decision := '';
    perform public._limite('public.signalements', 'auteur_id', new.auteur_id, 20, interval '1 day');
  else
    new.auteur_id := old.auteur_id; new.cible_type := old.cible_type; new.cible_id := old.cible_id; new.created_at := old.created_at;
  end if;
  return new;
end $$;
drop trigger if exists signalements_avant_ecriture on public.signalements;
create trigger signalements_avant_ecriture before insert or update on public.signalements
  for each row execute function public.signalement_avant_ecriture();
-- Trois signalements distincts sur une solution la masquent en attendant la décision de l'administrateur
create or replace function public.signalement_apres_insert() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if new.cible_type = 'solution' and (select count(*) from public.signalements s where s.cible_type = 'solution' and s.cible_id = new.cible_id and not s.traite) >= 3 then
    update public.solutions set statut = 'masquee' where id::text = new.cible_id;
  end if;
  return null;
end $$;
drop trigger if exists signalements_apres_insert on public.signalements;
create trigger signalements_apres_insert after insert on public.signalements
  for each row execute function public.signalement_apres_insert();
alter table public.signalements enable row level security;
drop policy if exists "signalements: les siens ou admin" on public.signalements;
create policy "signalements: les siens ou admin" on public.signalements for select using (auteur_id = auth.uid() or public.is_prof());
drop policy if exists "signalements: signaler" on public.signalements;
create policy "signalements: signaler" on public.signalements for insert with check (auteur_id = auth.uid());
drop policy if exists "signalements: traiter" on public.signalements;
create policy "signalements: traiter" on public.signalements for update using (public.is_prof());

-- File de modération (administrateur) : signalements ouverts, avec un extrait du contenu visé
create or replace function public.moderation_file() returns jsonb
language sql stable security definer set search_path = public as $$
  select coalesce(jsonb_agg(x order by x->>'dernier' desc), '[]') from (
    select jsonb_build_object('cible_type', s.cible_type, 'cible_id', s.cible_id, 'n', count(*), 'motifs', jsonb_agg(distinct s.motif),
      'details', jsonb_agg(s.details) filter (where s.details <> ''), 'dernier', max(s.created_at),
      'extrait', case s.cible_type
        when 'commentaire' then (select left(c.contenu, 300) from public.commentaires c where c.id::text = s.cible_id)
        when 'solution' then (select left(x.contenu, 300) from public.solutions x where x.id::text = s.cible_id)
        when 'solution_commentaire' then (select left(c.contenu, 300) from public.solution_commentaires c where c.id::text = s.cible_id)
        when 'carnet' then (select left(c.titre || ' — ' || c.contenu, 300) from public.carnet c where c.id::text = s.cible_id)
        when 'collection' then (select c.titre from public.collections c where c.id::text = s.cible_id)
        when 'profil' then (select coalesce(p.username, '') || ' — ' || left(p.bio, 200) from public.profils p where p.user_id::text = s.cible_id) end,
      'exercice', case s.cible_type
        when 'commentaire' then (select c.exercice_id from public.commentaires c where c.id::text = s.cible_id)
        when 'solution' then (select x.exercice_id from public.solutions x where x.id::text = s.cible_id)
        when 'solution_commentaire' then (select x.exercice_id from public.solution_commentaires c join public.solutions x on x.id = c.solution_id where c.id::text = s.cible_id) end) x
    from public.signalements s where not s.traite and public.is_prof()
    group by s.cible_type, s.cible_id) q;
$$;
-- Décision de l'administrateur : 'supprimer' le contenu, 'masquer' (solution), 'retablir' (solution) ou 'classer'
create or replace function public.moderer(p_type text, p_id text, p_action text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_prof() then raise exception 'Réservé à l''administrateur'; end if;
  if p_action = 'supprimer' then
    case p_type
      when 'commentaire' then delete from public.commentaires where id::text = p_id;
      when 'solution' then delete from public.solutions where id::text = p_id;
      when 'solution_commentaire' then delete from public.solution_commentaires where id::text = p_id;
      when 'carnet' then delete from public.carnet where id::text = p_id;
      when 'collection' then delete from public.collections where id::text = p_id;
      when 'profil' then update public.profils set public = false, annuaire = false, bio = '', objectif = '', lien_github = '', lien_linkedin = '', lien_site = '' where user_id::text = p_id;
      else null; end case;
  elsif p_action = 'masquer' and p_type = 'solution' then update public.solutions set statut = 'masquee' where id::text = p_id;
  elsif p_action = 'retablir' and p_type = 'solution' then update public.solutions set statut = 'publiee' where id::text = p_id;
  end if;
  update public.signalements set traite = true, decision = p_action where cible_type = p_type and cible_id = p_id and not traite;
end $$;

-- 25. Annuaire des profils publics qui ont choisi d'y apparaître (ordre alphabétique, aucun classement)
create or replace function public.annuaire(p_q text default '', p_filiere text default '', p_matiere text default '',
  p_etab text default '', p_collections boolean default false, p_suivis boolean default false, p_page int default 0) returns jsonb
language sql stable security definer set search_path = public as $$
  select coalesce(jsonb_agg(c order by lower(c->>'nom')), '[]') from (
    select jsonb_build_object('id', p.user_id, 'username', p.username, 'nom', pf.full_name, 'photo', coalesce(s.data->>'photo', ''),
      'filiere', p.filiere, 'annee', p.annee, 'etablissement', p.etablissement, 'matieres', to_jsonb(p.matieres), 'bio', left(p.bio, 160),
      'collections', (select count(*) from public.collections c where c.user_id = p.user_id and c.public and p.vis_collections),
      'abonnes', (select count(*) from public.abonnements a where a.suivi_id = p.user_id),
      'suivi', exists (select 1 from public.abonnements a where a.suiveur_id = auth.uid() and a.suivi_id = p.user_id)) c
    from public.profils p join public.profiles pf on pf.id = p.user_id left join public.suivi s on s.user_id = p.user_id
    where auth.uid() is not null and p.public and p.annuaire
      and (coalesce(p_q, '') = '' or pf.full_name ilike '%' || p_q || '%' or p.username ilike '%' || p_q || '%' or p.bio ilike '%' || p_q || '%')
      and (coalesce(p_filiere, '') = '' or p.filiere = p_filiere)
      and (coalesce(p_matiere, '') = '' or p_matiere = any(p.matieres))
      and (coalesce(p_etab, '') = '' or p.etablissement ilike '%' || p_etab || '%')
      and (not p_collections or exists (select 1 from public.collections c where c.user_id = p.user_id and c.public and p.vis_collections))
      and (not p_suivis or exists (select 1 from public.abonnements a where a.suiveur_id = auth.uid() and a.suivi_id = p.user_id))
    order by lower(pf.full_name) limit 24 offset greatest(0, least(p_page, 100)) * 24) q;
$$;

-- Fil des abonnements : dernières publications publiques des profils suivis
create or replace function public.fil_abonnements(p_limite int default 40) returns jsonb
language sql stable security definer set search_path = public as $$
  with suivis as (select a.suivi_id u from public.abonnements a join public.profils p on p.user_id = a.suivi_id
                  where a.suiveur_id = auth.uid() and p.public),
  ev as (
    select 'solution' k, s.user_id u, s.exercice_id ex, null::text titre, left(s.contenu, 240) txt, s.created_at d, s.id::text ref
      from public.solutions s where s.user_id in (select u from suivis) and s.statut = 'publiee'
    union all select 'commentaire', c.user_id, c.exercice_id, null, left(c.contenu, 240), c.created_at, c.id::text
      from public.commentaires c join public.profils p on p.user_id = c.user_id where c.user_id in (select u from suivis) and c.public and p.vis_commentaires
    union all select 'collection', c.user_id, null, c.titre, left(c.description, 240), c.created_at, c.id::text
      from public.collections c join public.profils p on p.user_id = c.user_id where c.user_id in (select u from suivis) and c.public and p.vis_collections
    union all select 'carnet', c.user_id, c.exercice_id, c.titre, left(c.contenu, 240), c.created_at, c.id::text
      from public.carnet c join public.profils p on p.user_id = c.user_id where c.user_id in (select u from suivis) and c.public and p.vis_carnet)
  select coalesce(jsonb_agg(jsonb_build_object('k', ev.k, 'u', ev.u, 'nom', pf.full_name, 'username', pr.username, 'photo', coalesce(sv.data->>'photo', ''),
    'ex', ev.ex, 'titre', ev.titre, 'txt', ev.txt, 'd', ev.d, 'ref', ev.ref) order by ev.d desc), '[]')
  from (select * from ev order by d desc limit least(greatest(p_limite, 1), 100)) ev
  join public.profiles pf on pf.id = ev.u left join public.profils pr on pr.user_id = ev.u left join public.suivi sv on sv.user_id = ev.u;
$$;

-- Les auteurs de solutions publiées ont aussi une « carte » (nom, identifiant, photo)
create or replace function public.cartes_auteurs(p_ids uuid[]) returns table(id uuid, nom text, username text, photo text)
language sql stable security definer set search_path = public as $$
  select p.id, p.full_name, x.username, coalesce(s.data->>'photo', '')
  from public.profiles p left join public.profils x on x.user_id = p.id left join public.suivi s on s.user_id = p.id
  where auth.uid() is not null and p.id = any(p_ids[1:200])
    and (p.id = auth.uid() or public.is_prof() or public.partage_groupe(p.id) or coalesce(x.public, false)
         or exists (select 1 from public.commentaires c where c.user_id = p.id and c.public)
         or exists (select 1 from public.solutions so where so.user_id = p.id and so.statut = 'publiee')
         or exists (select 1 from public.solution_commentaires sc where sc.user_id = p.id));
$$;

-- Infos sociales ajoutées au profil : abonnés, abonnement, solutions publiées
create or replace function public._profil_social(u uuid, tout boolean) returns jsonb
language sql stable security definer set search_path = public as $$
  select jsonb_build_object(
    'abonnes', (select count(*) from public.abonnements a where a.suivi_id = u),
    'abonnements', (select count(*) from public.abonnements a where a.suiveur_id = u),
    'je_suis', exists (select 1 from public.abonnements a where a.suiveur_id = auth.uid() and a.suivi_id = u),
    'annuaire', (select annuaire from public.profils where user_id = u),
    'solutions', (select coalesce(jsonb_agg(jsonb_build_object('id', s.id, 'ex', s.exercice_id, 'd', s.created_at, 'verifiee', s.verifiee, 'statut', s.statut) order by s.created_at desc), '[]')
                  from public.solutions s where s.user_id = u and (s.statut = 'publiee' or tout)));
$$;

-- =====================================================================
--  APRÈS avoir créé ton propre compte sur le site, exécute ceci
--  (remplace l'adresse) pour devenir professeur :
--
--  update public.profiles set role = 'prof'
--  where id = (select id from auth.users where email = 'ton.email@exemple.fr');
-- =====================================================================
