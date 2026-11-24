"""Découpe data/corriges.json en un petit fichier par exercice (data/corr/<id>.json),
chargé par le site seulement à l'ouverture de l'exercice.
Lancé automatiquement à la fin de build_bilan.py ; peut aussi se lancer seul."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((root / 'data/corriges.json').read_text())
out = root / 'data/corr'; out.mkdir(exist_ok=True)
for f in out.glob('*.json'):
    if f.stem not in C: f.unlink()
for i, v in C.items():
    p = out / f'{i}.json'; s = json.dumps(v, ensure_ascii=False, separators=(',', ':'))
    if not p.exists() or p.read_text() != s: p.write_text(s)
print(f'{len(C)} corrigés découpés dans data/corr/')
