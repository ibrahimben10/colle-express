# Bilans — physique et chimie (exercices d'origine)
from bilan_lib import *
B = {}

# ----- chimie -----
B['c-thermo-1'] = ([GIBBS,
  r"**Constante d'équilibre avec un seul gaz.** Les solides purs ont une activité 1 : $K^\circ=\frac{P_{\mathrm{O_2}}}{P^\circ}$ (à la puissance de son coefficient)."],
  [r"Deux mesures de $K$ à deux températures donnent $\Delta_rH^\circ$ et $\Delta_rS^\circ$ (approximation d'Ellingham) : résoudre un système linéaire.",
   r"Activité 1 pour les solides : seule la pression du gaz intervient.",
   r"Vérifier les signes : une décomposition qui libère un gaz a $\Delta_rS^\circ>0$."])
B['c-sol-2'] = ([KS, KA, REAC_PREP],
  [r"En milieu acide, écrire la réaction prépondérante de dissolution avec les ions $\mathrm{H^+}$.",
   r"Combiner les constantes : $K=\frac{K_s}{K_{A1}K_{A2}}$.",
   r"Vérifier a posteriori que l'espèce supposée majoritaire ($\mathrm{H_2S}$) l'est bien au pH considéré."])
B['c-redox-3'] = ([K_REDOX, NERNST,
  r"**Potentiel d'un couple combiné.** Les $\Delta_rG^\circ=-nFE^\circ$ s'additionnent, pas les potentiels : $n_3E_3^\circ=n_1E_1^\circ+n_2E_2^\circ$."],
  [r"Pour combiner des couples redox, passer par les enthalpies libres $-nFE^\circ$.",
   r"Une médiamutation est favorable quand l'oxydant le plus fort réagit sur le réducteur le plus fort.",
   r"Équilibrer en électrons avant de calculer $\log K$."])
B['c-thermo-4'] = ([GIBBS,
  r"**Variance et coexistence de phases.** Si un équilibre ne fait intervenir qu'un gaz, sa pression est imposée par $K^\circ(T)$ tant que les solides coexistent (palier)."],
  [r"Tracer $P$ en fonction de $V$ : paliers à la pression d'équilibre de chaque carbonate, hyperboles $PV=nRT$ ailleurs.",
   r"Rupture d'équilibre : quand un solide disparaît, la pression n'est plus imposée.",
   r"Le carbonate le moins stable se décompose en premier quand on détend."])
B['c-thermo-6'] = ([GIBBS,
  r"**Quotient de réaction.** En phase gazeuse : $Q=\prod\left(\frac{P_i}{P^\circ}\right)^{\nu_i}$ avec $P_i=x_iP$ ; comparer $Q$ à $K^\circ$ donne le sens d'évolution."],
  [r"Ajout d'un constituant à $T$ et $P$ fixées : exprimer $Q$ en fonction des quantités et de $n_{\text{tot}}$, puis dériver.",
   r"Ajouter un réactif ne favorise pas toujours le sens direct : cela dépend de sa fraction molaire.",
   r"Raisonner sur le signe de $\frac{\partial\ln Q}{\partial n_i}$."])
B['c-electro-3'] = ([IE,
  r"**Loi de Tafel.** Loin de l'équilibre, $\eta=a+b\log|j|$ : courbes $E(\log|j|)$ affines."],
  [r"Au potentiel de corrosion, courant global nul : $j_a=|j_c|$.",
   r"Tracer en coordonnées $(\log|j|,E)$ : le point de corrosion est l'intersection des deux droites de Tafel.",
   r"La vitesse de corrosion est proportionnelle à $j_{\text{cor}}$ (loi de Faraday)."])
B['c-electro-5'] = ([PILE, IE],
  [r"Point de fonctionnement d'une pile : même intensité à l'anode et à la cathode, et loi d'Ohm dans le circuit.",
   r"Les surtensions linéarisées agissent comme des résistances internes.",
   r"Le courant maximal est limité par la somme $R+\alpha_A+|\alpha_C|$."])
B['c-cin-2'] = ([ORDRE1],
  [r"Relier une grandeur mesurée (volume de gaz) à l'avancement : $V(t)=V_\infty(1-e^{-kt})$.",
   r"Linéariser : $\ln\frac{V_\infty}{V_\infty-V}=kt$.",
   r"Le temps de demi-réaction d'ordre 1 ne dépend pas de la concentration initiale."])
B['c-cristallo-1'] = ([MASSE_VOL,
  r"**Hexagonal compact et cubique centré.** HC idéal : $c=a\sqrt{8/3}$, $a=2r$, compacité 0,74 ; CC : 2 atomes par maille, contact selon la grande diagonale ($4r=a\sqrt3$), compacité 0,68."],
  [r"Identifier la direction de contact avant tout calcul de rayon.",
   r"Compter les atomes par maille avec les poids (sommet 1/8, face 1/2, arête 1/4).",
   r"Comparer les compacités pour discuter de la stabilité des formes."])
B['c-cristallo-2'] = ([CFC, MASSE_VOL,
  r"**Habitabilité.** Site octaédrique : $r_O=\frac a2-R$ ; site tétraédrique : $r_T=\frac{a\sqrt3}4-R$."],
  [r"Situer les sites interstitiels : octaédriques au centre et aux milieux des arêtes, tétraédriques aux centres des 8 petits cubes.",
   r"Comparer la taille de l'atome inséré à l'habitabilité du site.",
   r"Formule de l'hydrure : nombre de sites occupés par maille / 4 atomes métalliques."])
B['p-chim-ccs6'] = ([P1,
  r"**Enthalpie de réaction.** Transformation isobare adiabatique : $\Delta H=\xi\,\Delta_rH+C_{\text{tot}}\Delta T=0$."],
  [r"Repérer le réactif limitant avant l'équivalence ($\xi=c_0V_s$).",
   r"Chemin fictif : réaction à température initiale puis échauffement du mélange.",
   r"Ne pas oublier la capacité thermique du calorimètre (valeur en eau)."])

# ----- électromagnétisme -----
B['p-em-1'] = ([GAUSS, CURIE],
  [r"Commencer par les symétries et invariances : $\vec E=E(r)\vec u_r$.",
   r"Choisir une surface de Gauss cylindrique coaxiale ; les bases ne contribuent pas au flux.",
   r"Une distribution globalement neutre crée un champ nul à l'extérieur."])
B['p-em-2'] = ([GAUSS,
  r"**Énergie électrostatique.** $W=\iiint\frac{\varepsilon_0E^2}2\,\mathrm d\tau$ sur tout l'espace."],
  [r"Calculer le champ partout (intérieur, extérieur) par Gauss sphérique.",
   r"Intégrer la densité d'énergie en coquilles sphériques $4\pi r^2\,\mathrm dr$.",
   r"Vérifier l'homogénéité : $W\propto\frac{e^2}{4\pi\varepsilon_0R}$."])
B['p-em-3'] = ([AMPERE, CURIE],
  [r"Symétries : tout plan contenant l'axe est plan de symétrie, donc $\vec B=B(r)\vec u_\theta$.",
   r"Contour d'Ampère circulaire coaxial ; courant enlacé proportionnel à $r^2$ à l'intérieur.",
   r"Continuité de $B$ en $r=b$ (pas de courant surfacique) : bonne vérification."])
B['p-max-1'] = ([MAXWELL,
  r"**Équation de Laplace.** En l'absence de charges, $\Delta V=0$ ; en cylindriques, pour $V(r)$ : $\frac1r\frac{\mathrm d}{\mathrm dr}\left(r\frac{\mathrm dV}{\mathrm dr}\right)=0$."],
  [r"Réduire à une seule variable par symétrie, puis intégrer deux fois.",
   r"Fixer les constantes avec les potentiels imposés sur les conducteurs.",
   r"$\vec E=-\overrightarrow{\mathrm{grad}}\,V$ : vérifier le sens du champ."])
B['p-max-2'] = ([MAXWELL,
  r"**ARQS.** Si la taille $L$ du système vérifie $L\ll cT$, le courant de déplacement est négligeable et $\overrightarrow{\mathrm{rot}}\vec B\approx\mu_0\vec j$."],
  [r"Comparer les termes par ordres de grandeur : $\partial_t\to\frac1T$, $\overrightarrow{\mathrm{rot}}\to\frac1L$.",
   r"Le rapport des deux termes de Maxwell-Ampère est $(L/cT)^2$.",
   r"Critère pratique : durée de propagation négligeable devant la période."])
B['p-max-3'] = ([MAXWELL,
  r"**Modèle de Drude.** $m\frac{\mathrm d\vec v}{\mathrm dt}=q(\vec E+\vec v\wedge\vec B)-\frac m\tau\vec v$ ; en régime permanent sans champ magnétique : $\vec j=\gamma\vec E$, $\gamma=\frac{nq^2\tau}m$."],
  [r"Géométrie radiale : la résistance s'obtient en intégrant $\frac{\mathrm dr}{\gamma\,2\pi ra}$.",
   r"Avec $\vec B$, la vitesse dévie d'un angle de Hall $\tan\theta_H=\frac{e\tau B}m$ : la magnétorésistance apparaît.",
   r"Comparer avec une barre de Hall, où le champ de Hall compense la déviation."])
B['p-ind-2'] = ([FARADAY, LAPLACE, LENZ],
  [r"Orienter le circuit une fois pour toutes, puis calculer $e$ et la force de Laplace avec cette orientation.",
   r"Le freinage électromagnétique ajoute un terme de frottement fluide $\frac{B^2D^2}R\dot z$.",
   r"Lire un temps d'amortissement sur l'équation : $\tau=\frac{2m}{\alpha+B^2D^2/R}$."])
B['p-ind-3'] = ([AMPERE,
  r"**Inductance mutuelle.** $\Phi_{1\to2}=Mi_1$ et $\Phi_{2\to1}=Mi_2$, avec le même coefficient $M$ (théorème de Neumann)."],
  [r"Calculer le flux du champ le plus simple à connaître (celui du solénoïde long), puis utiliser la symétrie $M_{12}=M_{21}$.",
   r"Champ d'un solénoïde long : $\mu_0ni$ à l'intérieur, nul à l'extérieur.",
   r"Seule la surface de la spire intérieure au solénoïde compte."])
B['p-ondes-1'] = ([PFD, DALEMBERT,
  r"**Module d'Young.** $\frac FS=E\frac{\Delta\ell}\ell$ : une tranche $\mathrm dx$ se comporte comme un ressort de raideur $\frac{ES}{\mathrm dx}$."],
  [r"Modèle de la chaîne de masses et de ressorts, puis passage au continu.",
   r"Écrire le PFD sur une tranche et faire apparaître $\partial_x^2u$.",
   r"Identifier $c=\sqrt{E/\mu}$ par comparaison avec d'Alembert."])
B['p-ondes-2'] = ([PFD, OPPH,
  r"**Équation de Klein-Gordon.** $\partial_x^2z-\frac1{c^2}\partial_t^2z=\frac{\omega_c^2}{c^2}z$ : milieu dispersif, propagation seulement pour $\omega>\omega_c$."],
  [r"PFD projeté verticalement sur un tronçon $\mathrm dx$ ; la force de rappel des fils ajoute un terme en $z$.",
   r"Injecter une onde harmonique pour obtenir la relation de dispersion.",
   r"Pulsation de coupure : en dessous, onde évanescente."])
B['p-oem-2'] = ([OPPH],
  [r"Injecter l'onde complexe : $\partial_x\to-ik$, $\partial_t\to i\omega$.",
   r"Écrire $k=k'+ik''$ et identifier parties réelle et imaginaire de $k^2$.",
   r"Le signe de $k'k''$ dit si l'onde est atténuée dans le sens de propagation."])
B['p-oem-3'] = ([MAXWELL, POYNTING,
  r"**Effet de peau.** Dans un bon conducteur, le champ décroît comme $e^{-z/\delta}$ avec $\delta=\sqrt{\frac2{\mu_0\gamma\omega}}$."],
  [r"Obtenir $\vec B$ à partir de $\vec E$ par Maxwell-Faraday.",
   r"Puissance Joule volumique moyenne : $\frac12\gamma E^2$, à intégrer sur l'épaisseur.",
   r"Vérifier que la puissance dissipée égale le flux moyen du vecteur de Poynting entrant."])
B['p-oem-4'] = ([MAXWELL,
  r"**Milieu diélectrique linéaire.** $\vec P=\varepsilon_0\chi\vec E$, densités équivalentes $\rho=-\mathrm{div}\vec P$, $\vec j=\partial_t\vec P$ ; indice $n=\sqrt{1+\chi}$."],
  [r"Ajouter les densités de polarisation dans Maxwell, puis procéder comme dans le vide.",
   r"Modèle de l'électron élastiquement lié : $\chi(\omega)$ décroît avec $\lambda$, d'où la loi de Cauchy.",
   r"Développement limité de $n$ pour $\omega\ll\omega_0$."])
B['p-oem-5'] = ([MAXWELL, OPPH,
  r"**Pulsation plasma.** $\omega_p=\sqrt{\frac{ne^2}{m\varepsilon_0}}$ ; pour $\omega>\omega_p$ le milieu devient transparent."],
  [r"Négliger poids et force magnétique (électrons non relativistes).",
   r"Conductivité complexe, puis relation de dispersion $\underline k^2=\frac{\omega^2-\omega_p^2}{c^2}$.",
   r"Ordre de grandeur : $\omega_p\sim10^{16}$ rad/s pour un métal, d'où la transparence dans l'UV."])

# ----- mécanique -----
B['p-meca-1'] = ([INERTIE, RESONANCE],
  [r"Travailler dans le référentiel du boîtier : la force d'inertie d'entraînement joue le rôle d'excitation.",
   r"Fonction de transfert passe-haut en déplacement : au-delà de $\omega_0$, la masse reste fixe et la mesure donne le mouvement du sol.",
   r"Choisir $\omega_0$ petit et un amortissement voisin du critique."])
B['p-meca-2'] = ([INERTIE,
  r"**Énergie potentielle d'une force constante.** $\vec F=-m\vec A$ uniforme dérive de $E_p=m\vec A\cdot\overrightarrow{OM}$."],
  [r"Une force d'inertie d'entraînement de translation uniforme est conservative.",
   r"Position d'équilibre : minimum de l'énergie potentielle totale.",
   r"Petites oscillations : développer l'énergie potentielle au second ordre."])
B['p-meca-3'] = ([INERTIE, PFD],
  [r"Petites oscillations d'un pendule long : rappel horizontal $-\frac gL\overrightarrow{OM}$ (oscillateur 2D isotrope).",
   r"Passer au référentiel tournant pour comprendre la figure observée ; Coriolis fait tourner le plan.",
   r"Nombre de pétales : rapport entre $\sqrt{g/L}$ et $\Omega$."])
B['p-meca-4'] = ([INERTIE,
  r"**Poids dans le référentiel terrestre.** Il inclut la force d'inertie d'entraînement ; reste la force de Coriolis $-2m\vec\Omega\wedge\vec v$."],
  [r"Résoudre par perturbation : à l'ordre 0 chute libre, à l'ordre 1 Coriolis calculée avec la vitesse d'ordre 0.",
   r"Projeter $\vec\Omega$ dans la base locale (est, nord, verticale).",
   r"Ordre de grandeur : quelques centimètres pour une centaine de mètres de chute."])
B['p-meca-5'] = ([INERTIE, PFD],
  [r"Petites oscillations : la tension vaut $mg$ et rappelle horizontalement.",
   r"Seule la composante verticale de $\vec\Omega$ agit sur le mouvement horizontal : $\Omega\sin\lambda$.",
   r"Notation complexe $\rho=x+iy$ : l'équation devient du second ordre à coefficients constants."])
B['p-meca-6'] = ([TPC, PFD,
  r"**Mouvement dans un champ magnétique uniforme.** Sans frottement : cercle de rayon $\frac{mv}{|q|B}$, pulsation cyclotron $\omega=\frac{|q|B}m$."],
  [r"La force magnétique ne travaille pas : l'énergie ne varie qu'à cause du frottement.",
   r"Notation complexe pour le mouvement plan : $\dot z=v_0e^{-(1/\tau+i\omega)t}$.",
   r"Intégrer pour trouver le point limite de la spirale."])
B['p-meca-7'] = ([PFD, COULOMB],
  [r"Supposer le non-glissement, résoudre, puis vérifier la condition de Coulomb.",
   r"Le cube doit recevoir $m\omega^2X_m$ de la part du frottement.",
   r"L'amplitude maximale ne dépend pas de la masse du cube."])
B['p-meca-8'] = ([INERTIE, TMC, COULOMB],
  [r"Dans le référentiel du camion, la force d'inertie est appliquée au centre de masse.",
   r"Roulement sans glissement : $v=R\omega$ ; vérifier ensuite $\|T\|\le\mu N$.",
   r"Énergie cinétique d'un cylindre qui roule : $\frac34m\dot x^2$."])
B['p-meca-9'] = ([PFD, COULOMB,
  r"**Équilibre d'un solide.** Résultante et moment des forces nuls (pas de basculement)."],
  [r"Calculer les réactions normales par les équilibres vertical et des moments.",
   r"Frottement de glissement opposé à chaque vitesse relative : leur différence crée une force de rappel.",
   r"On obtient un oscillateur harmonique, dont la période permet de mesurer $\mu_d$."])
B['p-meca-10'] = ([TMC, COULOMB],
  [r"Phase de glissement : décélération du solide et accélération angulaire du rouleau jusqu'au roulement sans glissement.",
   r"Conserver le moment cinétique total quand il n'y a pas de couple extérieur.",
   r"La perte relative de vitesse à chaque rouleau donne une suite géométrique."])
B['p-meca-ccmp2'] = ([STATIQUE, PFD],
  [r"Écarter de l'équilibre : la variation de poussée d'Archimède donne la force de rappel.",
   r"Période $T=2\pi\sqrt{\frac{\rho_be}{\rho_eg}}$ : on en déduit la masse volumique du bois.",
   r"L'amortissement se lit sur la décroissance des amplitudes."])
B['p-meca-ccmp13'] = ([KEPLER, ENERGIE],
  [r"Orbite circulaire : $v=\sqrt{\frac{GM}r}$, avec $GM=g_0R_T^2$.",
   r"Une variation de vitesse en un point d'une orbite circulaire en fait l'apogée (ou le périgée) d'une ellipse.",
   r"Utiliser $E_m=-\frac{GMm}{2a}$ pour relier vitesse et demi-grand axe."])
B['p-meca-ccs1'] = ([PFD, KEPLER,
  r"**Barycentre.** $M_S\overrightarrow{GS}+M_J\overrightarrow{GJ}=\vec0$ ; le problème à deux corps se ramène à un mobile fictif de masse réduite."],
  [r"Placer l'origine au barycentre : les deux corps tournent à la même vitesse angulaire.",
   r"PFD pour Jupiter : $\omega^2=\frac{G(M_S+M_J)}{d^3}$ (Kepler corrigé).",
   r"Points de Lagrange : équilibre dans le référentiel tournant (gravitation + force centrifuge)."])
B['p-meca-ccs3'] = ([GAUSS, PFD,
  r"**Théorème de Gauss gravitationnel.** Le flux de $\vec g$ sortant d'une surface fermée vaut $-4\pi GM_{\text{int}}$."],
  [r"À l'intérieur d'une boule homogène, $g$ est proportionnel à $r$.",
   r"Projeter sur l'axe du tunnel : oscillateur harmonique de pulsation $\sqrt{g_0/R_T}$, indépendant du tunnel.",
   r"Durée du trajet : une demi-période, environ 42 min."])
B['p-meca-ccs-ressort'] = ([PFD,
  r"**Masse réduite.** Pour deux corps en interaction mutuelle : $\mu\ddot{\vec r}=\vec F$ avec $\mu=\frac{m_1m_2}{m_1+m_2}$ et $\vec r=\overrightarrow{M_1M_2}$."],
  [r"Écrire le PFD pour chaque masse, diviser par les masses et soustraire.",
   r"Le centre de masse a un mouvement rectiligne uniforme (système isolé).",
   r"Le mouvement relatif est celui d'une masse $\mu$ attachée au ressort."])

# ----- optique -----
B['p-opt-2'] = ([CONJ],
  [r"Distance objet-image d'une lentille : $D\ge4f'$ pour une image réelle d'un objet réel.",
   r"Exprimer $D$ en fonction de la position de la lentille et étudier la fonction.",
   r"Doubler la focale d'un objectif : grandissement $-1$ pour la lentille additionnelle, placée à $2f'$."])
B['p-opt-3'] = ([CONJ,
  r"**Grossissement commercial.** $G=\frac{\alpha'}{\alpha_0}$ avec $\alpha_0=\frac{AB}{d_m}$ ($d_m=25$ cm)."],
  [r"Œil au repos : l'image intermédiaire doit être au foyer objet de l'oculaire.",
   r"Le grandissement de l'objectif multiplie le grossissement de l'oculaire.",
   r"Garder les mesures algébriques jusqu'au bout pour les signes."])
B['p-opt-4'] = ([FRESNEL,
  r"**Déphasage à la réflexion.** Une réflexion sur un milieu plus réfringent ajoute $\frac\lambda2$ à la différence de marche."],
  [r"Épaisseur de la lame d'air par Pythagore : $\varepsilon\approx\frac{x^2}{2R}$.",
   r"Ne pas oublier le $\frac\lambda2$ supplémentaire dû à la réflexion.",
   r"Le centre sombre confirme le déphasage de réflexion."])
B['p-opt-5'] = ([RESEAU],
  [r"Différence de marche entre deux traits voisins : $a(\sin\theta-\sin i)$.",
   r"Nombre d'ordres observables : $|\sin\theta|\le1$.",
   r"Au minimum de déviation, $\sin\frac{D_m}2=\frac{p\lambda}{2a}$."])
B['p-opt-6'] = ([FRESNEL,
  r"**Lame d'air au Michelson.** Différence de marche $\delta=2e\cos i$ ; une lame d'indice $n$ et d'épaisseur $h$ ajoute $2(n-1)h$."],
  [r"Contact optique : $e=0$, teinte uniforme.",
   r"Chaque frange qui défile correspond à une variation de $\delta$ de $\lambda$.",
   r"Une lame introduite dans un bras décale de $2(n-1)h$ : on compte les franges."])
B['p-opt-7'] = ([FRESNEL, CONJ,
  r"**Coin d'air.** Franges d'égale épaisseur rectilignes, interfrange $i=\frac\lambda{2\alpha}$, localisées sur le coin."],
  [r"Franges localisées au voisinage du coin : on les projette avec une lentille.",
   r"$\delta=2\alpha x$ : interfrange $\frac\lambda{2\alpha}$, multiplié par $|\gamma|$ sur l'écran.",
   r"Bien distinguer localisation et observation."])
B['p-opt-8'] = ([FRESNEL,
  r"**Source à spectre large.** Les composantes spectrales sont incohérentes : on somme les éclairements $\mathrm d\mathcal E=2\mathcal D(\sigma)[1+\cos(2\pi\sigma\delta)]\mathrm d\sigma$."],
  [r"Intégrer sur le profil spectral : le contraste est la transformée de Fourier du spectre.",
   r"Profil gaussien de largeur $b$ : contraste gaussien en $\delta$.",
   r"Longueur de cohérence $\sim1/\Delta\sigma$."])
B['p-opt-ccmp1'] = ([FRESNEL,
  r"**Cohérence spatiale.** Deux points de la source donnent des systèmes de franges décalés ; le contraste disparaît quand le décalage atteint une interfrange."],
  [r"Calculer $\delta$ par développement limité ($a,x\ll D$).",
   r"Une source étendue : sommer les éclairements des points sources (incohérents).",
   r"Condition de visibilité : largeur angulaire de la source vue des trous inférieure à $\frac\lambda a$."])

# ----- quantique et statistique -----
B['p-q-1'] = ([SCHRO,
  r"**Condition de périodicité.** Sur un cercle, $\psi(\theta+2\pi)=\psi(\theta)$ : quantification $n\in\mathbb Z$."],
  [r"Remplacer $\frac{\mathrm d^2}{\mathrm dx^2}$ par $\frac1{R^2}\frac{\mathrm d^2}{\mathrm d\theta^2}$.",
   r"La périodicité joue le rôle des conditions aux limites.",
   r"Niveaux $n$ et $-n$ dégénérés (sens de rotation)."])
B['p-q-2'] = ([SCHRO],
  [r"Injecter la forme proposée et identifier les termes en $\frac1x$ et constants.",
   r"Un état lié a une énergie négative ; normaliser avec $\int_0^\infty x^2e^{-2kx}=\frac1{4k^3}$.",
   r"Analogie avec l'atome d'hydrogène (potentiel en $1/x$)."])
B['p-q-3'] = ([SCHRO, HEIS],
  [r"Analyse dimensionnelle d'abord : $|\psi|^2\,\mathrm dx$ est sans dimension.",
   r"Injecter la gaussienne et identifier les termes en $x^2$ et constants.",
   r"L'énergie du fondamental $\frac{\hbar\omega}2$ est non nulle : énergie de point zéro."])
B['p-q-4'] = ([SCHRO],
  [r"Oscillant dans le puits, évanescent dans la zone interdite : raccorder $\varphi$ et $\varphi'$.",
   r"Résolution graphique de l'équation transcendante $\tan(ka)=-k\delta$.",
   r"Existence d'un état lié seulement si le puits est assez profond et large ($k_0a>\frac\pi2$)."])
B['p-stat-1'] = ([BOLTZ,
  r"**Loi de Curie.** À haute température, l'aimantation est proportionnelle à $\frac BT$."],
  [r"Deux niveaux $\pm\mu_0B$ : probabilités par Boltzmann, moyenne en tangente hyperbolique.",
   r"Limites : saturation à basse température, régime linéaire (Curie) à haute température.",
   r"Comparer $\mu_0B$ à $k_BT$ pour savoir quel régime s'applique."])
B['p-stat-3'] = ([BOLTZ,
  r"**Entropie statistique.** $S=k_B\ln\Omega$ ; force entropique : $f=-T\frac{\partial S}{\partial\mathcal L}$."],
  [r"Dénombrer les configurations de longueur donnée : coefficients binomiaux.",
   r"Formule de Stirling pour dériver $\ln\binom Nk$.",
   r"Une fibre entropique se raidit quand la température augmente (comme le caoutchouc)."])

# ----- thermodynamique -----
B['p-th-1'] = ([P1, P2, GP],
  [r"Détente brutale sous pression extérieure constante : $W=-P_{\text{ext}}\Delta V$, pas de loi de Laplace.",
   r"Combiner premier principe et équation d'état pour trouver l'état final.",
   r"Entropie créée par la fonction d'état $S$, sur un chemin réversible fictif."])
B['p-th-4'] = ([LAPLACE_GP,
  r"**Premier principe industriel.** En écoulement permanent : $\Delta h+\Delta e_c=w_u+q$ par unité de masse."],
  [r"Chaque organe (compresseur, chambre, turbine, tuyère) : premier principe en écoulement.",
   r"Adiabatiques réversibles : lois de Laplace en $T$ et $P$.",
   r"La tuyère convertit l'enthalpie en énergie cinétique : $\frac12v^2=c_p\Delta T$."])
B['p-th-spe1'] = ([FOURIER, NEWTON_CC],
  [r"Bilan sur une tranche : Joule $+$ conduction $-$ pertes latérales.",
   r"Régime permanent puis transitoire : équation du premier ordre en temps.",
   r"Temps caractéristique $\tau=\frac{\mu ca}{2\beta}$ : capacité sur conductance."])
B['p-th-spe2'] = ([STEFAN],
  [r"Puissance solaire reçue : flux à la distance $r$ multiplié par la section du disque.",
   r"Équilibre radiatif d'une surface : puissance absorbée $=$ puissance émise.",
   r"$T\propto\sqrt{R_S/r}$ : à distance fixée, ne dépend pas de la taille du corps."])
B['p-th-spe3'] = ([STEFAN,
  r"**Changement de variable spectral.** $\mathcal D(\lambda)\,|\mathrm d\lambda|=\mathcal D(\omega)\,|\mathrm d\omega|$."],
  [r"Ne pas oublier le jacobien $\left|\frac{\mathrm d\omega}{\mathrm d\lambda}\right|$ en changeant de variable spectrale.",
   r"Maximum : dériver et résoudre une équation transcendante (solution numérique).",
   r"Intégrer sur tout le spectre : $\int_0^\infty\frac{x^3}{e^x-1}\mathrm dx=\frac{\pi^4}{15}$."])
B['p-th-spe4'] = ([P1, LAPLACE_GP,
  r"**Pression de radiation.** Un gaz de photons isotrope exerce $P=\frac u3$."],
  [r"Calculer la pression par transfert de quantité de mouvement sur une paroi.",
   r"Détente adiabatique réversible avec $U=uV$ et $u\propto T^4$ : $TV^{1/3}=\text{cte}$.",
   r"Application cosmologique : $T\propto\frac1R$."])
B['p-th-spe5'] = ([FOURIER, OPPH, DIFF],
  [r"Injecter une onde harmonique dans l'équation de la chaleur : $k=\frac{1-i}\delta$.",
   r"Épaisseur de pénétration $\delta=\sqrt{\frac{2\lambda}{\mu c\omega}}$ : elle croît comme $\sqrt T$.",
   r"Théorie des caves : à quelques mètres, la variation annuelle est très atténuée et déphasée."])
B['p-th-spe6'] = ([FOURIER, RTH],
  [r"En régime permanent sans source, le flux est conservé à travers tout cylindre coaxial.",
   r"Intégrer $\frac{\mathrm dT}{\mathrm dr}=-\frac\Phi{2\pi\lambda Lr}$ : profil logarithmique.",
   r"La résistance thermique cylindrique contient $\ln\frac{a_2}{a_1}$."])
B['p-th-ccs4'] = ([FOURIER],
  [r"Bilan avec source : $\lambda T''+q=0$ en régime permanent.",
   r"Symétrie : la température est maximale au milieu.",
   r"Vérification : le flux sortant total égale la puissance produite $2qL$."])
B['p-th-ccmp4'] = ([FOURIER, CHGT_ETAT],
  [r"Régime quasi stationnaire dans une couche mince : profil linéaire.",
   r"Bilan à l'interface : le flux conduit évacue la chaleur latente de la glace formée.",
   r"Croissance en $\sqrt t$, signature d'un phénomène diffusif."])
B['p-th-ccmp15'] = ([FOURIER, RTH],
  [r"Bilan entre production métabolique et pertes par conduction à travers la graisse.",
   r"Couche mince : géométrie quasi plane.",
   r"En déduire une taille minimale : les petits animaux perdent trop de chaleur."])
B['p-ccs-bulle'] = ([STATIQUE, PFD,
  r"**Force de Stokes.** Une sphère de rayon $r$ à faible vitesse dans un fluide de viscosité $\eta$ subit $-6\pi\eta r\vec v$."],
  [r"Masse de la bulle négligeable devant celle du liquide déplacé.",
   r"Vitesse limite : Archimède équilibre la traînée.",
   r"Vérifier a posteriori le nombre de Reynolds pour justifier Stokes."])
B['p-ccs-plan'] = ([GAUSS, CURIE, PFD],
  [r"Symétries d'un plan infini : $\vec E=E(z)\vec u_z$, impair en $z$.",
   r"Surface de Gauss : cylindre symétrique par rapport au plan médian.",
   r"Une charge dans le champ $\propto z$ à l'intérieur oscille harmoniquement."])
