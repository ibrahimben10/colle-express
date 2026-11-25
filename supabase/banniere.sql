-- Colle express : bannière de profil personnalisable.
-- À coller une fois dans Supabase > SQL Editor > Run. Sans risque à relancer ; rien n'est supprimé.
begin;
-- Bannière de profil choisie par l'élève : « motif:couleur » (vide = bannière par défaut)
alter table public.profils add column if not exists banniere text not null default ''
  check (banniere = '' or banniere ~ '^(onde|lissajous|champ|grille):(terra|vert|encre|ambre)$');

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
    'matieres', to_jsonb(pr.matieres), 'objectif', pr.objectif, 'banniere', coalesce(pr.banniere, ''),
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
                       and (select avg(n.note) from public.notes n where n.reponse_id = r2.id) >= 12));
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

commit;
