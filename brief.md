# Brief

Written before research begins. See the workspace docs (run `papers docs`):
research-pipeline.md §1.

> **Note 2026-06-07.** Seed is the origin chat (`chat.md`, gitignored): Levin's
> conjecture that psychological frustration is a high-scale geometric
> frustration, reframed — at the author's direction — away from a thematic
> "geometry of meaning" essay and toward a genealogy of geometry itself, in the
> register of Foucault's *Birth of the Clinic* and Nietzsche's *Birth of
> Tragedy*. Decisions fixed in discussion: genealogy **plus** a computational
> layer; subtitle *From Earth-Measure to the Spaces of Life and Mind*;
> frustration kept **minimal** (it surfaces only in the final stratum, as the
> physics fact, not a psychological centerpiece).

## Question

What is geometry, that the same word now governs land-survey, ideal figure,
curved space, transformation groups, phase portraits, biological form, semantic
embeddings, and morphogenetic problem-solving? Not "what do these have in
common" but the genealogical question: through what succession of regimes did
geometric reason pass, such that each made a new domain visible as a space — and
what is the stratum now forming, for which "geometry" (earth-measure) has become
a false name?

## Claim

The history of geometry is not a topic widening its applications. It is the
progressive abstraction of form from place and the progressive conversion of
becoming into navigable structure. Read stratigraphically — each stratum
remaining active beneath the next, not replaced — geometry passes from geodesy,
to Euclidean ideality, to coordinate capture, to the pluralization of space
(projective, non-Euclidean, Riemannian), to the transformation regime (Klein,
topology), to state-space (phase portraits, information geometry), to the
biological morphospace, to the semantic embedding, to Levin's problem-space.
*Morphotopy* names the stratum at which the object is no longer space but the
generation, deformation, and navigation of spaces of possible form. The
generative tension running the whole sequence is Apollonian form against
Dionysian becoming: geometry begins by fixing form; morphotopy begins when form
is understood as a trajectory. The one technical invariant carried across is
frustration — local satisfiability failing to compose globally,
$\min_x \sum_i E_i(x) > \sum_i \min_x E_i(x)$ — which the final stratum
generalizes from spin systems to any constrained navigable space. The paper does
**not** claim morphotopy solves consciousness (Chalmers' caution is kept): it may
formalize the structure of selfhood and reportability, not the existence of
experience.

## Kind

**genealogy that ships a computational layer.** Sets `has_simulation: true`,
`claims_target: results.json`. Two small models, parallel to the stratigraphy
model in `invention-of-the-person`:
1. a **dated stratigraphy** of the geometric strata (Euclid ~300 BCE → Descartes
   1637 → Riemann 1854 → Klein 1872 → … → Levin 2022 → morphotopy 2026): order,
   span, and the conceptual gaps, computed not asserted;
2. a **geometric-frustration** model (a small frustrated spin system) that
   exhibits the inequality above: ground-state degeneracy and a residual
   frustration index, demonstrating "local satisfaction does not imply global
   satisfaction" as a fact about geometry, not a metaphor.

## Cornerstone literature

The names the paper must engage; omissions that would make it not-yet-a-genealogy:

- **Method:** Foucault, *The Birth of the Clinic* (archaeology of perception);
  Nietzsche, *The Birth of Tragedy* (the generative opposition).
- **The strata (primary where possible):** Euclid, *Elements*; Descartes,
  *La Géométrie* (1637); Desargues/Poncelet (projective); Lobachevsky, Bolyai,
  Gauss (non-Euclidean); Riemann, *On the Hypotheses which Lie at the Foundations
  of Geometry* (1854); Klein, *Erlangen Program* (1872); Poincaré (*Analysis
  Situs*; phase space); Grothendieck (schemes, toposes — via a standard account,
  e.g. Caramello); Amari (information geometry).
- **Biological / cognitive / machine strata:** Raup (1966) and Mitteroecker &
  Huttegger (2009, the caution that morphospaces are not all Euclidean);
  Gärdenfors, *Conceptual Spaces: The Geometry of Thought* (2000); Landauer &
  Dumais (LSA, 1997); Mikolov et al. (word2vec, 2013); Levin (TAME, 2019/2022).
- **The technical hinge and the limit:** the geometrical-frustration /
  spin-ice literature (e.g. Ramirez, Bramwell); Chalmers (the hard problem).

Next-pass candidates (logged, not chased this pass): Cassirer on the concept of
space; Lautman/Châtelet on the philosophy of geometric thought; sheaf-theoretic
accounts of "space without points" beyond the one-paragraph Grothendieck note.
