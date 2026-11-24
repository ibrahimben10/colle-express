# Remplace les corrigés par les versions détaillées définies dans tools/detail/d*.py (dictionnaire D : id -> texte).
# Un texte peut se terminer par « ===RÉPONSE=== résultat » pour remplacer aussi le résultat affiché.
import json, os, sys, importlib
sys.path.insert(0, 'tools/detail')
C = json.load(open('data/corriges.json'))
D = {}
for f in sorted(os.listdir('tools/detail')):
    if f.startswith('d') and f.endswith('.py'):
        D.update(importlib.import_module(f[:-3]).D)
for i, t in D.items():
    if i not in C: print('inconnu :', i); continue
    corr, _, rep = t.partition('===RÉPONSE===')
    C[i]['corrige'] = corr.strip()
    if rep.strip(): C[i]['reponse'] = rep.strip()
# Rédactions « rigoureuses » (type copie de concours) écrites à la main : tools/rig/r*.py (dictionnaire R : id -> texte).
sys.path.insert(0, 'tools/rig'); R = {}
for f in sorted(os.listdir('tools/rig')) if os.path.isdir('tools/rig') else []:
    if f.startswith('r') and f.endswith('.py'):
        R.update(importlib.import_module(f[:-3]).R)
for i, t in R.items():
    if i not in C: print('inconnu (rig) :', i); continue
    C[i]['rigoureux'] = t.strip()
json.dump(C, open('data/corriges.json', 'w'), ensure_ascii=False)
print(len(R), 'rédactions rigoureuses')
print(len(D), 'corrigés détaillés sur', len(C))
