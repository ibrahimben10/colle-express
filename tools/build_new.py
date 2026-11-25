# Ajoute les exercices des fichiers new_*.py aux bases JSON (idempotent : remplace les ids n-*).
import json, sys, importlib
sys.path.insert(0, 'tools')
import newlib
for m in ['new_phys1', 'new_phys2', 'new_chim', 'new_math', 'new_src_x', 'new_src_alg', 'new_src_ana', 'new_info_1', 'new_info_2', 'new_phys_src1', 'new_phys_src2']:
    importlib.import_module(m)
E = [e for e in json.load(open('data/exercices.json')) if not e['id'].startswith(('n-', 'i-'))]
C = {k: v for k, v in json.load(open('data/corriges.json')).items() if not k.startswith(('n-', 'i-'))}
E += newlib.E; C.update(newlib.C)
json.dump(E, open('data/exercices.json', 'w'), ensure_ascii=False, indent=1)
json.dump(C, open('data/corriges.json', 'w'), ensure_ascii=False)
print(len(newlib.E), 'ajoutés ;', len(E), 'exercices au total')
