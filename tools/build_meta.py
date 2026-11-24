"""Régénère le bloc « exercices_meta » de supabase/schema.sql à partir de data/exercices.json.
Usage : python3 tools/build_meta.py   (puis relancer schema.sql dans Supabase)"""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
ex = json.loads((root / 'data/exercices.json').read_text())
q = lambda s: "'" + str(s).replace("'", "''") + "'"
rows = ",\n".join(f"  ({q(e['id'])},{q(e['mat'])},{q(e['chap'])},{int(e['niveau'])})" for e in ex)
sql = (root / 'supabase/schema.sql').read_text()
new = re.sub(r"(insert into public\.exercices_meta \(id, mat, chap, niveau\) values\n)(.*?)(\non conflict \(id\) do update)", lambda m: m.group(1) + rows + m.group(3), sql, flags=re.S)
(root / 'supabase/schema.sql').write_text(new)
print(f"{len(ex)} exercices écrits dans schema.sql")
