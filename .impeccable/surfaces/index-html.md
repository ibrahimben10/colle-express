---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

Scope: the whole signed-in app shell and its main surfaces (exercise list and exercise page, fiches, colleur virtuel, profil, communauté, groupes). Mode: Operate (fiches and corrections read in Read mode inside it).

Audience and job: prépa students (MPSI/MP) searching an oral-style exercise on paper, asking graduated hints, then reading the correction; as much on phone as on desktop.

## Direction contract

THESIS: Colle Express is the student's copie double: you search on squared paper with a blue pen, the corrector answers in red in the margin. It refuses the grey Apple-clone dashboard with one blue accent and icon-only navigation.

OWN-WORLD: bright paper ground (not cream) with a faint blue Seyès grid only in work zones; graphite ink text; Bic-blue ink for actions and links; correcting red for hints, correction, marks and errors; a pink-red margin rule at page scale beside the work column; subject colours as notebook dividers (maths blue, physique orange, chimie teal, info green). Headings in Latin Modern Roman (the face of every sujet de concours, matching MathJax), UI in the system sans, red-pen annotations in a handwriting face, used sparingly. Dark: night-blue paper, the same inks brightened.

STORY: the student sees where they are in their copy (filière, matière, chapitre), opens an exercise, works, asks a hint written in red, reads a correction annotated in the margin, and sees their progress as marked copies.

FIRST VIEWPORT: top bar with wordmark and text navigation (Exercices, Fiches, Colle, Groupes, Carnet, Communauté) plus avatar and theme; a filter line (filière segmented control, matière dividers, chapter, search); the exercise list as ruled rows on paper with duration and level in tabular columns; on desktop the selected exercise sits on a Seyès sheet to the right of the margin rule. Phone: same order, bottom tab bar, one column.

FORM: code-led; candidate 2 of 7 on the grounded list (user chose the pick over the assigned colloscope); seed:a3e72191ffd23d7f. Signature interaction: the red-pen stroke, an underline or circle drawn as a correction step or hint is revealed; motion grammar: short ease-out fades and lifts (under 250 ms), press feedback at scale .97, reduced-motion = opacity only.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
