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
  if new.role is distinct from old.role and not public.is_prof() then
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
--  APRÈS avoir créé ton propre compte sur le site, exécute ceci
--  (remplace l'adresse) pour devenir professeur :
--
--  update public.profiles set role = 'prof'
--  where id = (select id from auth.users where email = 'ton.email@exemple.fr');
-- =====================================================================
