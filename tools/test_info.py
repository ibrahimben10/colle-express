"""Exécute tout le code Python des exercices d'informatique (énoncés et corrigés) et vérifie
les résultats annoncés dans les corrigés. À lancer après toute modification :
    python3 tools/test_info.py
"""
import re, sys, os, math, random, tempfile, itertools
sys.path.insert(0, os.path.dirname(__file__))
import newlib
import new_info_1, new_info_2  # noqa: F401  (remplissent newlib.E / newlib.C)

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

print(f'{ok} vérifications réussies, {len(fails)} échec(s)', sorted(set(fails)))
sys.exit(1 if fails else 0)
