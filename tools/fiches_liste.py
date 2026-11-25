# Liste des fiches de cours et des schémas attendus (une fiche par chapitre). Source du tableau partagé.
import json
# (matiere, niveau, fiche_id, fiche_titre, [(schema, contenu, prio)])
D = [
('Physique','MPSI','p1-oscillateur','Oscillateur harmonique',[
 ('Masse-ressort horizontal','Masse sur support sans frottement, ressort, axe Ox, position d\'équilibre x=0, allongement',1),
 ('Graphe x(t)','Sinusoïde avec amplitude X_m, période T, phase à l\'origine',1),
 ('Portrait de phase','Ellipse (x, dx/dt) parcourue dans le sens horaire',2)]),
('Physique','MPSI','p1-propagation','Propagation d\'un signal',[
 ('Onde progressive','Profil s(x) à t et à t+Δt, décalé de cΔt dans le sens de propagation',1),
 ('Double périodicité','Onde sinusoïdale : vue en x (λ) et vue en t (T) côte à côte',1)]),
('Physique','MPSI','p1-superposition','Superposition de deux signaux sinusoïdaux',[
 ('Interférences de deux sources','Deux sources ponctuelles, point M, distances d1 et d2, zones d\'amplitude max/min',1),
 ('Ondes stationnaires sur une corde','Corde fixée aux deux bouts, modes n=1,2,3, nœuds et ventres, L = nλ/2',1),
 ('Battements','Somme de deux sinusoïdes de fréquences proches, enveloppe',2)]),
('Physique','MPSI','p1-onde-lumineuse','Onde lumineuse',[
 ('Spectre électromagnétique','Échelle des longueurs d\'onde, domaine visible 400-800 nm détaillé',1),
 ('Diffraction par une fente','Fente de largeur a, faisceau, écran, demi-angle θ ≈ λ/a, tache centrale',1)]),
('Physique','MPSI','p1-optique-geo','Optique géométrique',[
 ('Lois de Snell-Descartes','Dioptre plan, normale, rayons incident, réfléchi, réfracté, angles i1, i2, indices n1, n2',1),
 ('Réflexion totale','Rayon rasant, angle limite, cas n1 > n2',1),
 ('Lentille convergente','Construction de l\'image avec les 3 rayons particuliers, F, F\', O, objet AB, image A\'B\'',1),
 ('Lentille divergente','Même construction, image virtuelle',1),
 ('Lunette astronomique afocale','Objectif + oculaire, F\'1 = F2, faisceaux parallèles, angles α et α\'',2),
 ('Modèle de l\'œil','Cristallin = lentille, rétine = écran, punctum proximum et remotum',2)]),
('Physique','MPSI','p1-quantique','Introduction au monde quantique',[
 ('Fentes d\'Young électron par électron','Impacts qui apparaissent un à un puis forment des franges',1),
 ('Niveaux d\'énergie','Diagramme en énergie, absorption et émission d\'un photon hν = E_n − E_p',1)]),
('Physique','MPSI','p1-arqs','Circuits électriques dans l\'ARQS',[
 ('Conventions récepteur et générateur','Dipôle avec flèches de u et i dans les deux conventions',1),
 ('Lois de Kirchhoff','Un nœud avec courants entrants/sortants, une maille avec tensions',1),
 ('Diviseurs de tension et de courant','Deux résistances en série puis en parallèle',1)]),
('Physique','MPSI','p1-premier-ordre','Circuit linéaire du premier ordre',[
 ('Circuit RC série','Générateur d\'échelon E, interrupteur, R, C, u_C',1),
 ('Charge du condensateur','u_C(t) avec asymptote E, tangente à l\'origine, τ = RC, 63 %',1),
 ('Circuit RL série','Générateur, R, L, courant i(t)',2)]),
('Physique','MPSI','p1-second-ordre','Circuit linéaire du second ordre',[
 ('Circuit RLC série','Générateur, R, L, C, u_C',1),
 ('Trois régimes','Pseudo-périodique, critique, apériodique sur un même graphe',1)]),
('Physique','MPSI','p1-sinusoidal','Régime sinusoïdal forcé',[
 ('Représentation de Fresnel','Vecteurs tournants U_R, U_L, U_C et U, déphasage φ',2),
 ('Résonance en intensité','Courbes I(ω) pour plusieurs facteurs de qualité Q, bande passante Δω',1),
 ('Résonance en tension aux bornes de C','Courbes selon Q, existence ou non de la résonance',2)]),
('Physique','MPSI','p1-frequentielle','Analyse fréquentielle d\'un système linéaire',[
 ('Spectre d\'un signal créneau','Raies aux harmoniques impaires, amplitudes en 1/n',1),
 ('Diagramme de Bode générique','Gain en dB et phase en fonction de log ω, asymptotes',1)]),
('Physique','MPSI','p1-filtrage','Filtrage linéaire',[
 ('Passe-bas RC','Schéma du filtre et Bode asymptotique + réel, ω_c',1),
 ('Passe-haut RC','Schéma et Bode',1),
 ('Passe-bande RLC','Schéma et Bode, bande passante',1),
 ('Effet d\'un filtre sur un spectre','Spectre d\'entrée, gabarit du filtre, spectre de sortie',2)]),
('Physique','MPSI','p2-cinematique','Cinématique du point',[
 ('Base cartésienne','Repère (O, ux, uy, uz), point M, vecteur position',1),
 ('Base polaire','Point M, r, θ, vecteurs u_r et u_θ',1),
 ('Base cylindrique','r, θ, z et (u_r, u_θ, u_z)',1),
 ('Base sphérique','r, θ, φ et (u_r, u_θ, u_φ)',2),
 ('Mouvement circulaire','Vitesse tangente, accélération tangentielle et normale (centripète)',1)]),
('Physique','MPSI','p2-solide','Cinématique du solide',[
 ('Translation et rotation','Solide en translation (vecteurs vitesse égaux) vs rotation autour d\'un axe fixe (v = rω)',1)]),
('Physique','MPSI','p2-dynamique','Principes de la dynamique newtonienne',[
 ('Plan incliné','Bloc, poids, réaction normale, frottement, angle α, axes choisis',1),
 ('Pendule simple','Fil, masse, angle θ, tension, poids, base polaire',1),
 ('Mouvement d\'un projectile','Parabole, v0, angle, portée, flèche',2)]),
('Physique','MPSI','p2-energie','Aspects énergétiques de la dynamique du point',[
 ('Travail d\'une force','Trajectoire de A à B, force et déplacement élémentaire dl',2),
 ('Énergie potentielle et équilibres','Courbe Ep(x), minimum = équilibre stable, maximum = instable',1)]),
('Physique','MPSI','p2-puits','Mouvement dans un puits de potentiel',[
 ('Zones accessibles','Ep(x), niveau Em horizontal, points de rebroussement, état lié ou de diffusion',1),
 ('Approximation harmonique','Ep(x) et sa parabole tangente au fond du puits',1)]),
('Physique','MPSI','p2-charge','Particule chargée dans un champ E ou B',[
 ('Déviation entre deux plaques','Condensateur plan, E uniforme, trajectoire parabolique d\'un électron',1),
 ('Mouvement cyclotron','B uniforme orthogonal à la vitesse, cercle de rayon R = mv/(|q|B), sens selon le signe de q',1),
 ('Trajectoire en hélice','v ayant une composante parallèle à B',2)]),
('Physique','MPSI','p3-moment','Moment cinétique et solide en rotation',[
 ('Moment d\'une force','Bras de levier d, axe Δ, force F',1),
 ('Pendule pesant','Solide en rotation autour d\'un axe, centre de gravité G, distance a, angle θ',1),
 ('Couple de forces','Deux forces opposées non alignées',2)]),
('Physique','MPSI','p3-central','Force centrale, champs newtoniens',[
 ('Loi des aires','Aires balayées égales pendant des durées égales',1),
 ('Énergie potentielle effective','Ep,eff(r), niveaux d\'énergie : état lié (r entre rmin et rmax) ou de diffusion',1),
 ('Trajectoires coniques','Ellipse avec foyer, périgée, apogée, demi-grand axe a ; parabole et hyperbole',1),
 ('Satellite géostationnaire','Orbite équatoriale, Terre en rotation, altitude',2)]),
('Physique','MPSI','p4-equilibre','Système thermodynamique à l\'équilibre',[
 ('Diagramme (P,T) d\'un corps pur','Solide, liquide, gaz, point triple, point critique ; cas de l\'eau',1),
 ('Diagramme de Clapeyron (P,v)','Courbe de saturation, isothermes, palier de changement d\'état, titre x',1)]),
('Physique','MPSI','p4-energie','Énergie échangée au cours d\'une transformation',[
 ('Travail et aire en diagramme de Watt','Transformation en (P,V), aire sous la courbe',1),
 ('Cycle moteur et cycle récepteur','Même cycle parcouru dans les deux sens, signe du travail',1)]),
('Physique','MPSI','p4-premier','Premier principe, bilans d\'énergie',[
 ('Détente de Joule-Gay-Lussac','Deux compartiments, vide, robinet, parois calorifugées',1),
 ('Calorimètre','Vase isolé, thermomètre, agitateur',2)]),
('Physique','MPSI','p4-second','Deuxième principe, bilans d\'entropie',[
 ('Cycle en diagramme (T,S)','Cycle de Carnot : rectangle, aire = travail',2)]),
('Physique','MPSI','p4-machines','Machines thermiques',[
 ('Moteur ditherme','Sources chaude et froide, flèches Qc, Qf, W avec leurs signes',1),
 ('Réfrigérateur et pompe à chaleur','Même schéma, sens des transferts inversés',1),
 ('Cycle de Carnot en (P,V)','Deux isothermes, deux adiabatiques',1),
 ('Cycle de Beau de Rochas','Moteur à essence en (P,V)',2)]),
('Physique','MPSI','p5-champ-b','Le champ magnétique',[
 ('Lignes de champ d\'un aimant droit','Pôles N et S, lignes sortant du nord',1),
 ('Fil rectiligne','Lignes circulaires, règle de la main droite',1),
 ('Spire circulaire','Lignes de champ, champ sur l\'axe',1),
 ('Solénoïde','Champ uniforme à l\'intérieur, lignes à l\'extérieur',1)]),
('Physique','MPSI','p5-actions','Actions d\'un champ magnétique',[
 ('Force de Laplace sur une barre','Rails, barre mobile, courant I, champ B, force F = I L ∧ B',1),
 ('Spire dans un champ uniforme','Moment magnétique m, couple Γ = m ∧ B, position d\'équilibre',1)]),
('Physique','MPSI','p5-induction','Lois de l\'induction',[
 ('Flux à travers une surface orientée','Circuit, normale orientée par le sens du courant, B',1),
 ('Loi de Lenz','Aimant qui s\'approche d\'une spire, courant induit qui s\'oppose',1)]),
('Physique','MPSI','p5-circuit-fixe','Circuit fixe dans un champ variable',[
 ('Inductance mutuelle','Deux bobines couplées, M, circuits primaire et secondaire',1),
 ('Transformateur','Noyau, N1 et N2 spires, u1, u2',2)]),
('Physique','MPSI','p5-circuit-mobile','Circuit mobile dans un champ stationnaire',[
 ('Rails de Laplace','Barre qui glisse, schéma électrique équivalent avec e = −dΦ/dt',1),
 ('Spire en rotation (alternateur)','Spire tournant à ω dans B uniforme, angle θ = ωt',2)]),
('Physique','MPSI','px-incertitudes','Mesures et incertitudes',[
 ('Distribution de mesures','Histogramme et gaussienne, valeur moyenne, écart-type',2),
 ('Régression linéaire','Points avec barres d\'incertitude et droite ajustée',2)]),
# ---------------- MP
('Physique','MP','mp-referentiels','Changements de référentiels',[
 ('Référentiels en translation et en rotation','R et R\', origine O et O\', axe de rotation, vecteur ω',1),
 ('Composition des vitesses','Point M, vitesse relative, vitesse d\'entraînement',1)]),
('Physique','MP','mp-non-galileen','Dynamique dans un référentiel non galiléen',[
 ('Force centrifuge','Manège, point à distance r de l\'axe, force −m ω ∧ (ω ∧ HM)',1),
 ('Force de Coriolis','Déviation vers l\'est d\'un corps en chute, et vents sur la Terre',1),
 ('Pendule dans un véhicule accéléré','Inclinaison d\'équilibre du fil, pesanteur apparente',1),
 ('Poids et pesanteur','Terre en rotation, latitude λ, g et gravitation',2)]),
('Physique','MP','mp-frottement','Lois du frottement solide',[
 ('Cône de frottement','Réaction R = N + T, angle φ avec tan φ = f',1),
 ('Adhérence et glissement sur plan incliné','Bloc sur plan d\'angle α, cas tan α < f et tan α > f',1)]),
('Physique','MP','mp-signal','Signaux périodiques, filtrage',[
 ('Gabarit d\'un filtre','Zones interdites, fréquences de coupure',2),
 ('Filtrage d\'un créneau','Signal d\'entrée et de sortie d\'un passe-bas (intégrateur) et d\'un passe-haut (dérivateur)',1)]),
('Physique','MP','mp-numerique','Électronique numérique',[
 ('Échantillonnage','Signal continu et échantillons tous les Te',1),
 ('Repliement de spectre','Spectre échantillonné, motifs répétés à fe, critère de Shannon',1),
 ('Quantification','Signal en escalier d\'un CAN, pas q',2)]),
('Physique','MP','mp-ondes-lumineuses','Modèle scalaire des ondes lumineuses',[
 ('Surfaces d\'onde et rayons','Théorème de Malus, chemin optique entre deux surfaces d\'onde',1),
 ('Train d\'onde','Durée τc, longueur de cohérence ℓc = cτc',2)]),
('Physique','MP','mp-interferences','Interférences de deux ondes',[
 ('Intensité en fonction de δ','I(δ) sinusoïdale entre Imin et Imax, contraste',1)]),
('Physique','MP','mp-young','Trous d\'Young',[
 ('Dispositif des trous d\'Young','Source S, trous S1 et S2 distants de a, écran à D, point M d\'abscisse x',1),
 ('Calcul de la différence de marche','Triangle avec δ = ax/D',1),
 ('Figure d\'interférences','Franges, interfrange i = λD/a',1)]),
('Physique','MP','mp-michelson','Interféromètre de Michelson',[
 ('Schéma général','Source, séparatrice, compensatrice, miroirs M1 et M2, écran',1),
 ('Lame d\'air','Schéma équivalent, anneaux à l\'infini, δ = 2e cos i',1),
 ('Coin d\'air','Schéma équivalent, franges rectilignes localisées',1)]),
('Physique','MP','mp-n-ondes','Interférences de N ondes cohérentes',[
 ('Réseau par transmission','Pas a, angles θi et θ, différence de marche entre deux traits',1),
 ('Intensité pour N ondes','Pics fins, largeur en 1/N, comparaison N = 2 et N grand',1)]),
('Physique','MP','mp-electrostatique','Champ électrostatique',[
 ('Symétries et invariances','Distribution, plan de symétrie (E contenu) et d\'antisymétrie (E orthogonal)',1),
 ('Théorème de Gauss','Surface fermée, flux sortant, charges intérieures',1)]),
('Physique','MP','mp-exemples-e','Exemples de champs électrostatiques',[
 ('Boule uniformément chargée','Sphère de Gauss et courbe E(r) : linéaire puis en 1/r²',1),
 ('Fil infini','Cylindre de Gauss, E en 1/r',1),
 ('Plan infini','Cylindre de Gauss traversant le plan, E uniforme de chaque côté',1),
 ('Condensateur plan','Deux armatures, champ uniforme entre elles',1)]),
('Physique','MP','mp-dipole-e','Dipôle électrostatique',[
 ('Lignes de champ et équipotentielles','Dipôle p, lignes et équipotentielles orthogonales',1),
 ('Dipôle dans un champ extérieur','Couple Γ = p ∧ E, équilibre stable',2)]),
('Physique','MP','mp-magnetostatique','Champ magnétostatique',[
 ('Théorème d\'Ampère pour un fil','Contour circulaire, B orthoradial',1),
 ('Solénoïde infini','Contour rectangulaire, B = μ0 n I à l\'intérieur',1),
 ('Câble coaxial','Coupe, contours pour les différentes zones, B(r)',2),
 ('Nappe de courant','Plan parcouru par j_s, B de chaque côté',2)]),
('Physique','MP','mp-dipole-m','Dipôle magnétique',[
 ('Analogie spire et dipôle','Lignes de champ d\'une spire loin de celle-ci, moment m',1),
 ('Boussole dans un champ','Aiguille, moment, couple de rappel',2)]),
('Physique','MP','mp-maxwell','Équations de Maxwell',[
 ('Relations de passage','Interface entre deux milieux, normale n12, charges et courants surfaciques',2)]),
('Physique','MP','mp-energie-em','Énergie du champ électromagnétique',[
 ('Vecteur de Poynting dans un fil résistif','Fil, E le long du fil, B orthoradial, Π entrant',1),
 ('Bilan local d\'énergie','Volume V, surface S, flux de Π sortant',2)]),
('Physique','MP','mp-ondes-vide','Ondes électromagnétiques dans le vide',[
 ('Trièdre de l\'OPPM','E, B, k orthogonaux, B = k ∧ E/ω',1),
 ('Polarisations','Rectiligne, circulaire et elliptique : trajectoire du bout de E',1)]),
('Physique','MP','mp-plasma','Propagation dans un plasma, dispersion',[
 ('Relation de dispersion','ω(k) avec coupure à ωp, asymptote ω = ck',1),
 ('Paquet d\'ondes','Enveloppe à v_g et porteuse à v_φ',1)]),
('Physique','MP','mp-conducteur','Onde dans un conducteur, réflexion',[
 ('Effet de peau','Amplitude qui décroît en exp(−z/δ) dans le métal',1),
 ('Réflexion sur un métal parfait','Ondes incidente et réfléchie, onde stationnaire, nœuds de E sur le plan',1)]),
('Physique','MP','mp-rayonnement','Rayonnement dipolaire',[
 ('Dipôle oscillant','Dipôle p(t) suivant uz, point M en sphériques, zone de rayonnement',1),
 ('Indicatrice de rayonnement','Puissance en sin²θ (tore), aucune émission selon l\'axe',1)]),
('Physique','MP','mp-systemes-ouverts','Systèmes ouverts en régime stationnaire',[
 ('Système fermé fictif','Conduite, volume de contrôle, masses entrant et sortant pendant dt',1),
 ('Organes industriels','Compresseur, turbine, détendeur, tuyère, échangeur : symboles',1),
 ('Diagramme (P,h) d\'une machine frigorifique','Cycle sur le diagramme avec courbe de saturation',1)]),
('Physique','MP','mp-diffusion','Transferts thermiques',[
 ('Bilan sur une tranche','Tranche entre x et x+dx, flux entrant et sortant',1),
 ('Mur et résistance thermique','Profil T(x) linéaire et schéma électrique équivalent (résistances en série)',1),
 ('Conducto-convection','Paroi, fluide, loi de Newton φ = h S (T − Text)',2)]),
('Physique','MP','mp-quantique','Introduction à la mécanique quantique',[
 ('Densité de probabilité','|ψ(x)|² et aire = probabilité de présence',1),
 ('Inégalité de Heisenberg','Paquet d\'onde étroit en x large en k, et inversement',2)]),
('Physique','MP','mp-libre','Particule quantique libre',[
 ('Étalement du paquet d\'ondes','|ψ|² à plusieurs instants',2)]),
('Physique','MP','mp-potentiel','Particule quantique dans un potentiel',[
 ('Marche de potentiel','Cas E > V0 et E < V0, onde évanescente',1),
 ('Puits infini','Niveaux E_n en n² et fonctions propres n = 1, 2, 3',1),
 ('Effet tunnel','Barrière de largeur a, onde transmise atténuée',1),
 ('Puits fini','États liés, ondes qui débordent du puits',2)]),
('Physique','MP','mp-statistique','Thermodynamique statistique',[
 ('Atmosphère isotherme','Densité n(z) en exp(−mgz/kT)',1),
 ('Système à deux niveaux','Populations des deux niveaux en fonction de T',1)]),
# ---------------- Chimie MPSI
('Chimie','MPSI','c-matiere','Transformation de la matière',[
 ('Diagramme (P,T) d\'un corps pur','Cas général et cas de l\'eau (pente négative solide/liquide)',1)]),
('Chimie','MPSI','c-classification','Classification périodique',[
 ('Tableau périodique simplifié','Blocs s, p, d, f, familles (alcalins, halogènes, gaz nobles)',1),
 ('Évolution des propriétés','Électronégativité et rayon atomique selon la ligne et la colonne',1),
 ('Niveaux de l\'hydrogène','Diagramme En = −13,6/n² eV, séries de Lyman et Balmer',2)]),
('Chimie','MPSI','c-lewis','Modèle de Lewis',[
 ('Géométries VSEPR','AX2 à AX6 et formes avec doublets non liants (coudée, pyramidale)',1),
 ('Moment dipolaire','Molécule polaire (H2O) et apolaire (CO2) avec moments de liaison',1)]),
('Chimie','MPSI','c-cinetique','Cinétique chimique',[
 ('Méthode intégrale','Graphes [A], ln[A] et 1/[A] en fonction de t pour les ordres 0, 1 et 2',1),
 ('Loi d\'Arrhenius','ln k en fonction de 1/T, pente −Ea/R',1),
 ('Profil énergétique','Énergie le long de la coordonnée réactionnelle, état de transition, Ea',2)]),
('Chimie','MPSI','c-intermoleculaire','Forces intermoléculaires',[
 ('Liaison hydrogène','Molécules d\'eau liées, donneur et accepteur',1),
 ('Solvatation d\'un ion','Ion entouré de molécules d\'eau orientées',2)]),
('Chimie','MPSI','c-cristal','Le solide cristallin',[
 ('Maille cubique faces centrées','Atomes, contact sur la diagonale d\'une face',1),
 ('Maille cubique centrée','Contact sur la grande diagonale',1),
 ('Hexagonal compact','Empilement ABAB',2),
 ('Sites tétraédriques et octaédriques','Position des sites dans la maille CFC',1),
 ('Chlorure de sodium et chlorure de césium','Les deux structures ioniques',1),
 ('Blende ZnS et diamant','Atomes dans la moitié des sites tétraédriques',2)]),
('Chimie','MPSI','c-acide-base','Équilibres acido-basiques, titrages',[
 ('Diagramme de prédominance','Axe de pH avec pKa, zones HA et A⁻',1),
 ('Courbe de titrage pH-métrique','Saut de pH, équivalence, demi-équivalence pH = pKa',1),
 ('Titrage conductimétrique','Segments de droite, rupture de pente à l\'équivalence',2)]),
('Chimie','MPSI','c-solubilite','Équilibres de solubilité',[
 ('Diagramme d\'existence','Axe pX, frontière d\'apparition du précipité',1),
 ('Solubilité en fonction du pH','Courbe log s(pH)',2)]),
('Chimie','MPSI','c-redox','Oxydoréduction',[
 ('Pile Daniell','Deux compartiments, pont salin, électrodes, sens des électrons et du courant',1),
 ('Échelle de potentiels','Couples rangés par E°, réaction spontanée entre l\'oxydant le plus fort et le réducteur le plus fort',1)]),
('Chimie','MPSI','c-e-ph','Diagrammes potentiel-pH',[
 ('Diagramme E-pH de l\'eau','Droites des couples O2/H2O et H2O/H2, domaine de stabilité',1),
 ('Diagramme E-pH du fer','Domaines de Fe, Fe²⁺, Fe³⁺, Fe(OH)2, Fe(OH)3',1),
 ('Superposition de deux diagrammes','Domaines disjoints = réaction, lecture de la stabilité',2)]),
]
