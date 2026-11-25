# Bilans — physique d'après planches CCINP, préparation aux oraux et rapport Centrale 2025 (n-pc-*)
B = {}
PP = r"**Premier principe.** $\mathrm dU=\delta W+\delta Q$ ; pour une phase condensée, $\mathrm dU=C\,\mathrm dT$."
ORDRE1 = r"**Équation du premier ordre.** $\tau\dot y+y=y_\infty$ a pour solution $y=y_\infty+(y_0-y_\infty)e^{-t/\tau}$."
COND = r"**Condensateur.** $q=Cu$, $i=\dot q$, énergie $\frac{q^2}{2C}$ ; la charge est continue."
MC = r"**Théorème du moment cinétique.** $\frac{\mathrm d\vec L_O}{\mathrm dt}=\sum\mathcal{\vec M}_O$."
EM = r"**Énergie mécanique.** Conservée si seules des forces conservatives travaillent."
DEUXSRC = r"**Deux sources cohérentes.** $\delta\approx\frac{ax}D$, $\mathcal E=2\mathcal E_0\big(1+\cos\frac{2\pi\delta}\lambda\big)$, interfrange $i=\frac{\lambda D}a$."
SYM = r"**Symétries.** $\vec B$ est contenu dans les plans d'antisymétrie des courants et orthogonal à leurs plans de symétrie."

B['n-pc-radiateur'] = ([PP, ORDRE1, r"**Loi de Newton.** Puissance conducto-convective $h(T-T_0)$."],
  [r"Définir le système et la durée $\mathrm dt$ avant d'écrire le bilan.", r"Régime établi à 1 % au bout de $\tau\ln100\approx4{,}6\,\tau$.", r"Vérifier l'homogénéité : $\tau=C/h$ est un temps."])
B['n-pc-deuxcond'] = ([COND, r"**Conservation de la charge.** La charge totale d'un ensemble de conducteurs isolés est constante."],
  [r"État final : conservation de la charge + égalité des tensions.", r"Capacités en série pour la constante de temps : $\frac{C_0C_1}{C_0+C_1}$.", r"L'énergie dissipée ne dépend pas de $R$."])
B['n-pc-elastique'] = ([MC, EM, r"**Énergie potentielle effective.** $E_{p,\mathrm{eff}}=\frac{m\mathcal C^2}{2r^2}+E_p(r)$."],
  [r"Force centrale ⇒ mouvement plan et loi des aires.", r"Lire les bornes du mouvement sur le graphe de $E_{p,\mathrm{eff}}$.", r"Force élastique : ellipse centrée (et non de foyer $O$)."])
B['n-pc-filtre-id'] = ([r"**Comportements limites.** En continu et en BF, $C$ ouvert et $L$ fil ; en HF, l'inverse.", r"**Passe-bande d'ordre 2.** $H=\frac{H_0}{1+jQ(x-1/x)}$, $\Delta\omega=\omega_0/Q$."],
  [r"Analyser BF et HF avant tout calcul.", r"Pont diviseur seulement si le même courant traverse les deux dipôles (sortie ouverte).", r"Utiliser une mesure en continu pour éliminer des configurations."])
B['n-pc-decollage'] = ([EM, r"**Mouvement circulaire.** $\vec a=-R\dot\theta^2\vec e_r+R\ddot\theta\,\vec e_\theta$."],
  [r"Le décollage correspond à $N=0$.", r"Énergie pour la vitesse, principe fondamental pour la réaction.", r"Près d'un équilibre instable, linéariser : croissance en $\operatorname{ch}(t/\tau)$."])
B['n-pc-barre2sources'] = ([r"**Résistance thermique.** $R_{th}=\frac L{\lambda S}$ ; flux uniforme sans source ni stockage.", r"**Entropie d'une phase condensée.** $\Delta S=C\ln\frac{T_f}{T_i}$."],
  [r"Capacité de la barre négligeable ⇒ profil affine à chaque instant.", r"Étudier l'écart de température : une seule exponentielle.", r"Système isolé : $\Delta S=S_{\text{créée}}\ge0$ (concavité du logarithme)."])
B['n-pc-armatures'] = ([COND, r"**Bilan de charge d'un condensateur.** Le générateur fournit $CE^2$ : moitié stockée, moitié dissipée."],
  [r"Une opération brève conserve la charge du condensateur.", r"Énergie fournie par un générateur de tension : $E\,\Delta q$, avec son signe.", r"Vérifier un bilan d'énergie par le calcul direct de $\int Ri^2\,\mathrm dt$."])
B['n-pc-pac'] = ([r"**Loi de Laplace.** $TV^{\gamma-1}$ constant pour une adiabatique réversible d'un gaz parfait.", r"**Second principe (cycle ditherme).** $\frac{Q_c}{T_c}+\frac{Q_f}{T_f}\le0$, égalité si réversible."],
  [r"Efficacité d'une pompe à chaleur : $\frac{-Q_c}{W}\le\frac{T_c}{T_c-T_f}$.", r"Sur une isotherme d'un gaz parfait, $Q=-W=nRT\ln\frac{V_f}{V_i}$.", r"Diagramme $(S,T)$ d'un cycle de Carnot : un rectangle."])
B['n-pc-etoiledouble'] = ([DEUXSRC, r"**Sources incohérentes.** Les éclairements s'ajoutent."],
  [r"Une onde plane inclinée de $\varepsilon$ ajoute la différence de marche $a\varepsilon$ entre les trous.", r"Factoriser la somme de deux cosinus pour lire le contraste.", r"Interférométrie stellaire : $\varepsilon=\frac\lambda{2a_1}$ à la première annulation."])
B['n-pc-deuxopph'] = ([r"**Maxwell-Ampère dans le vide.** $\overrightarrow{\mathrm{rot}}\,\vec B=\frac1{c^2}\partial_t\vec E$.", r"**Vecteur de Poynting.** $\vec\Pi=\frac{\vec E\wedge\vec B}{\mu_0}$, à calculer en réel."],
  [r"Deux ondes planes symétriques : progressive selon l'axe, stationnaire transversalement.", r"$v_\varphi>c$ n'est pas un problème : l'énergie va à $c\cos\alpha$ et $v_\varphi v_e=c^2$.", r"Moyenner dans le temps et dans l'espace avant de calculer une vitesse de l'énergie."])
B['n-pc-spire'] = ([SYM, r"**Loi de Biot et Savart.** $\mathrm d\vec B=\frac{\mu_0}{4\pi}\frac{I\,\mathrm d\vec\ell\wedge\overrightarrow{PM}}{PM^3}$."],
  [r"Sur l'axe, toutes les contributions ont la même composante axiale.", r"Champ au centre : $\frac{\mu_0I}{2R}$.", r"Loin de la spire : champ de dipôle, en $1/x^3$, avec $m=I\pi R^2$."])
B['n-pc-troisfils'] = ([r"**Fil infini.** $\vec B=\frac{\mu_0I}{2\pi r}\vec e_\theta$.", r"**Force de Laplace.** $\mathrm d\vec F=I\,\mathrm d\vec\ell\wedge\vec B$."],
  [r"Placer la figure dans un repère et écrire chaque $\vec e_\theta=\vec e_z\wedge\vec e_r$.", r"Champ nul en un point ⇒ force nulle sur un fil placé en ce point.", r"Exploiter la symétrie par rapport à la diagonale."])
B['n-pc-cylressort'] = ([MC, r"**Roulement sans glissement.** Vitesse nulle du point de contact ; $|T|\le f|N|$."],
  [r"Masse effective $M+\frac J{R^2}=\frac32M$ pour un cylindre plein.", r"Vérifier la condition de non-glissement sur tout le mouvement (au maximum de $|T|$).", r"Sans glissement, les actions de contact ne travaillent pas : méthode énergétique."])
B['n-pc-langevin'] = ([r"**Loi de Boltzmann.** Probabilité d'un état d'énergie $\varepsilon$ proportionnelle à $e^{-\varepsilon/k_BT}$.", r"**Angle solide.** $\mathrm d\Omega=\sin\theta\,\mathrm d\theta\,\mathrm d\phi$."],
  [r"Changement de variable $u=\cos\theta$ pour les intégrales d'orientation.", r"$\langle\cos\theta\rangle=\frac{\mathrm d}{\mathrm dy}\ln Z$.", r"Loi de Curie à haute température ; saturation à basse température."])
B['n-pc-shannon'] = ([r"**Théorème de Nyquist-Shannon.** Pas de repliement si $f_e>2f_{\max}$."],
  [r"Fréquence apparente : $|f-kf_e|$ ramenée dans $[0,f_e/2]$.", r"Effet stroboscopique : fréquence apparente négative = rotation à l'envers.", r"Filtre anti-repliement analogique avant l'échantillonneur."])
B['n-pc-fresnel'] = ([DEUXSRC, r"**Miroir plan.** L'image est le symétrique de l'objet ; deux symétries composent une rotation d'angle double."],
  [r"Se ramener à deux sources secondaires cohérentes.", r"Petit angle entre les miroirs ⇒ grand interfrange.", r"Lumière blanche : frange centrale blanche puis blanc d'ordre supérieur."])
B['n-pc-troisondes'] = ([r"**Superposition cohérente.** Les amplitudes complexes s'ajoutent.", r"**Somme géométrique.** $\big|\sum_{p<N}e^{ip\varphi}\big|^2=\frac{\sin^2(N\varphi/2)}{\sin^2(\varphi/2)}$."],
  [r"Factoriser par le terme central pour une somme symétrique.", r"Plus d'ondes : maxima principaux aux mêmes places, plus fins et plus intenses.", r"Pouvoir de résolution d'un réseau : $mN$."])
B['n-pc-cielbleu'] = ([r"**Électron élastiquement lié.** $m\ddot{\vec r}=-m\omega_0^2\vec r-e\vec E$.", r"**Rayonnement dipolaire.** $\mathcal P=\frac{\mu_0p_0^2\omega^4}{12\pi c}$, nul dans l'axe du dipôle."],
  [r"Loin de la résonance ($\omega\ll\omega_0$), le dipôle ne dépend pas de $\omega$ : $\mathcal P\propto\lambda^{-4}$.", r"Justifier l'approximation dipolaire : taille $\ll\lambda$, observation lointaine.", r"Polarisation à $90^\circ$ : le dipôle ne rayonne pas dans son axe."])
