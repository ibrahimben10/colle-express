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

  // Adresse qui reçoit les sujets d'oraux envoyés par les élèves (formulaire « Enrichir la plateforme »).
  // Au premier envoi, FormSubmit envoie un e-mail d'activation à cette adresse : clique sur « Activate Form ».
  ENVOI_EMAIL: 'ibrahimben930@gmail.com',

  // Présentation « À propos » (page de connexion + onglet À propos) — modifie librement ces textes.
  PRESENTATION: {
    initiales: 'IB',
    accroche: 'Élève ingénieur en 1re année à l’ENSEEIHT (Sciences du Numérique), Toulouse.',
    texte: [
      'Je m’appelle Ibrahim Ben Yakhlef. Je suis élève ingénieur en première année à l’ENSEEIHT, à Toulouse, dans le département Sciences du Numérique, après deux années de classes préparatoires MPSI puis MP au lycée Omar Ibn Abdelaziz.',
      'J’ai créé Colle express pour vous faire travailler comme en colle : des exercices courts et ciblés, des indices progressifs plutôt que la solution toute faite, et un corrigé détaillé une fois que vous avez vraiment cherché. C’est la méthode qui m’a le plus fait progresser pendant ma prépa.',
    ],
    // Parcours, du plus récent au plus ancien.
    parcours: [
      {quand: 'Aujourd’hui', quoi: 'ENSEEIHT — 1re année, Sciences du Numérique', ou: 'Informatique, logique formelle, mathématiques appliquées, signal et image, allemand LV2', ic: 'cap'},
      {quand: 'CPGE — 2e année', quoi: 'Classe préparatoire MP', ou: 'Lycée Omar Ibn Abdelaziz', ic: 'book'},
      {quand: 'CPGE — 1re année', quoi: 'Classe préparatoire MPSI', ou: 'Lycée Omar Ibn Abdelaziz', ic: 'sigma'},
    ],
    pourquoi: [
      'Des énoncés de type oral, classés par niveau : CCINP, Mines-Centrale, X-ENS.',
      'Une correction de ta copie par photo, avec des indices plutôt que la réponse.',
      'Un suivi personnel pour savoir quoi retravailler.',
    ],
    email: 'ibrahimben930@gmail.com',
    telephone: '+33 7 53 14 48 54',
  },
};
// Tant que SUPABASE_URL est vide, le site fonctionne en « mode démonstration »
// (données enregistrées dans le navigateur, pas de correction par l'IA).
