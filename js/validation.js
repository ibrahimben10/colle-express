// Règles de validation partagées par les formulaires d'authentification.
// Elles sont volontairement strictes côté navigateur ; Supabase Auth refait
// sa propre validation côté serveur (format d'adresse, longueur du mot de passe).

const LOCAL = /^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*$/;
const LABEL = /^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$/;

/** Adresse e-mail au format utilisable : une seule @, partie locale et domaine valides, extension ≥ 2 lettres. */
export function emailValide(v) {
  const s = String(v ?? '').trim();
  if (s.length < 6 || s.length > 254) return false;
  const parts = s.split('@');
  if (parts.length !== 2) return false;
  const [local, domain] = parts;
  if (!local || local.length > 64 || !LOCAL.test(local)) return false;
  const labels = domain.split('.');
  if (labels.length < 2 || !labels.every(l => LABEL.test(l))) return false;
  return /^[A-Za-z]{2,63}$/.test(labels[labels.length - 1]);
}

export const PW_MIN = 8;
/** Mot de passe d'un nouveau compte ou d'une réinitialisation. Renvoie un message d'erreur, ou '' si valide. */
export function motDePasseErreur(pw) {
  const s = String(pw ?? '');
  if (s.length < PW_MIN) return `Le mot de passe doit contenir au moins ${PW_MIN} caractères.`;
  if (s.length > 72) return 'Le mot de passe ne doit pas dépasser 72 caractères.';
  if (!/[A-Za-zÀ-ÿ]/.test(s) || !/\d/.test(s)) return 'Utilisez au moins une lettre et un chiffre.';
  return '';
}
/** Force indicative de 0 à 4 (affichage uniquement). */
export function force(pw) {
  const s = String(pw ?? '');
  let f = 0;
  if (s.length >= PW_MIN) f++;
  if (s.length >= 12) f++;
  if (/[a-z]/.test(s) && /[A-Z]/.test(s)) f++;
  if (/\d/.test(s) && /[^A-Za-z0-9]/.test(s)) f++;
  return Math.min(4, f);
}
