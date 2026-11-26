---
titre: Transferts thermiques
---
## L'essentiel

La conduction thermique transporte de l'énergie des zones chaudes vers les zones froides. Elle est décrite par la loi de Fourier ; un bilan local donne l'**équation de la chaleur**.

> **Loi de Fourier.** $\vec j_{th} = -\lambda\,\overrightarrow{\mathrm{grad}}\,T$, avec $\lambda$ la conductivité thermique (W·m⁻¹·K⁻¹).

## Bilan d'énergie local

[[fig:mp-diffusion-1]]

Sur une tranche de section $S$ et d'épaisseur $\mathrm dx$, sans source :
$$\rho c\,\frac{\partial T}{\partial t} = -\frac{\partial j_{th}}{\partial x}\quad\Rightarrow\quad \frac{\partial T}{\partial t} = D\,\frac{\partial^2T}{\partial x^2},\qquad D = \frac{\lambda}{\rho c}.$$

Temps caractéristique de diffusion sur une longueur $L$ : $\tau \approx L^2/D$.

## Régime stationnaire et résistance thermique

[[fig:mp-diffusion-2]]

En régime stationnaire sans source, le flux $\Phi$ est conservé et le profil est affine dans un mur homogène.

> **Formule — Résistance thermique.** $T_1 - T_2 = R_{th}\,\Phi$, avec $R_{th} = \dfrac{e}{\lambda S}$ pour un mur d'épaisseur $e$.

Comme en électricité, les résistances en série s'ajoutent, et les conductances en parallèle s'ajoutent.

## Conducto-convection

[[fig:mp-diffusion-3]]

> **Loi de Newton.** $\Phi = hS\,(T_p - T_{\text{ext}})$, soit une résistance $\dfrac{1}{hS}$.

## Ordres de grandeur

| Matériau | $\lambda$ (W·m⁻¹·K⁻¹) |
|---|---|
| cuivre | 400 |
| verre, béton | 1 |
| air immobile, laine de verre | 0,03 |

## Exemple corrigé

**Énoncé.** Un mur de béton ($\lambda = 1$ W·m⁻¹·K⁻¹) de 20 cm et de 10 m² sépare une pièce à 20 °C de l'extérieur à 0 °C. Calculer les pertes, puis l'effet d'une couche de 5 cm de laine de verre ($\lambda = 0{,}04$).

**Solution.**
1. $R_{\text{béton}} = \dfrac{e}{\lambda S} = \dfrac{0{,}2}{1\times10} = 0{,}02$ K·W⁻¹, d'où $\Phi = \Delta T/R = 1000$ W.
2. $R_{\text{laine}} = \dfrac{0{,}05}{0{,}04\times10} = 0{,}125$ K·W⁻¹, en série : $R = 0{,}145$ K·W⁻¹.
3. $\Phi \approx 138$ W : les pertes sont divisées par plus de 7.

## Pièges classiques

- L'analogie électrique ne vaut qu'en régime stationnaire.
- Le temps de diffusion varie comme le **carré** de la longueur.
