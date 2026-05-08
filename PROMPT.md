# Kontext: Mathematisches Forschungsprojekt — prolate-gram-coercivity

> **Verwendung:** Diesen Prompt am Anfang jedes neuen KI-Chats einfügen.
> Danach `RESEARCH_DIRECTIONS.md` und `DEPENDENCIES.md` aus diesem Repo laden —
> sie enthalten offene Probleme, Programmsprache und Paper-Abhängigkeiten.
> **Repo:** `github.com/Waschtl904/prolate-gram-coercivity`
> **Stand: Mai 2026** — Papers I–XX vorhanden; Paper XX arXiv-ready.

---

## Über mich

Ich bin Werkzeugbautechniker mit Berufsreifeprüfung (Maschinenbau),
lerne Programmieren und Mathematik im Selbststudium.
Ich arbeite freiwillig an einem mathematischen Forschungsprogramm
mit KI-Unterstützung (Perplexity + ChatGPT).
Autor aller Papers: Sebastian Schmalnauer, Wien.

---

## Das übergeordnete Ziel

Konstruktion eines spektralen Operators, dessen Eigenwerte die nichttrivialen
Nullstellen der Riemannschen Zetafunktion spiegeln (Hilbert-Pólya-Vermutung).
Ausgangspunkt: **CCM2025** = Connes–Consani–Moscovici, arXiv:2511.22755.
Kernmethode: PSWF-Konzentrationsoperator + Gram-Formenrahmen.

**Kein Paper in diesem Repo macht eine Behauptung über Nullstellen von ζ(s).**

---

## Programmstruktur (Papers I–XX)

| Paper | Datei | Inhalt | Status |
|---|---|---|---|
| I | `paper1.tex` | Gram-Koerzivität, Defektzerlegung, DSTP | frozen |
| II | `paper2.tex` | Skalierungslimiten, Spurformel, Weil-Verbindung | frozen |
| II-Q | `paper2_quadrature.tex` | Quadraturschätzungen | frozen |
| III | `paper3.tex` | Spektraler Tail, Off-diagonal | frozen |
| IV | `paper4_semiclassical.tex` | Semiklassische Äquidistribution | frozen |
| V | `paper5.tex` | WKB Cover, Bridge Lemma | frozen |
| VI | `paper6.tex` | No-Go-Theorem, Galerkin-Normen | frozen |
| VII | `paper7_skeleton.tex` | Dyadic Cancellation, H1 bedingungslos | frozen |
| VIII | `paper8_scale_separated.tex` | H2 bedingungslos | frozen |
| IX | `paper9_superconcentration.tex` | Superkonzentration | frozen |
| X | `paper10_coercivity_gap.tex` | Koerzivitätslücke | frozen |
| XI | `paper11_fredholm_microlocal.tex` | Fredholm–mikrolokal | frozen |
| XII | `paper12_direct_coercivity.tex` | Direkte Koerzivität | frozen |
| XIII | `paper13_gap_s.tex` | Gap-S Lemma | frozen |
| XIV | `paper14_airy_resolvent.tex` | Airy-Resolvent | frozen |
| XV | `paper15_quasimode.tex` | Quasimode-Konstruktion | frozen |
| XVI | `paper16_bridge.tex` | Bridge Lemma (allgemein) | frozen |
| XVII | `paper17_cliff.tex` | Cliff-Schätzungen | frozen |
| XVIII | `paper18_airy_universality.tex` | BR3: qualitative Airy-Universalität | frozen |
| XIX | `paper19_quantitative_rate.tex` | Quantitative Zwei-Skalen-Rate, $O(c^{-1/3}(\log c)^{5/3})$ | frozen |
| XX | `paper20_universality.tex` | Universalität und strukturelle Rigidität der Turning-Point-Truncation-Geometrie | **arXiv-ready** |

---

## Die Trilogie XVIII–XX: Kern des Programms

### XVIII — Qualitative Universalität
$\|K_{B_c} - K_{\mathcal{A}}\|_{L^2} \to 0$ (BR3) via Zwei-Skalen-Zerlegung.
Kein Rate-Ergebnis; iterierte Limesstruktur.

### XIX — Quantitative Zwei-Skalen-Rate
Zerlegung $A_K = A_K^{\rm lin} + A_K^{\rm quad}$;
$C_{\rm lin} = O(K^{5/3})$, $C_{\rm quad} = O(K^{7/3})$.
Optimale Truncation $K_{\rm opt} \sim (\log c)/(3\alpha)$:
Rate $O(c^{-1/3}(\log c)^{5/3})$.

### XX — Universelles Schicht-Selektionsprinzip
Für jedes $\mathcal{A}_\gamma \in \mathfrak{T}_\gamma$
(Spektralwachstum $a_K \sim K^\gamma$, Turning-Point-Fenster $c^{-\beta}$):
$$\|K_{B_c} - K_{\mathcal{A}_\gamma}\| = O\!\left(c^{-\beta}(\log c)^{1+\gamma}\right).$$
Strukturelle Rigidität: keine Methode in $\mathcal{M}(\mathrm{S1,S2,S3})$
erreicht $o(c^{-\beta}(\log c)^{1+\gamma})$.

---

## Aktuelle Programmsprache (Paper XX)

Diese Begriffe sind die interne Sprache des Programms ab Paper XX.
**Unbedingt verwenden, nicht paraphrasieren.**

| Symbol / Begriff | Bedeutung |
|---|---|
| $\mathfrak{T}_\gamma$ | Operatorklasse mit Spektralwachstum $a_K \sim K^\gamma$ |
| $\mathcal{M}(\mathrm{S1,S2,S3})$ | Methodklasse: S1 = Hüllenbedingung (H1), S2 = Skalenstabilität, S3 = Diagonalsubstitution |
| $\mathfrak{R}: \mathcal{B} \to \mathcal{S}/\!\sim_{\mathcal{S}}$ | Realisierungsabbildung: analytische Bounds → asymptotische Klassen |
| $K^*(c) \sim \frac{2\beta}{\alpha}\log c$ | Optimaler Truncation-Index (Balance-FOC) |
| $\succ$ | Formale Ordnung auf $\mathcal{S}/\!\sim_{\mathcal{S}}$ |
| $\rho$-Klassen | Deformationsklassen: $A(K,\lambda c)/A(K,c) \to \lambda^\rho$; Paper XX = $\rho = 0$ |
| S2 | Skalenstabilität: $\mathfrak{R} \circ \mathrm{Res}_\lambda = \mathfrak{R}$; EM ist eine Realisierung |
| S3 | Diagonalkompression: $j \mapsto K^*(c)$ projiziert globale Freiheitsgrade auf Log-Diagonale |
| `thm:universal_rate` | Hauptsatz: universelle Rate $O(c^{-\beta}(\log c)^{1+\gamma})$ |
| `thm:rate_obstruction` | Obstruktionssatz: Rigidität der Rate innerhalb $\mathcal{M}$ |
| `lem:S2_knockdown` | S2-Knockdown: ohne S2 kollabiert die Platzierung in $\mathcal{S}/\!\sim_{\mathcal{S}}$ |
| `def:realization_map` | Definition von $\mathfrak{R}$ |

---

## Offene Probleme

Vollständige Klassifikation in `RESEARCH_DIRECTIONS.md`.

**O1** — Notwendigkeit von H1 (Envelope-Minimalität):
Verbessert $f(j) = o(1)$ in der Eigenfunktionsschranke die Rate?
Kernfrage: was überlebt die S3-Diagonalprojektion $j \mapsto K^*(c)$?

**O3a** — Rate außerhalb $\mathcal{M}(\mathrm{S1,S2,S3})$:
Gibt es eine Methode außerhalb der Klasse mit $o(c^{-\beta}(\log c)^{1+\gamma})$?
Erfordert informationstheoretischen oder semiklassischen Zugang.

**Realisierungsproblem** — Welche Operatorklassen tragen $\rho \neq 0$?

**Stabilitätsproblem** — S2$^\epsilon$: Rate unter schwacher Verletzung von S2?

---

## Bitte beim Start jedes neuen Chats

1. Lies `RESEARCH_DIRECTIONS.md` — offene Probleme, Programmsprache, Horizonte
2. Lies `DEPENDENCIES.md` — Paper-Abhängigkeiten und Implikationskette
3. Für Paper XX: `paper20_universality.tex` und `paper20_context_prompt.md`
4. Für ältere Papers: `context_summary.md` und jeweilige `paper*.tex`
5. **Kein Claim über ζ(s)-Nullstellen** in keinem der Papers
6. **Paper XX ist arXiv-ready** — nicht als Draft behandeln
7. **Die Programmsprache aus der Tabelle oben verwenden** — nicht durch ältere Begriffe ersetzen
8. **`RESEARCH_DIRECTIONS.md` ist das aktive Planungsdokument** — nicht `context_summary.md`
9. `assumption_2_4_target.md`, `PHASE_NONDEG_NOTE.md`, `REVIEW_NOTES_paper18.md` — archiviert, nicht aktiv
