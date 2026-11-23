# Outils communs pour les exercices ajoutés (énoncés originaux + indices + corrigés).
E, C = [], {}
CONC = {1: 'CCINP', 2: 'Mines-Centrale', 3: 'X-ENS'}

def ex(id, mat, chap, niveau, titre, duree, enonce, h1, h2, h3, corrige, reponse=''):
    assert id not in C, id
    E.append({'id': id, 'mat': mat, 'chap': chap, 'niveau': niveau, 'concours': CONC[niveau],
              'titre': titre, 'enonce': enonce.strip(), 'duree': duree})
    C[id] = {'indices': [h1.strip(), h2.strip(), h3.strip()], 'corrige': corrige.strip(), 'reponse': reponse.strip()}
