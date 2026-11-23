// MathJax 4 : police New Computer Modern (rendu identique à LaTeX) et retour à la ligne
// automatique des formules trop longues pour l'écran (téléphone).
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']], displayMath: [['$$', '$$'], ['\\[', '\\]']]},
  output: {font: 'mathjax-newcm', displayOverflow: 'linebreak', linebreaks: {inline: true, width: '100%'}},
  options: {menuOptions: {settings: {enrich: false, speech: false, braille: false}}},
  startup: {typeset: false},
};
