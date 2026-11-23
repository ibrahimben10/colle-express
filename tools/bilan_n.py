# Bilans — exercices ajoutés (n-*)
from bilan_lib import *
B = {}

# ---------- physique CCINP ----------
B['n-p1-rc'] = ([LOIS_KIRCH,
  r"**Continuité.** La tension aux bornes d'un condensateur (et l'intensité dans une bobine) est continue.",
  r"**Énergie stockée.** Condensateur : $\frac12Cu^2$ ; bobine : $\frac12Li^2$."],
  [r"Premier ordre : $\tau=RC$, régime établi à $1\ \%$ près au bout de $\approx5\tau$.",
   r"Bilan d'énergie de la charge : générateur $CE^2$, condensateur $\frac12CE^2$, Joule $\frac12CE^2$, quelle que soit $R$.",
   r"Pour une énergie dissipée, intégrer $Ri^2$ ou, plus vite, faire la différence des autres énergies."])
B['n-p1-rlc'] = ([LOIS_KIRCH, OSC],
  [r"Mettre l'équation sous forme canonique pour lire $\omega_0$ et $Q$ directement.",
   r"Nombre d'oscillations visibles $\approx Q$ ; décrément logarithmique $\approx\frac\pi Q$.",
   r"Régime critique : $R_c=2\sqrt{L/C}$."])
B['n-p1-passebas'] = ([LOIS_KIRCH, FILTRE],
  [r"Pont diviseur de tension en complexes pour écrire $\underline H$ rapidement.",
   r"Signal composite : traiter chaque fréquence séparément (gain et déphasage), la composante continue passe avec $H(0)$.",
   r"Bien au-delà de $f_c$, un passe-bas du premier ordre est intégrateur."])
B['n-p1-passebande'] = ([LOIS_KIRCH, FILTRE, RESONANCE],
  [r"Diviser par $R$ pour faire apparaître la forme canonique $\frac1{1+jQ(x-1/x)}$.",
   r"Bande passante d'un passe-bande du second ordre : $\Delta\omega=\frac{\omega_0}Q$.",
   r"À la résonance, $L$ et $C$ se compensent : le circuit se réduit à $R$."])
B['n-p1-corde'] = ([DALEMBERT,
  r"**Célérité sur une corde.** $c=\sqrt{T/\mu}$ ; fréquences propres $f_n=n\frac c{2L}$."],
  [r"Modes propres d'une corde fixée aux deux bouts : $L=n\frac{\lambda_n}2$.",
   r"Changer la longueur vibrante ne change pas $c$ : $f\propto\frac1\ell$.",
   r"Les modes qui ont un nœud au point d'excitation ne sont pas excités."])
B['n-p1-ultrasons'] = ([FRESNEL],
  [r"Différence de marche de deux sources : $\delta\approx\frac{ax}D$ loin des sources, comme pour les trous d'Young.",
   r"Interfrange $i=\frac{\lambda D}a$.",
   r"Nombre de directions de maximum : $|p|\le\frac a\lambda$."])
B['n-p1-fente'] = ([DIFFRACTION],
  [r"Largeur de la tache centrale : $\ell\approx\frac{2\lambda D}a$, inversement proportionnelle à $a$.",
   r"Mesurer une petite largeur par diffraction : c'est une méthode de métrologie.",
   r"La diffraction n'est notable que si $a$ n'est pas très grand devant $\lambda$."])
B['n-p1-projecteur'] = ([CONJ],
  [r"Image réelle sur un écran éloigné : l'objet est juste au-delà du foyer objet.",
   r"Grandissement négatif : l'image est renversée, on place la diapositive à l'envers.",
   r"Une lentille convergente ne donne d'image réelle d'un objet réel que si $D\ge4f'$."])
B['n-p1-lunette'] = ([CONJ,
  r"**Système afocal.** Foyer image du premier élément confondu avec le foyer objet du second ; grossissement $G=-\frac{f_1'}{f_2'}$."],
  [r"Œil au repos face à un objet à l'infini : la lunette doit être afocale.",
   r"Le grossissement se lit sur un rayon passant par le foyer commun.",
   r"Le cercle oculaire est l'image de la monture de l'objectif par l'oculaire : on y place l'œil."])
B['n-p1-prisme'] = ([DESCARTES,
  r"**Formules du prisme.** $\sin i=n\sin r$, $\sin i'=n\sin r'$, $r+r'=A$, $D=i+i'-A$ ; au minimum de déviation, $n=\frac{\sin\frac{A+D_m}2}{\sin\frac A2}$."],
  [r"Établir $r+r'=A$ par la géométrie du triangle formé avec les normales.",
   r"Minimum de déviation : trajet symétrique, d'où une mesure précise de $n$.",
   r"Condition d'émergence : chaque angle intérieur reste inférieur à l'angle limite."])
B['n-p1-photo'] = ([PLANCK,
  r"**Effet photoélectrique (Einstein).** $E_{c,\max}=h\nu-W$ ; aucun électron n'est émis si $h\nu<W$, quelle que soit l'intensité."],
  [r"Utiliser $hc\approx1240\ \mathrm{eV\,nm}$ pour calculer vite en électronvolts.",
   r"Potentiel d'arrêt : $eU_0=E_{c,\max}$.",
   r"Le seuil en fréquence est la preuve de la quantification de la lumière."])
B['n-p1-debroglie'] = ([PLANCK,
  r"**Quantité de mouvement non relativiste.** $p=\sqrt{2mE_c}$ ; un électron accéléré sous $U$ a $E_c=eU$."],
  [r"Comparer $\lambda$ à la taille des obstacles : les effets ondulatoires apparaissent si $\lambda$ est du même ordre.",
   r"Électron sous 100 V : $\lambda\approx0{,}12$ nm, comme les distances interatomiques.",
   r"Vérifier $E_c\ll mc^2$ avant d'utiliser la formule non relativiste."])
B['n-p1-puits'] = ([SCHRO, HEIS,
  r"**Puits infini.** $\varphi_n=\sqrt{\frac2L}\sin\frac{n\pi x}L$, $E_n=\frac{n^2h^2}{8mL^2}$."],
  [r"Conditions aux limites $\varphi(0)=\varphi(L)=0$ : quantification de $k$.",
   r"Transition $1\to2$ : $\Delta E=3E_1$, et $\lambda\propto L^2$.",
   r"Estimer une énergie de confinement par Heisenberg : $E\sim\frac{\hbar^2}{2mL^2}$."])
B['n-p1-chute'] = ([PFD,
  r"**Équation du premier ordre.** $\dot v+\frac v\tau=g$ a pour solution $v=v_\ell(1-e^{-t/\tau})$, $v_\ell=g\tau$."],
  [r"Vitesse limite : la résultante des forces est nulle.",
   r"95 % de la vitesse limite au bout de $3\tau$.",
   r"Frottement quadratique : $k=\frac{mg}{v_\ell^2}$, sans résoudre l'équation."])
B['n-p1-geostat'] = ([KEPLER],
  [r"Satellite géostationnaire : orbite équatoriale circulaire de période égale au jour sidéral.",
   r"Troisième loi de Kepler pour le rayon : $r^3=\frac{\mathcal GMT^2}{4\pi^2}$.",
   r"Énergie d'une orbite circulaire : $E_m=-\frac{\mathcal GMm}{2r}$, d'où le coût d'un transfert."])
B['n-p1-pendule'] = ([ENERGIE, PFD,
  r"**Accélération normale.** En mouvement circulaire de rayon $L$ : $a_n=\frac{v^2}L$."],
  [r"Vitesse par l'énergie ; tension par le PFD projeté sur la normale.",
   r"Petites oscillations : $T_0=2\pi\sqrt{L/g}$, valable seulement pour de petits angles.",
   r"Tour complet avec un fil : il faut que le fil reste tendu au sommet ($v_h^2\ge gL$)."])
B['n-p1-rails'] = ([FARADAY, LAPLACE, LENZ],
  [r"Rails de Laplace : $e=-B\ell v$, force de Laplace $-\frac{B^2\ell^2}Rv$, freinage exponentiel.",
   r"Distance d'arrêt $v_0\tau$ par intégration de la vitesse.",
   r"Bilan de puissance : la puissance de Laplace compense exactement $ei$ (conversion électromécanique parfaite)."])
B['n-p1-transfo'] = ([FARADAY,
  r"**Transformateur parfait.** $\frac{u_2}{u_1}=\frac{N_2}{N_1}=m$, $\frac{i_1}{i_2}=m$ (conservation de la puissance) ; résistance ramenée au primaire : $\frac R{m^2}$."],
  [r"Même flux à travers chaque spire : rapport des tensions = rapport des nombres de spires.",
   r"Le côté basse tension porte le fort courant.",
   r"Pertes en ligne $rI^2=rP^2/U^2$ : transporter sous haute tension."])
B['n-p1-adiab'] = ([P1, GP, LAPLACE_GP],
  [r"Transformation rapide : adiabatique.",
   r"Lois de Laplace pour $T_2$ et $P_2$ ; travail par $\Delta U=C_v\Delta T$.",
   r"Une compression adiabatique coûte plus cher qu'une isotherme : le gaz s'échauffe."])
B['n-p1-frigo'] = ([P1, P2, CARNOT],
  [r"Efficacité d'un réfrigérateur : $e=\frac{Q_F}W\le\frac{T_F}{T_C-T_F}$.",
   r"Durée = énergie à extraire / puissance frigorifique $e\mathcal P$.",
   r"Entropie créée : $S_c=-\left(\frac{Q_F}{T_F}+\frac{Q_C}{T_C}\right)$ sur un cycle."])
B['n-p1-glacon'] = ([P1, P2, CHGT_ETAT],
  [r"Vérifier d'abord l'état final (tout fond ou non) en comparant les énergies disponibles.",
   r"Bilan enthalpique sur un chemin fictif découpé en étapes.",
   r"Entropie : $mc\ln\frac{T_f}{T_i}$ par étape, $\frac{m\ell}T$ pour la fusion ; système isolé donc $\Delta S=S_c>0$."])
B['n-p1-atmo'] = ([STATIQUE, GP],
  [r"Atmosphère isotherme : $P=P_0e^{-z/H}$ avec $H=\frac{RT}{Mg}\approx8$ km.",
   r"Sur une hauteur $h\ll H$, la pression d'un gaz est quasi uniforme.",
   r"Charge soulevée par un ballon : $(\rho_{\text{air}}-\rho_{\text{gaz}})V$."])
B['n-p1-bobine'] = ([FARADAY, LENZ],
  [r"Flux à travers $N$ spires : $N\,S\,B(t)$.",
   r"Puissance moyenne en sinusoïdal : $\frac{E_{\max}^2}{2r}$.",
   r"L'auto-induction est négligeable si $L\omega\ll r$."])

# ---------- physique Mines-Centrale / X ----------
B['n-p2-ailette'] = ([FOURIER, NEWTON_CC],
  [r"Bilan sur une tranche avec pertes latérales : $\theta''=\frac\theta{\delta^2}$.",
   r"Longueur caractéristique $\delta=\sqrt{\frac{\lambda a}{2h}}$ : une ailette plus longue que $3\delta$ est inutile.",
   r"Le flux évacué est celui qui entre à la base : $-\lambda S\theta'(0)$."])
B['n-p2-isolant'] = ([FOURIER, RTH, NEWTON_CC],
  [r"Associer en série résistance de conduction (logarithmique) et de convection.",
   r"Étudier $R(r_2)$ : minimum en $r_c=\lambda/h$.",
   r"Pour un fil fin, une gaine peut augmenter les pertes : c'est utile pour refroidir un câble."])
B['n-p2-peau'] = ([MAXWELL, ROTROT,
  r"**Loi d'Ohm locale.** $\vec j=\gamma\vec E$."],
  [r"Dans l'ARQS, combiner Maxwell-Faraday et Maxwell-Ampère pour obtenir une équation de diffusion.",
   r"Choisir la racine de $\underline k$ qui donne un champ borné.",
   r"$\delta=\sqrt{\frac2{\mu_0\gamma\omega}}$ : 9 mm à 50 Hz, quelques dizaines de µm en HF pour le cuivre."])
B['n-p2-bohr'] = ([HEIS,
  r"**Énergie potentielle coulombienne.** $E_p=-\frac{e^2}{4\pi\varepsilon_0r}$ pour l'électron et le proton."],
  [r"Écrire l'énergie totale en fonction de la taille $a$ : confinement en $\frac1{a^2}$, attraction en $-\frac1a$.",
   r"Minimiser : la compétition fixe la taille de l'atome.",
   r"Retenir $a_0\approx53$ pm et $E\approx-13{,}6$ eV."])
B['n-p2-marche'] = ([SCHRO,
  r"**Coefficients de réflexion et de transmission.** $R=|r|^2$, $T=\frac{k_2}{k_1}|t|^2$, avec $R+T=1$ (conservation du courant de probabilité)."],
  [r"Écrire les ondes incidente, réfléchie et transmise, puis raccorder $\varphi$ et $\varphi'$.",
   r"Pour $E<V_0$, remplacer $k_2$ par $i/\delta$ : réflexion totale mais onde évanescente.",
   r"Profondeur de pénétration $\delta=\frac\hbar{\sqrt{2m(V_0-E)}}$ : quelques dixièmes de nanomètre pour 1 eV."])
B['n-p2-doublet'] = ([FRESNEL,
  r"**Contraste.** $C=\frac{\mathcal E_{\max}-\mathcal E_{\min}}{\mathcal E_{\max}+\mathcal E_{\min}}$ ; pour un doublet d'intensités égales, $C=\left|\cos\frac{\pi\Delta\lambda\,\delta}{\lambda^2}\right|$."],
  [r"Raies incohérentes : sommer les éclairements, puis $\cos p+\cos q$.",
   r"Brouillages successifs pour $\Delta\delta=\frac{\lambda^2}{\Delta\lambda}$, soit $\Delta e=\frac{\lambda^2}{2\Delta\lambda}$ au Michelson.",
   r"Mesurer l'écart du doublet en comptant les brouillages."])
B['n-p2-reseau'] = ([RESEAU],
  [r"Ordre maximal : $|p|\le\frac a\lambda$.",
   r"Recouvrement de deux ordres : comparer $\sin\theta$ du rouge de l'ordre $p$ et du violet de l'ordre $p+1$.",
   r"Résolution : $|p|N\ge\frac\lambda{\Delta\lambda}$."])
B['n-p2-tige'] = ([INERTIE, PFD,
  r"**Puissance dans un référentiel tournant.** Dans le référentiel du laboratoire, la réaction de la tige travaille ; c'est le moteur qui fournit l'énergie."],
  [r"Référentiel tournant : force centrifuge selon la tige, Coriolis compensée par la réaction.",
   r"$\ddot r=\omega^2r$ : solution en $\cosh$, l'anneau s'éloigne exponentiellement.",
   r"Vérifier le bilan d'énergie dans le laboratoire : travail de la réaction $=\Delta E_c$."])
B['n-p2-resonance'] = ([RESONANCE],
  [r"Amplitude complexe, puis module ; résonance d'élongation en étudiant le dénominateur en fonction de $\omega^2$.",
   r"Résonance en vitesse : même forme qu'un passe-bande, bande passante $\frac{\omega_0}Q$.",
   r"Mesurer $Q$ expérimentalement par $Q=\frac{f_0}{\Delta f}$."])
B['n-p2-fourier'] = ([FILTRE,
  r"**Série de Fourier du créneau.** $\frac{4E}\pi\sum\frac{\sin((2k+1)\omega t)}{2k+1}$ : harmoniques impairs en $\frac1n$."],
  [r"Filtre loin au-dessus de sa coupure : comportement intégrateur.",
   r"Raisonnement temporel : pente $\frac E{RC}$ sur chaque demi-période, d'où un triangle.",
   r"Spectralement, chaque harmonique est divisé par $n$ : amplitudes en $\frac1{n^2}$."])
B['n-p2-coax'] = ([GAUSS, AMPERE, CURIE,
  r"**Énergie magnétique.** $W=\iiint\frac{B^2}{2\mu_0}\mathrm d\tau=\frac12LI^2$ ; capacité $C=\frac QU$."],
  [r"Gauss pour $\Gamma$, Ampère et énergie pour $\Lambda$.",
   r"$\Lambda\Gamma=\mu_0\varepsilon_0\varepsilon_r$ : la vitesse $c/\sqrt{\varepsilon_r}$ ne dépend pas de la géométrie.",
   r"Impédance caractéristique $\sqrt{\Lambda/\Gamma}$ : 50 Ω pour le câble standard."])
B['n-p2-serre'] = ([STEFAN,
  r"**Bilan radiatif.** En régime permanent, chaque couche émet autant qu'elle absorbe ; la Terre intercepte le flux solaire sur $\pi R^2$ et rayonne sur $4\pi R^2$."],
  [r"Facteur 4 entre surface d'interception et surface d'émission.",
   r"Modèle à une couche : bilan de la couche et bilan du sol, d'où $T_s=2^{1/4}T_a$.",
   r"Vu de l'espace, la planète rayonne toujours à 255 K."])
B['n-p2-dipole'] = ([
  r"**Dipôle électrostatique.** $V=\frac{p\cos\theta}{4\pi\varepsilon_0r^2}$, $E_r=\frac{2p\cos\theta}{4\pi\varepsilon_0r^3}$, $E_\theta=\frac{p\sin\theta}{4\pi\varepsilon_0r^3}$.",
  r"**Dipôle dans un champ extérieur.** $E_p=-\vec p\cdot\vec E$, couple $\vec p\wedge\vec E$ ; force $-\overrightarrow{\mathrm{grad}}E_p$."],
  [r"Comparer une énergie d'interaction à $k_BT$ pour savoir si l'agitation thermique l'emporte.",
   r"Un dipôle aligné est attiré vers les zones de champ intense.",
   r"Le champ d'un dipôle décroît en $\frac1{r^3}$."])
B['n-p2-plasma'] = ([MAXWELL, OPPH,
  r"**Pulsation plasma.** $\omega_p=\sqrt{\frac{ne^2}{m_e\varepsilon_0}}$ ; relation de dispersion $k^2c^2=\omega^2-\omega_p^2$."],
  [r"Conductivité complexe du plasma, puis relation de dispersion.",
   r"$\omega<\omega_p$ : onde évanescente, réflexion ; $\omega>\omega_p$ : propagation dispersive.",
   r"$v_\varphi v_g=c^2$ avec $v_g<c$ : l'énergie ne va pas plus vite que la lumière."])
B['n-p2-roulement'] = ([PFD, TMC, COULOMB],
  [r"Roulement sans glissement : $v=R\omega$, ce qui relie résultante et moment.",
   r"$\dot v=\frac{g\sin\alpha}{1+J/(mR^2)}$ : plus l'inertie est loin de l'axe, plus le cylindre est lent.",
   r"Toujours vérifier la condition de non-glissement $|T|\le fN$ à la fin."])
B['n-p2-beau'] = ([P1, LAPLACE_GP, CARNOT],
  [r"Cycle moteur : sens horaire dans le diagramme de Watt.",
   r"Rendement du cycle de Beau de Rochas : $\eta=1-a^{1-\gamma}$, ne dépend que du taux de compression.",
   r"Comparer au rendement de Carnot entre les températures extrêmes."])
B['n-p2-vdw'] = ([P1, P2,
  r"**Gaz de van der Waals.** $\left(P+\frac a{V_m^2}\right)(V_m-b)=RT$ ; $U_m=C_vT-\frac a{V_m}$."],
  [r"Détente de Joule-Gay-Lussac : $\Delta U=0$.",
   r"Le terme $-\frac a{V_m}$ refroidit le gaz qui se détend ; un gaz parfait ne change pas de température.",
   r"Entropie créée : système isolé donc $S_c=\Delta S>0$."])
B['n-p2-voile'] = ([PLANCK, KEPLER,
  r"**Pression de radiation.** Réflexion totale sous incidence normale : $P=\frac{2\varphi}c$ (absorption totale : $\frac\varphi c$)."],
  [r"Transfert de quantité de mouvement : $2\varepsilon/c$ par photon réfléchi.",
   r"Flux et gravité varient tous deux en $\frac1{r^2}$ : leur rapport est indépendant de la distance.",
   r"Comparer la masse surfacique à $\frac{2\varphi_0}{cg_0}\approx1{,}5\ \mathrm{g\,m^{-2}}$."])
B['n-p2-alternateur'] = ([FARADAY, LAPLACE, LENZ,
  r"**Valeur moyenne d'un produit.** $\langle\cos(\omega t)\cos(\omega t-\varphi)\rangle=\frac12\cos\varphi$."],
  [r"Fém d'une bobine tournante : $NBS\omega\sin\omega t$.",
   r"Le couple de Laplace moyen est résistant (Lenz) : le moteur doit le compenser.",
   r"Bilan : puissance mécanique fournie = puissance Joule moyenne."])
B['n-p2-diffusion'] = ([DIFF,
  r"**Loi de Fick.** $\vec j=-D\,\overrightarrow{\mathrm{grad}}\,n$ ; solution élémentaire gaussienne d'écart type $\sqrt{2Dt}$."],
  [r"Ordre de grandeur d'un temps de diffusion : $\tau\sim\frac{L^2}D$.",
   r"Diffusion efficace à petite échelle seulement ; à grande échelle, la convection domine.",
   r"Signature diffusive : distance parcourue en $\sqrt t$."])
B['n-p3-neutron'] = ([HEIS,
  r"**Principe de Pauli.** Deux fermions identiques ne peuvent occuper le même état : à densité $n$, chacun est confiné dans un volume $\sim1/n$."],
  [r"Écrire l'énergie totale en fonction de $R$ : confinement en $\frac1{R^2}$, gravitation en $-\frac1R$, puis minimiser.",
   r"En ordres de grandeur, oublier les facteurs numériques mais garder les puissances de $N$.",
   r"$R\propto M^{-1/3}$ : les objets dégénérés rétrécissent quand leur masse augmente."])

# ---------- chimie ----------
B['n-c-fer'] = ([KLECH],
  [r"Ions des métaux de transition : on retire d'abord les électrons $4s$.",
   r"Sous-couche $d$ à moitié pleine ($d^5$) ou pleine ($d^{10}$) : configurations particulièrement stables.",
   r"Position dans la classification : période = $n_{\max}$, bloc = dernière sous-couche remplie."])
B['n-c-vsepr'] = ([VSEPR,
  r"**Polarité.** Une molécule est polaire si la somme vectorielle des moments dipolaires de liaison est non nulle."],
  [r"Compter les électrons de valence, écrire Lewis, puis déterminer $\mathrm{AX}_m\mathrm E_n$.",
   r"Symétrie élevée (linéaire, triangle plan, tétraèdre régulier) : moments qui se compensent.",
   r"Les doublets non liants referment les angles de liaison."])
B['n-c-h2o2'] = ([ORDRE1, GP],
  [r"Tester l'ordre 1 en traçant $\ln c$ en fonction de $t$.",
   r"Lier la quantité de gaz formé à l'avancement grâce à la stœchiométrie.",
   r"Volume de gaz par $PV=nRT$, en unités SI."])
B['n-c-arrhenius'] = ([ARRH],
  [r"Deux constantes à deux températures donnent $E_a$ : $\ln\frac{k_2}{k_1}=\frac{E_a}R\left(\frac1{T_1}-\frac1{T_2}\right)$.",
   r"Toujours convertir les températures en kelvins.",
   r"Ordre de grandeur : vitesse doublée tous les 10 °C pour $E_a\approx50$ kJ/mol."])
B['n-c-vitinit'] = ([VIT_INIT, AEQS],
  [r"Comparer deux expériences qui ne diffèrent que par une concentration.",
   r"Une loi de vitesse conforme à la stœchiométrie ne prouve pas que la réaction est élémentaire.",
   r"Dégénérescence de l'ordre pour isoler un seul ordre partiel."])
B['n-c-ethanoique'] = ([KA, REAC_PREP],
  [r"pH d'un acide faible : $\frac12(\mathrm pK_a-\log c)$, puis vérifier la faible dissociation.",
   r"Demi-équivalence : $\mathrm{pH}=\mathrm pK_a$.",
   r"Choisir un indicateur dont la zone de virage contient le pH à l'équivalence."])
B['n-c-tampon'] = ([KA],
  [r"Relation de Henderson pour un mélange acide/base conjuguée.",
   r"Un ajout d'acide fort réagit totalement avec la base du tampon.",
   r"Pouvoir tampon maximal à $\mathrm{pH}=\mathrm pK_a$ (mélange équimolaire)."])
B['n-c-agcl'] = ([KS],
  [r"Solubilité dans l'eau pure : $K_s=s^2$ pour un sel 1:1.",
   r"Effet d'ion commun : la solubilité chute fortement.",
   r"Test de précipitation : calculer $Q$ juste après le mélange (dilution) et le comparer à $K_s$."])
B['n-c-mgoh2'] = ([KS, REAC_PREP],
  [r"$K_s=4s^3$ pour un hydroxyde $\mathrm{M(OH)_2}$ dans l'eau pure.",
   r"Début de précipitation : $[\mathrm M^{2+}][\mathrm{HO^-}]^2=K_s$.",
   r"$\log s$ affine en pH : pente $-2$ pour $\mathrm M(\mathrm{OH})_2$."])
B['n-c-nacl'] = ([CFC, MASSE_VOL,
  r"**Structure NaCl.** Anions en CFC, cations dans tous les sites octaédriques : coordinence [6,6], contact cation-anion selon l'arête ($r_++r_-=\frac a2$), stable pour $0{,}414\le\frac{r_+}{r_-}\le0{,}732$."],
  [r"Compter les ions avec les poids de position (sommet, face, arête, centre).",
   r"Contact cation-anion selon l'arête ; vérifier que les anions ne se touchent pas.",
   r"Le rapport des rayons explique le choix entre les structures NaCl et CsCl."])
B['n-c-daniell'] = ([NERNST, K_REDOX, PILE],
  [r"Le pôle + est l'électrode de plus haut potentiel (Nernst avec les concentrations réelles).",
   r"$K$ énorme : la pile fonctionne jusqu'à épuisement d'un réactif.",
   r"Capacité : $Q=nF$, à convertir en A·h (diviser par 3600)."])
B['n-c-permanganate'] = ([K_REDOX, NERNST],
  [r"Équilibrer les demi-équations en milieu acide ($\mathrm{H^+}$, $\mathrm{H_2O}$), puis combiner pour échanger le même nombre d'électrons.",
   r"Relation à l'équivalence : $n(\mathrm{Fe^{2+}})=5\,n(\mathrm{MnO_4^-})$.",
   r"Le permanganate, violet, est son propre indicateur de fin de dosage."])
B['n-c-conducti'] = ([KOHL],
  [r"Avant l'équivalence, on remplace un ion par un autre : la pente dépend de la différence des $\lambda$.",
   r"Après l'équivalence, on ajoute des ions : la conductivité croît.",
   r"$\mathrm{H_3O^+}$ et $\mathrm{HO^-}$ conduisent bien mieux que les autres ions (mécanisme de Grotthuss)."])
B['n-c-epH'] = ([NERNST, KS, EPH],
  [r"Commencer par les pH de précipitation à la concentration de tracé.",
   r"Exprimer $[\mathrm{Fe^{3+}}]$ par $K_s$ dans la formule de Nernst pour les frontières avec un hydroxyde.",
   r"Vérifier la continuité des frontières aux points anguleux."])
B['n-c-flamme'] = ([HESS, P1],
  [r"Inventaire complet des produits, y compris le diazote spectateur.",
   r"Température de flamme : réaction à 298 K, puis échauffement des produits, avec $\Delta H=0$.",
   r"L'azote de l'air absorbe une grande part de l'énergie."])
B['n-c-ellingham'] = ([ELLINGHAM, GIBBS],
  [r"Pente des droites d'Ellingham : signe donné par la variation du nombre de moles de gaz.",
   r"Réduction possible quand la droite du réducteur passe sous celle du métal.",
   r"Changement d'état du métal : point anguleux, pente qui augmente."])
B['n-c-electrolyse'] = ([IE,
  r"**Loi de Faraday (électrolyse).** La charge $Q=nF$ correspond à $n$ moles d'électrons ; une mole de $\mathrm{H_2}$ demande $2F$."],
  [r"Tension minimale = différence des potentiels thermodynamiques ; tension réelle = + surtensions + chute ohmique.",
   r"Énergie électrique par mole : $W=2FU$.",
   r"Rendement énergétique : énergie récupérable / énergie électrique consommée."])
B['n-c-aeqs'] = ([AEQS, ARRH, VANTHOFF],
  [r"Pré-équilibre rapide suivi d'une étape lente : $v=k_2K[\cdots]$.",
   r"L'AEQS redonne le pré-équilibre si l'intermédiaire revient en arrière bien plus vite qu'il ne réagit.",
   r"Énergie d'activation apparente $E_{a,2}+\Delta_rH_1^\circ$, éventuellement négative."])

# ---------- mathématiques ----------
B['n-m-max'] = ([QUEUE,
  r"**Loi du maximum.** Si les $X_i$ sont indépendantes, $P(\max X_i\le k)=\prod P(X_i\le k)$."],
  [r"Loi d'un maximum : passer par la fonction de répartition $P(M\le k)$, puis différencier.",
   r"Espérance d'une variable entière : $E(M)=\sum_{i\ge0}P(M>i)$.",
   r"Écrire $M(M-1)$ comme somme d'indicatrices pour le moment d'ordre 2."])
B['n-m-euler'] = ([EDL2,
  r"**Équations d'Euler.** Pour $t^2y''+aty'+by=0$, chercher $t^r$ : $r(r-1)+ar+b=0$."],
  [r"Chercher des solutions de la forme $t^r$.",
   r"Reconnaître une dérivée exacte : $t^2y''+4ty'+2y=(t^2y)''$.",
   r"Avec second membre, la même astuce donne la solution générale en deux intégrations."])
B['n-m-abb'] = ([SPECTRAL,
  r"**Produit scalaire associé à une matrice.** $(X,Y)\mapsto X^{\top}AY$ est un produit scalaire ssi $A$ est symétrique à valeurs propres strictement positives."],
  [r"Matrice « $a$ sur la diagonale, $b$ ailleurs » : $A=(a-b)I+bJ$ avec $J$ de rang 1.",
   r"La trace donne la valeur propre manquante.",
   r"Base orthonormée : orthonormaliser dans chaque sous-espace propre."])
B['n-m-antisym'] = ([
  r"**Endomorphisme antisymétrique.** $\langle u(x),x\rangle=0$ pour tout $x$ ssi $\langle u(y),z\rangle=-\langle y,u(z)\rangle$ ; alors $\ker u=(\mathrm{Im}\,u)^\perp$.",
  r"**Polynôme réel de degré impair.** Il a au moins une racine réelle (TVI)."],
  [r"Polariser l'identité $\langle u(x),x\rangle=0$.",
   r"Restreindre à $\mathrm{Im}\,u$ pour obtenir un automorphisme sans valeur propre réelle.",
   r"« Pas de valeur propre réelle » implique « dimension paire »."])
B['n-m-phiX1'] = ([DIAG_DIM,
  r"**Formule de Taylor pour les polynômes.** $\left((X-a)^k\right)_{0\le k\le n}$ est une base de $\mathbb R_n[X]$."],
  [r"Choisir la base adaptée à l'opérateur : ici les $(X-1)^k$.",
   r"$n+1$ valeurs propres distinctes en dimension $n+1$ : diagonalisable.",
   r"Réflexe : $P\mapsto(X-a)P'$ « compte le degré en $(X-a)$ »."])
B['n-m-ln1t'] = ([DSE, CSSA, CV_UNIF_INT],
  [r"Développer en série entière, puis intégrer terme à terme sur un segment.",
   r"Justifier par la convergence uniforme (reste d'une série alternée majoré uniformément).",
   r"$\sum\frac{(-1)^{n+1}}{n^2}=\frac12\zeta(2)$ en séparant termes pairs et impairs."])
B['n-m-wallis'] = ([CSSA,
  r"**Formule de Wallis.** $\prod_{k\ge1}\frac{4k^2}{4k^2-1}=\frac\pi2$."],
  [r"Une série convergente a pour somme la limite de $S_{2N}$ : on peut regrouper les termes deux à deux.",
   r"Somme de logarithmes = logarithme d'un produit.",
   r"Reconnaître le produit de Wallis."])
B['n-m-arctanx2'] = ([IPP, RIEMANN,
  r"**Décomposition en éléments simples.** $\frac1{x(1+x^2)}=\frac1x-\frac x{1+x^2}$."],
  [r"Existence par majoration avant tout calcul.",
   r"Intégration par parties sur $[1,A]$ puis $A\to+\infty$.",
   r"Regrouper les logarithmes avant de passer à la limite pour éviter $\infty-\infty$."])
B['n-m-symk'] = ([SPECTRAL],
  [r"Matrice symétrique réelle : raisonner sur les valeurs propres, réelles.",
   r"$\lambda^k=1$ avec $\lambda$ réel : $\lambda=\pm1$.",
   r"Contre-exemple non symétrique : rotation d'angle $\frac{2\pi}3$."])
B['n-m-chth'] = ([COMP,
  r"**Équivalents usuels.** En 0 : $\mathrm{ch}\,x-1\sim\frac{x^2}2$, $\mathrm{th}\,x\sim x$, $e^u-1\sim u$."],
  [r"Forme $u^v$ : passer à l'exponentielle $e^{v\ln u}$.",
   r"Équivalent de $u_n-\ell$ puis comparaison avec $\frac1n$.",
   r"Les termes de signe constant à partir d'un rang autorisent la comparaison par équivalents."])
B['n-m-extrema'] = ([CRITIQUE, COMPACT],
  [r"Additionner les équations des points critiques pour les simplifier.",
   r"Fonction coercive : le minimum global est atteint en un point critique.",
   r"Pour exclure un extremum, trouver deux directions où $f$ prend des signes opposés."])
B['n-m-In'] = ([CHGT, RAYON, TERM_INT],
  [r"Changement de variable pour simplifier l'intégrande, puis relation de récurrence.",
   r"Suite décroissante + relation $I_n+I_{n-1}=\frac1n$ : encadrer $2I_n$ pour obtenir l'équivalent.",
   r"Somme de la série : intervertir série et intégrale, puis éléments simples."])
B['n-m-double'] = ([TONELLI,
  r"**Représentation intégrale.** $\frac1{a}=\int_0^1x^{a-1}\,\mathrm dx$ pour $a>0$."],
  [r"Remplacer $\frac1{m+n+2}$ par une intégrale pour séparer les variables.",
   r"Termes positifs : interversion libre (Tonelli).",
   r"$\int_0^1y^a\ln^2y\,\mathrm dy=\frac2{(a+1)^3}$."])
B['n-m-blocs'] = ([DIAG_POLY,
  r"**Polynôme d'une matrice triangulaire par blocs.** Si $AB=BA$ : $P\begin{pmatrix}A&B\\0&A\end{pmatrix}=\begin{pmatrix}P(A)&P'(A)B\\0&P(A)\end{pmatrix}$."],
  [r"Calculer $M^k$ par récurrence, puis étendre par linéarité à $P(M)$.",
   r"Un polynôme annulateur scindé simple de $M$ annule $A$ et vérifie $P'(A)B=0$.",
   r"$P'(A)$ est inversible car les valeurs propres de $A$ sont des racines simples de $P$."])
B['n-m-pieces'] = ([GEOM],
  [r"Dénombrer les issues favorables parmi $2^n$ issues équiprobables.",
   r"Répétition jusqu'au premier succès : loi géométrique.",
   r"Vérifier les cas limites ($n=2$) qui cassent le dénombrement."])
B['n-m-Jn'] = ([IPP, RIEMANN,
  r"**Produit et logarithme.** $\ln\prod(1+a_k)=\sum\ln(1+a_k)$ ; avec $\sum_{k\le n}\frac1k=\ln n+\gamma+o(1)$."],
  [r"Relation de récurrence par parties en écrivant $\frac{x^3}{(1+x^3)^{n+2}}=\frac1{(1+x^3)^{n+1}}-\frac1{(1+x^3)^{n+2}}$.",
   r"Pour un équivalent d'un produit, passer au logarithme et développer.",
   r"$J_0$ par éléments simples : $\frac{2\pi}{3\sqrt3}$."])
B['n-m-sintx'] = ([DOM_DERIV],
  [r"Dominer la dérivée partielle indépendamment de $x$ : $\left|\frac{\cos(tx)}{1+t^2}\right|\le\frac1{1+t^2}$.",
   r"Intégrer $F'$ avec $F(0)=0$ et utiliser la parité.",
   r"Vérifier la régularité réelle : ici $F'$ a un point anguleux en 0."])
B['n-m-arctantx'] = ([DOM_DERIV, IPP],
  [r"Dériver sous l'intégrale fait disparaître l'arctangente.",
   r"Éléments simples en $t^2$ pour calculer $F'(x)$.",
   r"Relier l'intégrale demandée à $F(1)$ par une intégration par parties."])
B['n-m-geodiff'] = ([GEOM, SOMME_IND],
  [r"Loi d'une différence : sommer $P(X_2=k)P(X_1=k+n)$ (série géométrique de raison $q^2$).",
   r"Symétrie entre $X_1$ et $X_2$ pour les valeurs négatives.",
   r"$Y^2=(X_1-X_2)^2$ : la variance s'obtient sans connaître $E(Y^2)$ directement."])
B['n-m-kerf2'] = ([RANG],
  [r"Appliquer le théorème du rang à la restriction de $f$ à $\ker f^2$.",
   r"$f(\ker f^2)\subset\ker f$ : inclusion + égalité des dimensions.",
   r"$\ker f\subset\mathrm{Im}\,f$ s'utilise en écrivant $y=f(x)$."])
