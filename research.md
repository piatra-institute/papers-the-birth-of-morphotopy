# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2.
T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only).
A claim that reaches the paper rests on a T1 or T2 source.

## Findings

### Method (stated on the paper's own terms — 2026-06-07 rewrite)
The paper no longer scaffolds on or cites Foucault and Nietzsche; those were the
user's chat framing for the *kind* of paper, not material to import (a standing
rule — see paper-quality-standards). The method is now stated directly: strata as
regimes of what can be made visible, driven by the tension between the figure held
fixed and the transformation that deforms it. The history is grounded in the
mathematics' own historians instead:
- [T2] Gray (2008), *Plato's Ghost* — the 19th-century pluralization/abstraction as
  mathematical modernism. §3.
- [T2] Torretti (1978), *Philosophy of Geometry from Riemann to Poincaré* — the
  Riemann→Poincaré arc, consistency-over-intuition. §3.

### The geometric strata (primary where reachable)
- [T1] Euclid, *Elements* (~300 BCE) — figure abstracted from matter into proof. §2.
- [T1] Descartes, *La Géométrie* (1637, appendix to *Discours de la méthode*) — curve
  becomes equation; the coordinate capture of form. §3.
- [T1] Riemann, *Über die Hypothesen, welche der Geometrie zu Grunde liegen*
  (Habilitationsvortrag delivered 1854; published posthumously 1868) — space made
  intrinsic: manifold, metric, curvature, "multiply extended magnitude." §3. Date is
  high-error: deliver 1854, print 1868 — cite both.
- [T1] Klein, *Vergleichende Betrachtungen über neuere geometrische Forschungen*
  (Erlangen Program, 1872) — geometry = the study of invariants under a transformation
  group. The decisive mutation. §4. Verified 1872.
- [T1] Poincaré, *Analysis Situs* (1895, J. de l'École Polytechnique) — topology as
  continuity/connectedness beneath measurement; also the phase-space imagination. §4/§5.
- [T2] Mac Lane & Moerdijk, *Sheaves in Geometry and Logic* (1992) — Grothendieck
  toposes as "generalized spaces," space reconstructed from local/relational data.
  Used for the §5 "space without points" aside (kept brief; primary Grothendieck SGA
  not read this pass — logged next-pass).
- [T2] Amari, *Information Geometry and Its Applications* (2016, Springer) — families of
  probability distributions as Riemannian manifolds (Fisher metric); uncertainty given
  shape. §5.

### Biology, cognition, machine (the new terrains)
- [T1] Raup (1966), "Geometric analysis of shell coiling: general problems," *J.
  Paleontology* 40(5):1178–1190 — the founding morphospace: organisms occupy a space
  of *possible* forms. §6. Verified locator.
- [T2] Mitteroecker & Huttegger (2009), "The concept of morphospaces…," *Biological
  Theory* 4(1):54–67 — the load-bearing caution: morphospaces are not all Euclidean;
  distance/direction are not always licensed. Keeps §6 honest. Verified locator.
- [T1] Gärdenfors, *Conceptual Spaces: The Geometry of Thought* (2000, MIT Press) —
  concepts as convex regions over quality dimensions; meaning given geometric structure. §6.
- [T1] Landauer & Dumais (1997), "A solution to Plato's problem…" *Psychological Review*
  104(2):211–240 — LSA: meaning as high-dimensional co-occurrence structure. §6.
- [T1] Mikolov, Chen, Corrado & Dean (2013), "Efficient estimation of word
  representations in vector space," arXiv:1301.3781 — word2vec; meaning operationalized
  as scalable vector geometry. §6. The careful reading: embeddings show meaning leaves a
  geometric *trace*, they do not prove meaning *is* geometry.
- [T1] Levin (2022), "Technological Approach to Mind Everywhere (TAME)…," *Frontiers in
  Systems Neuroscience* 16:768201 (arXiv:2201.10346) — cognition as navigation of
  problem-spaces (anatomical, physiological, transcriptional, behavioral); stress/
  frustration placed on one cross-scale continuum. §6/§7. **Year corrected: 2022, not
  2019.**

### The technical hinge and the limit
- [T1] Bramwell & Gingras (2001), "Spin ice state in frustrated magnetic pyrochlore
  materials," *Science* 294(5546):1495–1501 — canonical geometrical frustration:
  geometry prevents all pairwise interactions being satisfied at once; macroscopically
  degenerate ground state (Pauling ice-entropy analogy). Grounds §7 + the frustration
  simulation. The general form: local satisfiability does not compose to global.
- [T1] Chalmers (1995), "Facing up to the problem of consciousness," *J. Consciousness
  Studies* 2(3):200–219 — the hard problem: structural/functional explanation does not
  reach why there is experience. The §9 caution; bounds the overclaim.

### The geometrize-the-non-geometric family (added 2026-06-07)
Prompted by the user pointing at the helix paper ("why not include this? what else?").
The family splits three ways.

- **The mechanistic turn in interpretability (§6).** Not "meaning leaves a geometric
  trace" but "the geometry is the computation," shown by causal intervention:
  - [T1] Kantamneni & Tegmark (2025), arXiv:2502.00873 — integers on a generalized
    helix (linear + Fourier windings T = [2,5,10,100]); addition by rotating the a,b
    helices into the a+b helix (the "Clock" algorithm), confirmed by activation
    patching across GPT-J, Pythia, Llama. Centerpiece. Read in full.
  - [T1] Gurnee & Tegmark (2023), arXiv:2310.02207 — linear space/time
    representations, place/time neurons (Llama-2 family).
  - [T1] Engels, Liao, Michaud, Gurnee & Tegmark (2024), arXiv:2405.14860 — circular
    multi-dimensional features (days/months) for modular arithmetic.
  - [T1] Li, Hopkins, Bau, Viégas, Pfister & Wattenberg (2023, ICLR), arXiv:2210.13382
    — Othello-GPT's interventionally-confirmed internal board geometry.
  - [T1] Huh, Cheung, Wang & Isola (2024, ICML), arXiv:2405.07987 — the Platonic
    Representation Hypothesis: cross-model/-modality convergence to a shared geometry.
- **The Erlangen loop-closer (§4).** [T1] Bronstein, Bruna, Cohen & Veličković (2021),
  arXiv:2104.13478 — "Geometric Deep Learning: the Erlangen Programme of ML";
  architectures classified by the symmetry group they respect. Klein's §4 stratum
  returns as the design principle of the latest stratum's machines.
- **The pattern recurs outside ML (§7 generality).**
  - [T1] Einstein (1916), *Annalen der Physik* 354(7):769–822 — gravitation as
    curvature; the long-delayed payoff of Riemann's §3 intrinsic manifold.
  - [T1] Tymoczko (2006), *Science* 313(5783):72–74 — musical chords as points in a
    non-Euclidean orbifold. Locator verified.
  - [T1] Billera, Holmes & Vogtmann (2001), *Adv. Appl. Math.* 27(4):733–767 —
    phylogenetic tree space as a CAT(0) metric space with unique geodesics.
  - [T2] Carlsson (2009), *Bull. AMS* 46(2):255–308 — persistent homology / topology
    of data.

## Fact-check notes
- Levin TAME year: chat used 2019; the TAME paper is 2022 (vol 16, 768201). Corrected everywhere.
- Riemann: deliver 1854 / publish 1868 — the stratigraphy model dates it 1854 (the event).
- Klein Erlangen: 1872 confirmed.
- Raup, Mitteroecker–Huttegger, Bramwell–Gingras locators verified against publisher records.

## Next-pass (logged, not chased)
Cassirer (*Substance and Function* / concept of space); Châtelet (*Les enjeux du mobile*);
primary Grothendieck (SGA/toposes) beyond the Mac Lane–Moerdijk secondary; Gauss/Bolyai/
Lobachevsky primaries for the non-Euclidean stratum (currently carried by Riemann + standard
history).
