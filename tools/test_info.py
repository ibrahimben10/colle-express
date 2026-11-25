"""Exécute tout le code Python des exercices d'informatique (énoncés et corrigés) et vérifie
les résultats annoncés dans les corrigés. À lancer après toute modification :
    python3 tools/test_info.py
"""
import re, sys, os, math, random, tempfile, itertools
sys.path.insert(0, os.path.dirname(__file__))
import newlib
import new_info_1, new_info_2, new_info_3, new_info_4  # noqa: F401  (remplissent newlib.E / newlib.C)

def blocs(t):
    return re.findall(r"```python[ \t]*\n(.*?)\n[ \t]*```", t, re.S)

NS, ok, fails = {}, 0, []
for e in newlib.E:
    if not e['id'].startswith('i-'):
        continue
    ns = {}
    for b in blocs(e['enonce']) + blocs(newlib.C[e['id']]['corrige']):
        exec(compile(b, e['id'], 'exec'), ns)
    NS[e['id']] = ns

def check(nom, cond):
    global ok
    if cond: ok += 1
    else: fails.append(nom)

R = random.Random(1)
# --- Python
f = NS['i-py-max2']['deux_plus_grands']
for _ in range(300):
    L = [R.randint(-5, 5) for _ in range(R.randint(2, 9))]
    check('max2', f(L) == tuple(sorted(L)[-1:-3:-1]))
check('max2 ex', [f([3, 7]), f([5, 5, 1]), f([1, 2, 3, 4]), f([4, 3, 2, 1])] == [(7, 3), (5, 5), (4, 3), (4, 3)])
ns = NS['i-py-csv']
with tempfile.NamedTemporaryFile('w', suffix='.csv', delete=False, encoding='utf-8') as t:
    t.write('ville;temperature\nToulouse;14.5\nLille;8\nToulouse;15.5\n\n'); nom = t.name
check('csv', ns['moyennes'](ns['lire'](nom)) == {'Toulouse': 15.0, 'Lille': 8.0})
# --- Complexité
dicho = NS['i-cx-dicho']['dicho']
for n in range(0, 40):
    L = sorted(R.sample(range(100), n))
    for x in range(-1, 101):
        r = dicho(L, x)
        check('dicho', (r == -1 and x not in L) or (0 <= r < n and L[r] == x))
# nombre de passages <= floor(log2 n) + 1
def dicho_cpt(L, x):
    g, d, k = 0, len(L) - 1, 0
    while g <= d:
        k += 1; m = (g + d) // 2
        if L[m] == x: return k
        elif L[m] < x: g = m + 1
        else: d = m - 1
    return k
check('dicho iter', all(dicho_cpt(list(range(n)), x) <= int(math.log2(n)) + 1 for n in range(1, 300) for x in range(-1, n + 1)))
check('dicho n=8', dicho_cpt(list(range(8)), 99) == 4)
p = NS['i-cx-expo']['puissance']
check('expo', all(p(a, n) == a ** n for a in range(-3, 5) for n in range(0, 40)))
bits = bin(1000)[2:]; check('expo 1000', (len(bits), bits.count('1'), len(bits) + bits.count('1')) == (10, 6, 16))
check('expo 3^13', p(3, 13) == 1594323)
occ = NS['i-cx-motif']['occurrences']
check('motif', occ('abracadabra', 'abra') == [0, 7])
for _ in range(200):
    t = ''.join(R.choice('ab') for _ in range(R.randint(1, 12))); m = ''.join(R.choice('ab') for _ in range(R.randint(1, len(t))))
    check('motif rnd', occ(t, m) == [i for i in range(len(t) - len(m) + 1) if t[i:i + len(m)] == m])
# --- Piles
bf = NS['i-pile-par']['bien_formee']
check('par', [bf('([])[]'), bf('([)]'), bf('(()'), bf('())'), bf('')] == [True, False, False, False, True])
ev = NS['i-pile-rpn']['evaluer']
check('rpn', ev(['3', '4', '+', '2', '*']) == 14 and ev('5 1 - 2 3 + * 4 -'.split()) == 16 and ev(['5', '1', '-']) == 4 and (5 - 1) * (2 + 3) - 4 == 16)
ns = NS['i-rec-fibo']
def F(n): return n if n < 2 else F(n - 1) + F(n - 2)
cnt = [0]
def fibo_c(n):
    cnt[0] += 1
    return n if n < 2 else fibo_c(n - 1) + fibo_c(n - 2)
for n in range(0, 20):
    cnt[0] = 0; fibo_c(n); check('fibo A(n)', cnt[0] == 2 * F(n + 1) - 1)
check('fibo A(30)', 2 * F(31) - 1 == 2692537)
check('fibo versions', all(ns['fibo_iter'](n) == ns['fibo_memo'](n) == F(n) for n in range(25)) and ns['fibo'](15) == F(15))
h = NS['i-rec-hanoi']['hanoi']
check('hanoi 2', h(2) == [(1, 2), (1, 3), (2, 3)])
def valide(n, moves):
    P = {1: list(range(n, 0, -1)), 2: [], 3: []}
    for a, b in moves:
        if not P[a]: return False
        d = P[a].pop()
        if P[b] and P[b][-1] < d: return False
        P[b].append(d)
    return P[3] == list(range(n, 0, -1))
check('hanoi', all(len(h(n)) == 2 ** n - 1 and valide(n, h(n)) for n in range(0, 11)))
# --- Tris
ti = NS['i-tri-ins']['tri_insertion']
for _ in range(300):
    L = [R.randint(0, 9) for _ in range(R.randint(0, 12))]; M2 = L[:]; ti(M2); check('insertion', M2 == sorted(L))
# stabilité : tri de couples par la clé seulement
def ins_cle(L):
    for i in range(1, len(L)):
        x = L[i]; j = i
        while j > 0 and L[j - 1][0] > x[0]:
            L[j] = L[j - 1]; j -= 1
        L[j] = x
L = [(R.randint(0, 3), k) for k in range(30)]; M2 = L[:]; ins_cle(M2); check('stable', M2 == sorted(L, key=lambda c: c[0]))
ns = NS['i-tri-fus']
for _ in range(300):
    L = [R.randint(0, 50) for _ in range(R.randint(0, 20))]; check('fusion', ns['tri_fusion'](L) == sorted(L))
check('fusion ex', ns['tri_fusion']([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6])
tc = NS['i-tri-cpt']['tri_comptage']
check('comptage', tc([12, 5, 20, 5, 0]) == [0, 5, 5, 12, 20] and all(tc(L) == sorted(L) for L in ([R.randint(0, 20) for _ in range(30)] for _ in range(50))))
ns = NS['i-tri-sel']
for _ in range(300):
    L = [R.randint(0, 9) for _ in range(R.randint(1, 15))]
    check('rapide', ns['tri_rapide'](L) == sorted(L))
    k = R.randint(1, len(L)); check('kieme', ns['kieme'](L, k) == sorted(L)[k - 1])
check('kieme ex', ns['kieme']([7, 2, 9, 4, 4, 1], 3) == 4 and ns['kieme']([7, 2, 9, 4, 4, 1], 6) == 9)
# --- Graphes
d = NS['i-gr-bfs']['distances']
check('bfs', d([[1, 2], [0, 3], [0, 3], [1, 2, 4], [3], []], 0) == [0, 1, 1, 2, 3, -1])
ns = NS['i-gr-cycle']
def rnd_graph(n, p):
    E2 = set()
    while len(E2) < p:
        a, b = R.sample(range(n), 2); E2.add((min(a, b), max(a, b)))
    G = [[] for _ in range(n)]
    for a, b in E2: G[a].append(b); G[b].append(a)
    return G
def has_cycle_ref(G):
    n = len(G); parent = list(range(n))
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a in range(n):
        for b in G[a]:
            if a < b:
                ra, rb = find(a), find(b)
                if ra == rb: return True
                parent[ra] = rb
    return False
for _ in range(300):
    n = R.randint(1, 9); G = rnd_graph(n, R.randint(0, min(n * (n - 1) // 2, n + 1)))
    check('cycle', ns['a_un_cycle'](G) == ns['cycle_dfs'](G) == has_cycle_ref(G))
check('cycle ex', [ns['a_un_cycle']([[1], [0, 2], [1]]), ns['a_un_cycle']([[1, 2], [0, 2], [0, 1]]), ns['composantes']([[1], [0], []])] == [False, True, 2])
dj = NS['i-gr-dijk']['dijkstra']
G = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5)], [(4, 3)], []]
check('dijkstra', dj(G, 0) == [0, 3, 1, 4, 7])
def bellman(G, s):
    D = [math.inf] * len(G); D[s] = 0
    for _ in range(len(G)):
        for u in range(len(G)):
            for v, w in G[u]:
                if D[u] + w < D[v]: D[v] = D[u] + w
    return D
for _ in range(200):
    n = R.randint(1, 8); G2 = [[(R.randrange(n), R.randint(0, 9)) for _ in range(R.randint(0, 3))] for _ in range(n)]
    check('dijkstra rnd', dj(G2, 0) == bellman(G2, 0))
Gneg = [[(1, 2), (2, 3)], [], [(1, -2)]]
check('dijkstra neg', bellman(Gneg, 0)[1] == 1)
bp = NS['i-gr-bip']['biparti']
check('biparti ex', bp([[1, 3], [0, 2], [1, 3], [0, 2]]) == [0, 1, 0, 1] and bp([[1, 2], [0, 2], [0, 1]]) is None)
for _ in range(300):
    n = R.randint(1, 8); G2 = rnd_graph(n, R.randint(0, n * (n - 1) // 2))
    c = bp(G2)
    brute = any(all(col[a] != col[b] for a in range(n) for b in G2[a]) for col in itertools.product((0, 1), repeat=n))
    check('biparti rnd', (c is not None) == brute and (c is None or all(c[a] != c[b] for a in range(n) for b in G2[a])))
# --- Programmation dynamique
rd = NS['i-pd-monnaie']['rendu']
check('monnaie ex', rd([1, 4, 6], 8) == (2, [4, 4]) and rd([1, 4, 6], 12) == (2, [6, 6]))
def best(P, s):
    from functools import lru_cache
    @lru_cache(None)
    def m(x): return 0 if x == 0 else 1 + min(m(x - p) for p in P if p <= x)
    return m(s)
for _ in range(100):
    P = sorted({1} | {R.randint(2, 12) for _ in range(3)}); s = R.randint(0, 40); n2, pcs = rd(P, s)
    check('monnaie rnd', n2 == best(tuple(P), s) and sum(pcs) == s and len(pcs) == n2)
pl = NS['i-pd-plsc']['plsc']
res = pl('GATTA', 'TACTA')
def is_sub(s, t):
    it = iter(t); return all(c in it for c in s)
def lcs_brute(a, b):
    return max(len(s) for k in range(len(a) + 1) for s in (''.join(c) for c in itertools.combinations(a, k)) if is_sub(s, b))
check('plsc ex', res == (3, 'ATA') and lcs_brute('GATTA', 'TACTA') == 3 and is_sub('TTA', 'GATTA') and is_sub('TTA', 'TACTA'))
Lt = [[0] * 6 for _ in range(6)]
for i in range(1, 6):
    for j in range(1, 6):
        Lt[i][j] = Lt[i - 1][j - 1] + 1 if 'GATTA'[i - 1] == 'TACTA'[j - 1] else max(Lt[i - 1][j], Lt[i][j - 1])
check('plsc table', [r[1:] for r in Lt[1:]] == [[0, 0, 0, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 2, 2], [1, 1, 1, 2, 2], [1, 2, 2, 2, 3]])
print('PLSC GATTA/TACTA ->', res)
for _ in range(150):
    a = ''.join(R.choice('ACGT') for _ in range(R.randint(0, 7))); b = ''.join(R.choice('ACGT') for _ in range(R.randint(0, 7)))
    L, s = pl(a, b); check('plsc rnd', L == lcs_brute(a, b) == len(s) and is_sub(s, a) and is_sub(s, b))
mg = NS['i-pd-grille']['meilleur_gain']
check('grille ex', mg([[1, 2, 5], [3, 1, 1], [4, 0, 2]]) == 15)
check('grille C(38,19)', math.comb(38, 19) == 35345263800)
def brute_grille(T):
    n, m = len(T), len(T[0]); best_ = 0
    for pas in set(itertools.permutations('N' * (n - 1) + 'E' * (m - 1))):
        i, j, s = n - 1, 0, T[n - 1][0]
        for c in pas:
            if c == 'N': i -= 1
            else: j += 1
            s += T[i][j]
        best_ = max(best_, s)
    return best_
for _ in range(60):
    n, m = R.randint(1, 4), R.randint(1, 4); T = [[R.randint(0, 9) for _ in range(m)] for _ in range(n)]
    check('grille rnd', mg(T) == brute_grille(T))
ns = NS['i-pd-sac']
check('sac ex', ns['sac']([1, 3, 4, 5], [1, 4, 5, 7], 7) == ns['sac_1d']([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9)
for _ in range(150):
    n = R.randint(0, 7); p2 = [R.randint(1, 8) for _ in range(n)]; v2 = [R.randint(0, 9) for _ in range(n)]; C = R.randint(0, 20)
    br = max(sum(v2[i] for i in S) for k in range(n + 1) for S in itertools.combinations(range(n), k) if sum(p2[i] for i in S) <= C)
    check('sac rnd', ns['sac'](p2, v2, C) == ns['sac_1d'](p2, v2, C) == br)
L = [3, 1, 4, 2, 2]; check('partition', ns['sac_1d'](L, L, sum(L) // 2) == 6)
# --- Apprentissage
ns = NS['i-ia-knn']
X = [(1, 1), (2, 1), (1, 2), (5, 5), (6, 5), (5, 6)]; Y = ['A', 'A', 'A', 'B', 'B', 'B']
check('knn', ns['knn'](X, Y, (3, 3), 3) == 'A' and ns['knn'](X, Y, (3, 3), 6) == 'A')
cA = (4 / 3, 4 / 3); cB = (16 / 3, 16 / 3)
check('knn centres', abs(math.dist((3, 3), cA) - 2.357) < 1e-3 and abs(math.dist((3, 3), cB) - 3.300) < 1e-3)
it = NS['i-ia-kmeans']['iteration']
P6 = [(0, 0), (1, 0), (0, 1), (5, 5), (6, 5), (9, 9)]
C1 = it(P6, [(0, 0), (1, 0)])
check('kmeans centres', C1 == [(0.0, 0.5), (5.25, 4.75)])
def inertie(X, C, groupes):
    return sum((x[0] - C[g][0]) ** 2 + (x[1] - C[g][1]) ** 2 for x, g in zip(X, groupes))
g0 = [min(range(2), key=lambda k: (x[0] - c[0]) ** 2 + (x[1] - c[1]) ** 2) for x in P6 for c in [None]] if False else None
C0 = [(0, 0), (1, 0)]
grp = [min(range(2), key=lambda k: (x[0] - C0[k][0]) ** 2 + (x[1] - C0[k][1]) ** 2) for x in P6]
check('kmeans groupes', grp == [0, 1, 0, 1, 1, 1])
check('kmeans I', inertie(P6, C0, grp) == 237 and abs(inertie(P6, C1, grp) - 74) < 1e-9)
grp2 = [min(range(2), key=lambda k: (x[0] - C1[k][0]) ** 2 + (x[1] - C1[k][1]) ** 2) for x in P6]
check('kmeans (1,0) change', grp2[1] == 0)
# --- Jeux
g = NS['i-jeu-nim']['gagnante']
check('nim', [i for i in range(41) if i not in g(40)] == list(range(0, 41, 4)))
perd = [i for i in range(20) if i not in g(19, (1, 3, 4))]
print('Nim {1,3,4} perdantes ->', perd)
check('nim 134', perd[:6] == [0, 2, 7, 9, 14, 16])
mm = NS['i-jeu-minmax']['minmax']
check('minmax', mm([[3, 12, 8], [2, 4, 6], [14, 5, 2]]) == 3 and mm(7) == 7)
check('minmax b30', sum(30 ** k for k in range(5)) == 837931 == (30 ** 5 - 1) // 29)
# --- Flottants
pr = NS['i-flot']['proches']
check('flot', (0.1 + 0.2 == 0.3) is False and (0.5 + 0.25 == 0.75) and pr(0.1 + 0.2, 0.3) and not pr(1.0, 1.1) and pr(0.0, 1e-12))
n = 10 ** 6
s1 = 0.0
for k in range(1, n + 1): s1 += 1 / k
s2 = 0.0
for k in range(n, 0, -1): s2 += 1 / k
ex_ = math.fsum(1 / k for k in range(1, n + 1))
print('flottants : écart', s1 - s2, ' |croissant-exact|', abs(s1 - ex_), ' |décroissant-exact|', abs(s2 - ex_))
check('flot somme', abs(s2 - ex_) < abs(s1 - ex_) and 5e-13 < abs(s1 - s2) < 1e-12 and 5e-13 < abs(s1 - ex_) < 1e-12 and abs(s2 - ex_) < 1e-13 and abs(ex_ - 14.39272672286572) < 1e-13)
check('flot 0.3', repr(0.1 + 0.2) == '0.30000000000000004')

# ================= 3e et 4e séries =================
from collections import deque
import sqlite3
# --- RLE
ns = NS['i-py-rle']
check('rle ex', ns['compresser']('aaabccdddd') == [('a', 3), ('b', 1), ('c', 2), ('d', 4)] and ns['compresser']('') == [] and len(ns['compresser']('abab')) == 4)
for _ in range(300):
    t = ''.join(R.choice('ab') for _ in range(R.randint(0, 15)))
    check('rle aller-retour', ns['decompresser'](ns['compresser'](t)) == t)
# --- matrices
ns = NS['i-py-matrice']
check('matrice piège', ns['M'] == [[1, 0, 0]] * 3)
z = ns['zeros'](2, 3); z[0][0] = 1; check('zeros', z == [[1, 0, 0], [0, 0, 0]])
check('produit ex', ns['produit']([[1, 2], [3, 4]], [[0, 1], [1, 0]]) == [[2, 1], [4, 3]] and ns['transposee']([[1, 2, 3]]) == [[1], [2], [3]])
for _ in range(50):
    n_, p_, q_ = R.randint(1, 4), R.randint(1, 4), R.randint(1, 4)
    A = [[R.randint(-3, 3) for _ in range(p_)] for _ in range(n_)]; Bm = [[R.randint(-3, 3) for _ in range(q_)] for _ in range(p_)]
    P_ = ns['produit'](A, Bm)
    check('produit', all(P_[i][j] == sum(A[i][k] * Bm[k][j] for k in range(p_)) for i in range(n_) for j in range(q_)))
    check('transposée', ns['transposee'](ns['transposee'](A)) == A)
# --- Euclide
ns = NS['i-cx-euclide']
check('division', all(ns['division'](a, b) == divmod(a, b) for a in range(60) for b in range(1, 12)))
def pgcd_tours(a, b):
    k = 0
    while b != 0: a, b = b, a % b; k += 1
    return k
Fb = [0, 1]
while len(Fb) < 40: Fb.append(Fb[-1] + Fb[-2])
check('euclide fibo', all(pgcd_tours(Fb[k + 1], Fb[k]) == k - 1 for k in range(2, 38)) and pgcd_tours(89, 55) == 9 and Fb[10] == 55)
check('euclide pgcd', all(ns['pgcd'](a, b) == math.gcd(a, b) for a in range(1, 50) for b in range(1, 50)))
# --- tranche max
ns = NS['i-cx-maxsub']
check('maxsub ex', ns['tranche_max']([2, -5, 3, -1, 4, -6, 2]) == 6 and ns['tranche_max']([-3, -1, -2]) == -1)
for _ in range(300):
    L = [R.randint(-9, 9) for _ in range(R.randint(1, 10))]
    v = max(sum(L[i:j]) for i in range(len(L)) for j in range(i + 1, len(L) + 1))
    check('maxsub', ns['tranche_max'](L) == ns['tranche_max_quad'](L) == ns['tranche_max_naif'](L) == v)
cs = []; c_ = None
for x in [2, -5, 3, -1, 4, -6, 2]:
    c_ = x if c_ is None else max(x, c_ + x); cs.append(c_)
check('maxsub ci', cs == [2, -3, 3, 2, 6, 0, 2])
check('maxsub cubique', all(sum(j - i for i in range(n) for j in range(i + 1, n + 1)) == n * (n + 1) * (n + 2) // 6 for n in range(1, 30)))
# --- deux somme
ns = NS['i-cx-deuxsomme']
check('2somme ex', ns['deux_somme']([1, 3, 4, 6, 9], 10) == (0, 4) and ns['deux_somme']([1, 3, 4, 6, 9], 8) is None)
for _ in range(400):
    L = sorted(R.randint(0, 20) for _ in range(R.randint(0, 9))); s_ = R.randint(0, 40)
    exist = any(L[i] + L[j] == s_ for i in range(len(L)) for j in range(i + 1, len(L)))
    for f_ in ('deux_somme', 'deux_somme_dict'):
        r = ns[f_](L, s_)
        check('2somme ' + f_, (r is None and not exist) or (r is not None and r[0] < r[1] and L[r[0]] + L[r[1]] == s_))
# --- file avec deux piles
ns = NS['i-pile-file2']
F_ = ns['file_vide']()
for x in (1, 2, 3): ns['enfiler'](F_, x)
out = [ns['defiler'](F_)]; ns['enfiler'](F_, 4); out += [ns['defiler'](F_) for _ in range(3)]
check('file2 ex', out == [1, 2, 3, 4])
for _ in range(100):
    F_ = ns['file_vide'](); D_ = deque(); good = True
    for _ in range(60):
        if D_ and R.random() < 0.45: good &= ns['defiler'](F_) == D_.popleft()
        else: x = R.randint(0, 99); ns['enfiler'](F_, x); D_.append(x)
    check('file2', good)
# --- permutations
ns = NS['i-rec-perm']
check('perm ex', ns['permutations']([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
check('perm', all(sorted(map(tuple, ns['permutations'](list(range(n))))) == sorted(itertools.permutations(range(n))) for n in range(1, 7)))
def A_(n): return 1 if n <= 1 else 1 + n * A_(n - 1)
check('perm appels', all(A_(n) == sum(math.factorial(n) // math.factorial(k) for k in range(1, n + 1)) and A_(n) <= (math.e - 1) * math.factorial(n) for n in range(1, 15)) and A_(4) == 41 and A_(3) == 10)
cnt = [0]; orig = ns['permutations']
def compte(L):
    cnt[0] += 1
    if len(L) <= 1: return [L[:]]
    res = []
    for i in range(len(L)):
        for p in compte(L[:i] + L[i + 1:]): res.append([L[i]] + p)
    return res
compte([1, 2, 3, 4]); check('perm A(4) réel', cnt[0] == 41)
# --- epsilon
ns = NS['i-flot-eps']
check('epsilon', ns['epsilon']() == 2 ** -52 == sys.float_info.epsilon and ns['proches'](0.1 + 0.2, 0.3) and (1.0 + 1e-17) - 1.0 == 0.0 and 1e-17 + (1.0 - 1.0) == 1e-17 and 1.0 + 2 ** -53 == 1.0)
# --- bulles
ns = NS['i-tri-bulle']
def inv(L): return sum(L[i] > L[j] for i in range(len(L)) for j in range(i + 1, len(L)))
check('bulles ex', ns['tri_bulles']([3, 1, 2]) == 2 and ns['tri_bulles']([5, 4, 3, 2, 1]) == 10 and ns['tri_bulles']([1, 2, 3]) == 0)
for _ in range(300):
    L = [R.randint(0, 9) for _ in range(R.randint(0, 10))]; L0 = L[:]
    check('bulles', ns['tri_bulles'](L) == inv(L0) and L == sorted(L0))
moy = sum(inv(list(p)) for p in itertools.permutations(range(6))) / math.factorial(6)
check('bulles moyenne', moy == 6 * 5 / 4)
# --- inversions n log n
ti = NS['i-tri-inv']['tri_inv']
check('inv ex', ti([2, 4, 1, 3, 5]) == ([1, 2, 3, 4, 5], 3))
for _ in range(300):
    L = [R.randint(0, 9) for _ in range(R.randint(0, 14))]
    check('inv', ti(L) == (sorted(L), inv(L)))
# --- tri topologique
ns = NS['i-gr-topo']
check('topo ex', ns['tri_topologique'](ns['G']) == ['algebre', 'analyse', 'proba', 'edo'])
check('topo cycle', ns['tri_topologique']({'a': ['b'], 'b': ['c'], 'c': ['a'], 'd': ['a']}) is None)
for _ in range(200):
    n_ = R.randint(1, 7); G_ = {s: [t for t in range(n_) if t != s and R.random() < 0.3] for s in range(n_)}
    o = ns['tri_topologique'](G_)
    def cyc(G):
        col = {s: 0 for s in G}
        def dfs(s):
            col[s] = 1
            for t in G[s]:
                if col[t] == 1 or (col[t] == 0 and dfs(t)): return True
            col[s] = 2; return False
        return any(col[s] == 0 and dfs(s) for s in G)
    if cyc(G_): check('topo rnd cycle', o is None)
    else:
        pos = {s: k for k, s in enumerate(o)}
        check('topo rnd', len(o) == n_ and all(pos[s] < pos[t] for s in G_ for t in G_[s]))
# --- graphe inverse
ns = NS['i-gr-inverse']; d_ = ns['d']
check('inverse', ns['degre_max'](d_) == 2 and ns['graphe_inverse'](d_) == {0: [3], 1: [0], 2: [0], 3: [1, 2], 4: [2, 5], 5: []})
check('coloration', ns['coloration_valide'](d_, [0, 1, 1, 2, 0, 1]) and not ns['coloration_valide'](d_, [0, 1, 0, 2, 0, 1]) and ns['coloration_valide'](ns['graphe_inverse'](d_), [0, 1, 1, 2, 0, 1]))
# --- labyrinthe
ns = NS['i-gr-chemin']
check('laby ex', ns['chemin'](ns['lab'], (0, 0), (0, 3)) == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3)])
lab2 = ns['lab'][:]; lab2[2] = '#...'
check('laby none', ns['chemin'](lab2, (0, 0), (0, 3)) is None)
for _ in range(150):
    n_, p_ = R.randint(1, 6), R.randint(1, 6)
    lb = [''.join('#' if R.random() < 0.3 else '.' for _ in range(p_)) for _ in range(n_)]
    fr = [(i, j) for i in range(n_) for j in range(p_) if lb[i][j] == '.']
    if len(fr) < 2: continue
    a, b = R.choice(fr), R.choice(fr)
    dist = {a: 0}; Q = deque([a])
    while Q:
        c = Q.popleft()
        for v in ns['voisins'](lb, c):
            if v not in dist: dist[v] = dist[c] + 1; Q.append(v)
    r = ns['chemin'](lb, a, b)
    if b not in dist: check('laby rnd none', r is None)
    else:
        check('laby rnd', r[0] == a and r[-1] == b and len(r) == dist[b] + 1 and all(abs(r[k][0] - r[k + 1][0]) + abs(r[k][1] - r[k + 1][1]) == 1 and lb[r[k][0]][r[k][1]] == '.' for k in range(len(r) - 1)))
# --- Levenshtein
ns = NS['i-pd-levensh']
check('lev ex', [ns['distance']('kayak', 'yak'), ns['distance']('', 'abc'), ns['distance']('chien', 'niche'), ns['distance']('colle', 'collet')] == [2, 3, 4, 1])
for _ in range(300):
    a = ''.join(R.choice('abc') for _ in range(R.randint(0, 7))); b = ''.join(R.choice('abc') for _ in range(R.randint(0, 7)))
    dd = ns['distance'](a, b)
    check('lev', dd == ns['distance_lignes'](a, b) == ns['distance'](b, a) and abs(len(a) - len(b)) <= dd <= max(len(a), len(b)) and (dd == 0) == (a == b))
# --- escalier
ns = NS['i-pd-escalier']
check('escalier', all(ns['W_rec'](n) == ns['W_memo'](n) == ns['W_iter'](n) == ns['nb_facons'](n, [1, 2]) for n in range(0, 22)) and ns['nb_facons'](10, [1, 2]) == 89 and ns['nb_facons'](10, [1, 2, 3]) == 274 and ns['W_iter'](4) == 5 and [ns['W_iter'](n) for n in (1, 2, 3)] == [1, 2, 3])
calls = [0]
def Wc(n):
    calls[0] += 1
    return 1 if n <= 1 else Wc(n - 1) + Wc(n - 2)
# appels(n) = 2 W(n) - 1 ; pour n = 40, 2 F_41 - 1 > 3e8
check('escalier appels', all((calls.__setitem__(0, 0), Wc(n), calls[0])[2] == 2 * ns['W_iter'](n) - 1 for n in range(0, 18)) and 2 * ns['W_iter'](40) - 1 > 3e8)
# --- plus longue sous-suite croissante
ns = NS['i-pd-pls']
check('pls ex', ns['pssc']([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 4, 5, 9])
def est_ss(S, L):
    it = iter(L); return all(x in it for x in S)
for _ in range(200):
    L = [R.randint(0, 9) for _ in range(R.randint(0, 10))]
    best = max((len(c) for k in range(len(L) + 1) for c in itertools.combinations(L, k) if all(c[i] < c[i + 1] for i in range(len(c) - 1))), default=0)
    S = ns['pssc'](L)
    check('pls', len(S) == best and est_ss(S, L) and all(S[i] < S[i + 1] for i in range(len(S) - 1)))
# --- confusion
ns = NS['i-ia-confusion']
C_ = ns['confusion'](ns['vrais'], ns['predits'], ['chat', 'chien', 'lapin'])
pr_, rp_ = ns['precision_rappel'](C_, 1)
check('confusion', C_ == [[3, 1, 0], [1, 2, 0], [0, 1, 2]] and sum(C_[i][i] for i in range(3)) / 10 == 0.7 and pr_ == 0.5 and abs(rp_ - 2 / 3) < 1e-12)
check('confusion sommes', [sum(r) for r in C_] == [4, 3, 3] and [sum(C_[i][j] for i in range(3)) for j in range(3)] == [4, 4, 2])
# --- attracteur
ns = NS['i-jeu-attr']
check('attr ex', ns['attracteur'](ns['succ'], ns['joueur'], ns['F']) == {0, 1, 3, 4, 5} == ns['attracteur_lineaire'](ns['succ'], ns['joueur'], ns['F']))
def gagne0(succ, joueur, F, s0):
    # jeu d'accessibilité résolu par point fixe sur les couches A_k (définition, sans optimisation)
    A = set(F)
    while True:
        B = A | {s for s in succ if (joueur[s] == 0 and any(t in A for t in succ[s])) or (joueur[s] == 1 and all(t in A for t in succ[s]))}
        if B == A: return s0 in A
        A = B
for _ in range(300):
    n_ = R.randint(1, 8)
    sc = {s: sorted(set(R.choice(range(n_)) for _ in range(R.randint(1, 3)))) for s in range(n_)}
    jr = [R.randint(0, 1) for _ in range(n_)]; Fs = {s for s in range(n_) if R.random() < 0.25}
    a1, a2 = ns['attracteur'](sc, jr, Fs), ns['attracteur_lineaire'](sc, jr, Fs)
    check('attr rnd', a1 == a2 == {s for s in range(n_) if gagne0(sc, jr, Fs, s)})
# --- SQL
def sql_blocs(t):
    return re.findall(r"```sql[ \t]*\n(.*?)\n[ \t]*```", t, re.S)
db = sqlite3.connect(':memory:')
db.executescript("""
CREATE TABLE films(idf INTEGER PRIMARY KEY, titre TEXT, annee INTEGER);
CREATE TABLE locations(idc INTEGER, idf INTEGER REFERENCES films, debut TEXT, duree REAL, PRIMARY KEY(idc, idf, debut));
INSERT INTO films VALUES (1,'Les Intégrales',2012),(2,'Le Pivot de Gauss',2001),(3,'Taylor-Lagrange',2011),(4,'La Colle',1995);
INSERT INTO locations VALUES (10,1,'2026-01-03',1.0),(11,1,'2026-01-05',2.0),(10,2,'2026-02-01',3.5),(12,2,'2026-02-02',4.5),(11,3,'2026-02-10',1.5);
""")
q = sql_blocs(newlib.C['i-sql-films']['corrige'])
res = [db.execute(x).fetchall() for x in q]
check('sql films', len(q) == 4 and res[0] == [(4.5,)] and res[1] == [('Les Intégrales', 2012), ('Taylor-Lagrange', 2011), ('Le Pivot de Gauss', 2001)]
      and sorted(res[2]) == [(1, 'Les Intégrales', 1.5), (3, 'Taylor-Lagrange', 1.5)] and res[3] == [(4,)])
db2 = sqlite3.connect(':memory:')
db2.executescript("""
CREATE TABLE eleves(ide INTEGER PRIMARY KEY, nom TEXT, classe TEXT);
CREATE TABLE notes(ide INTEGER REFERENCES eleves, matiere TEXT, note REAL);
INSERT INTO eleves VALUES (1,'Amine','MP'),(2,'Lina','MP'),(3,'Yanis','PC'),(4,'Sara','MP'),(5,'Noé','PC');
INSERT INTO notes VALUES (1,'maths',14),(1,'physique',9),(1,'info',16),(2,'maths',12),(2,'physique',15),(2,'info',13),(3,'maths',8),(3,'physique',11),(4,'maths',17),(4,'physique',16),(4,'info',18);
""")
q = sql_blocs(newlib.C['i-sql-notes']['corrige'])
res = [db2.execute(x).fetchall() for x in q]
moys = {n: m for n, m in res[0]}
check('sql notes', len(q) == 5 and moys['Amine'] == 13 and abs(moys['Lina'] - 40 / 3) < 1e-9 and moys['Yanis'] == 9.5 and moys['Sara'] == 17 and 'Noé' not in moys
      and res[1] == [('Sara',)] and sorted(res[2]) == [('Lina',), ('Sara',)] and sorted(res[3]) == [('MP', 3), ('PC', 1)] and len(res[4]) == 4)
# tables de l'énoncé = données du test
for idx, txt in (('i-sql-films', 'Les Intégrales | 2012'), ('i-sql-notes', '| 4 | info | 18 |')):
    check('sql énoncé ' + idx, txt in next(e for e in newlib.E if e['id'] == idx)['enonce'])

print(f'{ok} vérifications réussies, {len(fails)} échec(s)', sorted(set(fails)))
sys.exit(1 if fails else 0)
