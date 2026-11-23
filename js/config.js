// =====================================================================
//  Configuration du site — à compléter (voir README, étape 3)
// =====================================================================
export const CONFIG = {
  // Supabase > Project Settings > API : « Project URL » et clé « anon public »
  SUPABASE_URL: 'https://ubvtigfxptkiioykhexh.supabase.co',
  SUPABASE_ANON_KEY: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVidnRpZ2Z4cHRraWlveWtoZXhoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTUzOTU3NDAsImV4cCI6MjExMDk3MTc0MH0.0VtDSrmOkksC20c-McUSqm7GQSy6BT31__UDBPxFJdI',

  // Affichage
  NOM_PROF: 'BEN YAKHLEF IBRAHIM',
  NOM_SITE: 'Colle express',
  SOUS_TITRE: 'Classes préparatoires MP · Maths & Physique-Chimie',

  // Présentation « À propos » (page de connexion + onglet À propos) — modifie librement ces textes.
  PRESENTATION: {
    initiales: 'IB',
    accroche: 'Élève ingénieur à l’ENSEEIHT (Toulouse INP), passé par la prépa MP.',
    texte: [
      'Je m’appelle Ibrahim Ben Yakhlef. Je suis aujourd’hui élève ingénieur à l’ENSEEIHT, l’école d’ingénieurs de Toulouse INP, après deux années de classes préparatoires scientifiques en filière MP.',
      'J’ai créé Colle express pour vous faire travailler comme en colle : des exercices courts et ciblés, des indices progressifs plutôt que la solution toute faite, et un corrigé détaillé une fois que vous avez vraiment cherché. C’est la méthode qui m’a le plus fait progresser pendant ma prépa.',
    ],
    // Parcours, du plus récent au plus ancien : modifie les années et les intitulés.
    parcours: [
      {quand: 'Aujourd’hui', quoi: 'Élève ingénieur à l’ENSEEIHT', ou: 'Toulouse INP', ic: 'cap'},
      {quand: 'Concours', quoi: 'Admission en école d’ingénieurs', ou: 'Concours des grandes écoles', ic: 'trophy'},
      {quand: 'Prépa', quoi: 'Classes préparatoires MPSI puis MP', ou: 'Maths, physique-chimie, colles hebdomadaires', ic: 'book'},
      {quand: 'Lycée', quoi: 'Baccalauréat, spécialités maths et physique-chimie', ou: '', ic: 'star'},
    ],
    pourquoi: [
      'Des énoncés de type oral, classés par niveau : CCINP, Mines-Centrale, X-ENS.',
      'Une correction de ta copie par photo, avec des indices plutôt que la réponse.',
      'Un suivi personnel pour savoir quoi retravailler.',
    ],
    contact: '',   // facultatif : e-mail ou lien LinkedIn, ex. 'ibrahim.benyakhlef@etu.toulouse-inp.fr'
  },
};
// Tant que SUPABASE_URL est vide, le site fonctionne en « mode démonstration »
// (données enregistrées dans le navigateur, pas de correction par l'IA).
