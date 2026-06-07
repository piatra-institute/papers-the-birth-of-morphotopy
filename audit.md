# Audit

Dated log of editorial passes and verification runs. Newest first.
See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-06-07 (figures + sim depth) — embed the figures, make the computation load-bearing

User: the simulation figures were not in the paper; is the sim finished; can it be
improved. Answers: figures were generated but unembedded (no workspace paper embeds
figures); the sim was complete but minimal; yes it can be improved. Scope chosen:
deepen both models (no spin-ice tetrahedron this pass).

- **First embedded figures in the workspace.** Both PNGs now appear in §8 via
  `![caption](../simulation/output/figures/x.png){width=..}`; the build resolves the
  relative path through `pandoc --resource-path <paper_dir>` with no change to
  `build.py`. Pandoc auto-numbers them Figure 1 (stratigraphy) and Figure 2
  (frustration); verified by rendering the PDF pages (images present, 4 image
  XObjects).
- **Frustration model deepened** (`analyses.py`): added `_triangular_ground`, a
  periodic triangular-lattice antiferromagnet enumerated exactly at N = 9, 12, 16.
  Frustrated-bond fraction is exactly 1/3 at every size; ground-state degeneracy is
  extensive (6 → 42 → 68); residual entropy per spin (0.5973 → 0.2336) scatters
  around Wannier's (1950) exact thermodynamic 0.3231 — the single triangle shown to
  be the seed of a macroscopic fact. (Honest framing: small tori scatter, they do
  not smoothly converge.)
- **Stratigraphy model deepened**: acceleration made quantitative — median emergence
  year 1895; mean inter-stratum interval 1146 yr (pre-1829) vs 18 yr (post), a 64×
  contraction.
- **Figures redrawn** to publication quality: stratigraphy timeline with a
  cumulative-count inset (flat → vertical) and the 64× annotation; frustration with
  spin cartoons (the one red unsatisfied bond on the triangle) + the lattice-scaling
  panel.
- Added Wannier (1950) reference (41 entries). Claims-gate kept clean: the new
  decimals (0.3231, 0.2336, 0.5973) are all `results.json` keys; acceleration stats
  are integers.

Verification: voice 0 errors; refs OK, 0 missing; claims 0 unmatched (49 sim values,
8 prose decimals all matched); build clean, **17 → 18 pages**, figures render, zero
missing-character warnings; check => PASS. Still `status: draft`; not committed.

## 2026-06-07 (depth) — real chapters: subsectioned, monograph-leaning

User: the content was thin (3 paragraphs per chapter), wanted structure and power,
no thesis repetition, every phrase earning its stay. Chosen scope: monograph-leaning,
depth spread **evenly across all strata**, text only (no third simulation; §8 numbers
unchanged).

Restructured every chapter into `###` subsections, each a unit of verified specific
content (depth through specificity, not rhetoric):
- §2 administered earth (harpedonaptai 3-4-5; Rhind 8/9-diameter circle; Plimpton 322
  base-60 triples) + Euclid's architecture and the fifth postulate as hostage.
- §3 Descartes' unit length; the parallel postulate breaking (Saccheri 1733 →
  Lobachevsky/Bolyai/Gauss → **Beltrami 1868** relative consistency by models); Riemann's
  $ds^2$ and Gauss's Theorema Egregium; Einstein, matter-as-source.
- §4 Klein's group hierarchy (projective ⊃ affine ⊃ Euclidean) + Lie; Euler $V-E+F=2-2g$,
  genus, Poincaré homology; GDL's symmetry→architecture map.
- §5 phase space (Liouville, Poincaré recurrence); information geometry (Fisher metric,
  KL-not-a-metric, natural gradient); topos / space without points.
- §6 Raup's W/D/T/S cube and the empty regions (McGhee); Gärdenfors convexity + colour;
  LSA→Bengio→word2vec analogy + limits; trace→mechanism (RSA, Gurnee–Tegmark, Othello,
  Engels, **Nanda's circle → Kantamneni helix**, Platonic); Levin planaria + Durant 2017.
- §7 the five conditions, now with worked pass/fail cases; what-it-is-not; frustration
  (ice rules, the inequality); music orbifold / BHV tree space / persistent homology.
- §8 split into dating + frustration, with the limits of each model stated.
- §9 predictions-and-how-it-could-fail (the test as falsifiable core); the Chalmers bound.

Bibliography 34 → **40** (added Saccheri 1733, Beltrami 1868, Gauss 1828, McGhee 1999,
Nanda et al. 2023, Durant et al. 2017; all locators verified this session).

Discipline held: no thesis refrain (the through-line stated once per stratum as that
stratum's specific gain); kept new numerals as integers/fractions/years so the claims
gate stays clean (no stray decimals leaked).

Verification: voice 0 errors (8 developed-contrast warns); refs OK, 0 missing (40 bib
entries); claims 0 unmatched; build clean, **9 → 17 pages**, zero missing-character
warnings (accents render). check => PASS. Still `status: draft`; not committed/pushed.

## 2026-06-07 (rewrite) — scientific pass: de-scaffold, de-slop, sharpen, deepen the bibliography

User directives, in order: (1) drop Foucault/Nietzsche — they were chat framing,
the paper must stand on its own and quote relevant primary sources; (2) no PIATRA
paper may cite another; (3) massively improve the bibliography; (4) massively
de-slop the prose; (5) make the point sharper and more scientific ("Nature-level").
Recorded as standing rules in memory (paper-quality-standards).

Changes (a near-total prose rewrite, section structure kept):
- **De-scaffolded.** Removed every Foucault/Nietzsche reference and the
  Apollonian/Dionysian labels; the method (strata as regimes of visibility) and the
  engine (figure-held-fixed vs transformation) are now stated on the paper's own
  terms. Removed the "(PIATRA, 2026)" companion cross-reference and bib entry.
- **Sharpened the point.** §7 now states the contribution as a falsifiable-in-parts
  historical claim plus a **five-condition test** for when a treatment is morphotopic
  rather than a decorative "geometry of X" (space; licensed metric; transformations;
  constraints; navigation), and positions morphotopy explicitly against geometric
  deep learning / representational geometry / conceptual spaces / TAME. §9 states the
  limits plainly (organizational, not new mathematics; the Chalmers bound).
- **De-slopped.** Cut sweeping closers, anaphora, and most negate-pivots; denser,
  declarative sentences. Voice warns fell 8 → 5.
- **Bibliography deepened** to 34 entries: real primaries/translations (Euclid–Heath
  1956; Riemann via Clifford 1873; Klein with the Haskell 1893 translation noted and
  quoted; Amari & Nagaoka 2000; Pauling 1935; Bengio 2003) and serious secondaries
  (Gray 2008; Torretti 1978; Kriegeskorte, Mur & Bandettini 2008). Quotes Klein
  ("not altered by the transformations of the group") and Riemann ("multiply extended
  magnitude") directly. New locators verified against publisher/arXiv records.

Pitfall handled: the inline "trans. Haskell, 1893" parsed as a separate citation
(MISSING); folded the translation into the Klein 1872 bib entry and cite Klein by
his own date. No simulation change; §8 numbers unchanged.

Verification: voice 0 errors (5 developed-contrast warns); refs OK, 0 missing (34
bib entries; narrative citations show "unused" by the advisory humanities detector,
all hand-confirmed cited); claims 0 unmatched; build clean, **9 pages** (denser than
the 11-pp prior draft despite the larger bibliography), zero missing-character
warnings; check => PASS. Still `status: draft`; not committed/pushed.

## 2026-06-07 (later) — the geometrize-the-non-geometric family

Prompted by the user pointing at Kantamneni & Tegmark, *Language Models Use
Trigonometry to Do Addition* (arXiv:2502.00873; read in full), asking why it was
absent and "what else geometrizes something that does not look like geometry."
Researched outward (locators verified against arXiv/publisher records). Scope
chosen: mechanistic turn + the Erlangen loop + a generality paragraph; the helix
is cited textually (no third simulation), so `simulation/` and §8 numbers are
unchanged.

Added (10 references):
- §3 — Einstein (1916): gravitation as curvature, the long-delayed payoff of
  Riemann's intrinsic manifold (a real prior omission).
- §4 — Bronstein et al. (2021), "Geometric Deep Learning: the Erlangen Programme
  of ML": Klein's §4 stratum returns as the design principle of the latest
  stratum's machines. The loop-closer.
- §6 — the empirical turn from "geometry as trace" to "geometry as mechanism,"
  causally verified: Gurnee & Tegmark (2023, space/time), Li et al. (2023,
  Othello-GPT board model), Engels et al. (2024, circular features), Kantamneni &
  Tegmark (2025, the helix/Clock centerpiece), Huh et al. (2024, Platonic
  convergence).
- §7 — one paragraph showing the movement is general: Tymoczko (2006, chord
  orbifolds), Billera–Holmes–Vogtmann (2001, CAT(0) tree space), Carlsson (2009,
  persistent homology), plus Einstein.
- Abstract gained one clause (machine geometry as mechanism, not metaphor).

Pitfalls handled: kept model sizes out of prose as bare numbers (claims would
read "6.9B" as a stray decimal); reworded the Bronstein citation from the
four-author form (the non-ASCII "Veličković" adjacent to the year made the refs
parser key it "Erlangen 2021") to "Bronstein and colleagues (2021)".

Verification: voice 0 errors (same 8 developed-contrast warns, no new ones); refs
OK, 0 missing (30 bib entries; narrative citations show "unused" by the advisory
humanities detector, all hand-confirmed cited); claims 0 unmatched; build clean,
**9 → 11 pages**, zero missing-character warnings (accented German/French/Czech
names render); check => PASS. Still `status: draft`; not committed/pushed.

## 2026-06-07 — initial build (genealogy + computation)

First full pass, from the origin chat (`chat.md`) through to a built draft.
Decisions taken in discussion and recorded in `brief.md`: a genealogy of
geometric reason in the Foucault/Nietzsche register (not a "geometry of meaning"
essay); subtitle *From Earth-Measure to the Spaces of Life and Mind*; ships a
computational layer; frustration kept minimal (final stratum only, as the physics
fact, not a psychological centerpiece).

Built:
- `paper/PAPER.md` — 9 sections: the fossil in the name (method: Foucault's
  conditions of visibility, Nietzsche's form/becoming tension) → earth/ideal
  figure → capture & pluralization (Descartes, projective, non-Euclidean,
  Riemann) → transformation regime (Klein, topology) → becoming becomes geometric
  (phase space, information geometry, topos) → spaces of life and mind
  (morphospace, conceptual spaces, embeddings, Levin) → the birth of morphotopy
  (+ the frustration inequality) → §8 modelled → §9 the Chalmers caution + close.
- `simulation/` — two exact analyses (no seed): dated stratigraphy of 16 strata
  (span 3,826 yr; largest gap 1,937 yr Euclid→Descartes; 12 of 16 strata in the
  final 197 yr) and a geometric-frustration enumeration (triangle frustrated:
  global min −1 above summed local −3, degeneracy 6, one-third bonds frustrated;
  square control: unfrustrated, degeneracy 2). Every §8 number is a key in
  `output/results.json`.
- `brief.md`, `research.md`, `sources.md` filled; metadata set (`has_simulation:
  true`, `claims_target: results.json`, title/header).

Research: focused verification, not a broad fan-out (canonical history). Locators
verified against publisher records for Levin TAME (**corrected 2019 → 2022**, vol
16, 768201), Raup 1966, Mitteroecker & Huttegger 2009, Bramwell & Gingras 2001.
Added Desargues 1639, Lobachevsky 1829, Gibbs 1902 to the bibliography (cited in
prose, were missing).

Verification: voice 0 errors (8 warns, all developed contrasts in the genealogy
register — Foucault's point §1, the stratum's core claim §5, the
instrument-not-ontology caution §6 — kept per protocol); refs OK, 0 missing
(humanities author-year detection leaves narrative citations "unused"; all 20 bib
entries hand-verified as cited); claims 0 unmatched (6 prose decimals all trace to
results.json); build clean, 9 pages, zero missing-character warnings; check =>
PASS.

Status left `draft` (off the README index, off the web) pending author review and
the publish decision. Not yet committed/pushed; no GitHub repo created yet.

<!--
## YYYY-MM-DD — <pass name>
Scope: <the bounded list of changes>
Changes:
  - ...
Verification:
  - voice: <errors / warns>
  - refs: <missing / unused>
  - claims: <reconciliation result>
  - build: <pages, missing-char warnings>
  - check => PASS/FAIL
-->
