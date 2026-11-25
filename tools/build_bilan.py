# Ajoute à data/corriges.json les bilans (théorèmes & définitions, astuces & réflexes) de tools/bilan_*.py.
# À lancer après toute régénération des corrigés (tools/build_new.py, tools/corr_*.py).
import json, sys, importlib
sys.path.insert(0, 'tools')
B = {}
for m in ['bilan_m1', 'bilan_m2', 'bilan_p1', 'bilan_n', 'bilan_s', 'bilan_i']:
    B.update(importlib.import_module(m).B)
E = json.load(open('data/exercices.json')); C = json.load(open('data/corriges.json'))
ids = {e['id'] for e in E}
manque = sorted(ids - set(B)); inconnus = sorted(set(B) - ids)
for i, (th, ast) in B.items():
    if i in C: C[i]['theoremes'], C[i]['astuces'] = list(th), list(ast)
json.dump(C, open('data/corriges.json', 'w'), ensure_ascii=False)
print(f'{len(set(B) & ids)} bilans ; sans bilan : {manque} ; ids inconnus : {inconnus}')
import build_split  # découpe par exercice pour le site
