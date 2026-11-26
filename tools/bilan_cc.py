# Bilans — exercices de niveau CCINP (n-cc-*)
B = {}
def b(i, th, ast): B[i] = (th, ast)
b('n-cc-bertrand', [r"**Comparaison série-intégrale** pour $f$ continue, positive, décroissante."],
  [r"Penser à l'intégrale quand Riemann et d'Alembert échouent.", r"Primitives utiles : $\ln\ln t$ et $-\frac1{\ln t}$.", r"Vérifier d'abord la décroissance."])
b('n-cc-telescope', [r"**Télescopage.** $\sum_{n=1}^N(u_n-u_{n+1})=u_1-u_{N+1}$."],
  [r"Décomposer en différence de termes consécutifs d'une même suite.", r"Calculer la somme partielle avant de passer à la limite.", r"Contrôler avec les premiers termes."])
b('n-cc-se-somme', [r"**Exponentielle.** $e^x=\sum\frac{x^n}{n!}$, $R=+\infty$.", r"**Règle de d'Alembert** pour le rayon."],
  [r"Écrire $\frac{n}{n!}=\frac1{(n-1)!}$ et décaler l'indice.", r"Séparer le coefficient polynomial en morceaux connus.", r"Vérifier la somme en $x=0$."])
b('n-cc-se-ln', [r"**Développement usuel.** $\ln(1-u)=-\sum\frac{u^n}n$ pour $|u|<1$.", r"**Rayon et encadrement** des coefficients."],
  [r"Transformer $\ln$ d'un produit ou d'un quotient en somme de logarithmes.", r"$1+x+x^2=\frac{1-x^3}{1-x}$.", r"Vérifier sur un développement limité à l'ordre 3."])
b('n-cc-wallis', [r"**Intégration par parties généralisée** (limites du crochet).", r"**Comparaison** à $\frac1{x^2}$ en $+\infty$."],
  [r"Écrire $x^2=(1+x^2)-1$ pour faire apparaître $I_n$ et $I_{n+1}$.", r"Changement de variable $x=\tan\theta$ pour vérifier.", r"Relation de récurrence puis produit pour une formule close."])
b('n-cc-cvd', [r"**Convergence dominée.**", r"**Inégalité** $\ln(1+t)\le t$."],
  [r"Intervalle qui grandit : prolonger par $0$ avec une indicatrice.", r"Dominer $(1-\frac xn)^n$ par $e^{-x}$.", r"Confirmer par un calcul direct quand il existe."])
b('n-cc-param', [r"**Continuité et dérivation sous l'intégrale** avec domination.", r"**Domination locale** sur $[a,+\infty[$, $a>0$."],
  [r"Une domination globale peut échouer en $0$ : se placer sur $[a,+\infty[$.", r"Combiner $F''$ et $F$ pour simplifier l'intégrande.", r"Encadrer $F$ pour obtenir sa limite."])
b('n-cc-ed1', [r"**Équation d'ordre 1.** Homogène $Ce^{-A}$, puis variation de la constante."],
  [r"Normaliser en divisant par le coefficient de $y'$ (non nul).", r"Reconnaître $(\sqrt{1+x^2}\,y)'$ pour vérifier.", r"Primitive de $\frac1{\sqrt{1+x^2}}$ : $\ln(x+\sqrt{1+x^2})$."])
b('n-cc-ed2', [r"**Équation d'ordre 2 à coefficients constants** et équation caractéristique.", r"**Second membre $e^{mx}$** avec $m$ racine double : $Q$ de degré 2."],
  [r"Repérer la résonance avant de chercher la solution particulière.", r"Changement de fonction $y=ze^x$ : $z''=1$.", r"Appliquer les conditions initiales à la solution générale."])
b('n-cc-red3', [r"**Critère.** Annulateur scindé à racines simples ⇔ diagonalisable.", r"**Binôme de Newton** pour des matrices qui commutent."],
  [r"Écrire la matrice à l'aide de $J$ (tous coefficients égaux à 1).", r"$J^k=3^{k-1}J$ en dimension 3.", r"Vérifier $A^n$ pour $n=1$ et $n=2$."])
b('n-cc-matJ', [r"**Théorème du rang** et **trace = somme des valeurs propres**."],
  [r"Matrice de rang 1 : valeur propre $0$ de multiplicité $n-1$, l'autre égale à la trace.", r"$J^2=nJ$ donne un annulateur scindé simple.", r"Translater le spectre : $J+\lambda I$."])
b('n-cc-red2', [r"**Spectre unique** : diagonalisable ⇒ scalaire.", r"**Nilpotence** et binôme de Newton."],
  [r"Écrire $A=\lambda I+N$ avec $N$ nilpotente.", r"Polynôme caractéristique $2\times2$ : $X^2-\operatorname{tr}(A)X+\det A$.", r"Contrôler $A^n$ pour $n=1,2$."])
b('n-cc-gram', [r"**Gram-Schmidt.**", r"**Distance.** $d^2=\|x\|^2-\|p_F(x)\|^2$."],
  [r"Sur $[-1,1]$, l'imparité annule beaucoup de produits scalaires.", r"Projeter sur une base orthonormée, jamais sur une base quelconque.", r"Vérifier l'orthogonalité du résidu."])
b('n-cc-proj', [r"**Projection sur un hyperplan.** $p(x)=x-\langle x,n\rangle n$, $n$ unitaire.", r"**Symétrie.** $s=2p-\mathrm{Id}$."],
  [r"Matrice de $x\mapsto\langle x,n\rangle n$ : $n\,{}^tn$.", r"Distance à un hyperplan : $\frac{|\langle x,n\rangle|}{\|n\|}$.", r"Tester sur le vecteur normal et sur un vecteur du plan."])
b('n-cc-de6', [r"**Loi géométrique** : espérance, variance, survie.", r"**Absence de mémoire.**"],
  [r"Temps d'attente d'un premier succès : loi géométrique.", r"Somme sur les pairs : série géométrique de raison $q^2$.", r"Vérifier que pairs et impairs somment à 1."])
b('n-cc-poisson', [r"**Loi de Poisson** et **formule de transfert**."],
  [r"Faire apparaître $(k+1)!$ en multipliant et divisant par $\lambda$.", r"Parité : $\frac{1+(-1)^k}2$.", r"$E(X(X-1))$ est plus simple que $E(X^2)$."])
b('n-cc-binom', [r"**Fonction génératrice** et indépendance.", r"**Bienaymé-Tchebychev.**"],
  [r"La fonction génératrice caractérise la loi.", r"$p(1-p)\le\frac14$ pour une majoration indépendante de $p$.", r"Résoudre $\frac{1}{4n\varepsilon^2}\le\alpha$ pour la taille d'échantillon."])
b('n-cc-poly', [r"**Degré de $P(X+1)-P(X)$** : $\deg P-1$."],
  [r"Fixer le degré, puis identifier les coefficients.", r"Télescoper $\sum(P(k+1)-P(k))$.", r"Vérifier sur une petite valeur de $n$."])
b('n-cc-sdf', [r"**Convergence normale**, continuité et dérivation terme à terme.", r"**Double limite.**"],
  [r"Majorer indépendamment de $x$ : $\frac1{n^2+x^2}\le\frac1{n^2}$.", r"Inégalité $n^2+x^2\ge2n|x|$ pour la dérivée.", r"Comparaison série-intégrale pour l'équivalent en $+\infty$."])
b('n-cc-norme', [r"**Racines.** Un polynôme non nul de degré $\le n$ a au plus $n$ racines.", r"**Dimension finie** : formes linéaires continues."],
  [r"Pour une norme, seule la séparation pose souvent problème.", r"Contre-exemple : le polynôme qui s'annule aux points imposés.", r"En dimension finie, la continuité d'une linéaire est gratuite."])
