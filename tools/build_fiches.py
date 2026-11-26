"""Construit data/fiches/index.json et copie le texte des fiches (tools/fiches_src/*.md) dans data/fiches/."""
import json, os, re, shutil
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(H)
ns = {}; exec(open(os.path.join(H, 'fiches_liste.py'), encoding='utf-8').read(), ns)
PARTIE = [(r'^p1-', 'Signaux physiques'), (r'^p2-', 'Mécanique 1'), (r'^p3-', 'Mécanique 2'), (r'^p4-', 'Thermodynamique'),
          (r'^p5-', 'Induction'), (r'^px-', 'Outils'),
          (r'^mp-(referentiels|non-galileen|frottement)', 'Mécanique'), (r'^mp-(signal|numerique)', 'Électronique'),
          (r'^mp-(ondes-lumineuses|interferences|young|michelson|n-ondes)', 'Optique ondulatoire'),
          (r'^mp-(electrostatique|exemples-e|dipole-e|magnetostatique|dipole-m|maxwell|energie-em|ondes-vide|plasma|conducteur|rayonnement)', 'Électromagnétisme'),
          (r'^mp-(systemes-ouverts|diffusion|statistique)', 'Thermodynamique'), (r'^mp-(quantique|libre|potentiel)', 'Physique quantique'),
          (r'^c-(classification|lewis|intermoleculaire|cristal)', 'Structure de la matière'), (r'^c-(matiere|cinetique)', 'Transformations de la matière'),
          (r'^c-', 'Réactions en solution aqueuse'),
          (r'^i-(python|nombres|piles|fichiers|images)', 'Programmation'), (r'^i-(numpy|zeros|integration|edo|systemes|aleatoire)', 'Méthodes numériques'), (r'^i-(complexite|recherche|tris|recursivite|gloutons)', 'Algorithmique'), (r'^i-(graphes|plus-courts)', 'Graphes'),
          (r'^i-sql', 'Bases de données'), (r'^i-(dictionnaires|progdyn)', 'Dictionnaires et programmation dynamique'), (r'^i-(ia|jeux)', 'Intelligence artificielle et jeux')]
src = os.path.join(H, 'fiches_src'); out = os.path.join(ROOT, 'data', 'fiches'); os.makedirs(out, exist_ok=True)
idx = []
for mat, niv, fid, titre, L in ns['D']:
    partie = next(p for r, p in PARTIE if re.match(r, fid))
    pret = os.path.exists(os.path.join(src, fid + '.md'))
    mots = ''
    if pret:
        md = open(os.path.join(src, fid + '.md'), encoding='utf-8').read()
        for k in re.findall(r'\[\[fig:([\w-]+)\]\]', md):
            assert k.startswith(fid + '-'), (fid, k)
        shutil.copy(os.path.join(src, fid + '.md'), os.path.join(out, fid + '.md'))
        # mots-clés pour la recherche : titres de sections, termes en gras, noms des schémas (sans LaTeX)
        k = re.findall(r'^##+ (.+)$', md, re.M) + re.findall(r'\*\*([^*]+)\*\*', md) + [sch for sch, _, _ in L]
        k = [re.sub(r'\$[^$]*\$|[—.:]', ' ', x) for x in k if x not in ("L'essentiel", 'Méthode', 'Pièges classiques', 'Ordres de grandeur')]
        mots = ' '.join(dict.fromkeys(' '.join(k).split()))
    idx.append({'id': fid, 'titre': titre, 'mat': mat, 'niveau': niv, 'partie': partie, 'n': len(L), 'pret': pret, 'k': mots})
json.dump(idx, open(os.path.join(out, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(idx), 'fiches dont', sum(x['pret'] for x in idx), 'rédigées')
