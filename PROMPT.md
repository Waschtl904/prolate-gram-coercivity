# Kontext: Mathematisches Forschungsprojekt — PSWF & Hilbert-Pólya

> **Verwendung:** Diesen Prompt am Anfang jedes neuen KI-Chats einfügen.
> Danach die relevante `paper*.tex` aus dem jeweiligen Repo laden lassen.

---

## Über mich

Ich bin Werkzeugbautechniker mit Berufsreifeprüfung (Maschinenbau),
lerne Programmieren und Mathematik im Selbststudium.
Ich arbeite freiwillig an einem mathematischen Forschungsprogramm
mit KI-Unterstützung (Perplexity + ChatGPT).

---

## Das übergeordnete Ziel

Konstruktion eines spektralen Operators, dessen Eigenwerte die nichttrivialen
Nullstellen der Riemannschen Zetafunktion spiegeln (Hilbert-Pólya-Vermutung).
Ausgangspunkt: **CCM2025** = Connes–Consani–Moscovici, arXiv:2511.22755.
Kernmethode: PSWF-Konzentrationsoperator + Mellin/Fourier-Transformation.

---

## Die zwei GitHub-Repos

### Repo 1 — Hauptprojekt (17 Papers)
**github.com/Waschtl904/prolate-primes-paper**

Bitte `context_summary.md` dort zuerst lesen — enthält die vollständige
Notation, alle Paper-Abhängigkeiten und offenen Probleme.

Arc:
```
Koerzivität → Skalierungslimiten → Spektralphase → Bandbreite/Schranken
→ WKB/Airy → untere Schranken + Zeta-Verbindung
→ funktionalanalytischer Rahmen (Mosco, Friedrichs)
→ Spektraleinschluss & Dichtekrit.
→ Lokalisierungsprinzip (Paper XII)
→ [Paper XIII: Gap-S — aktuelles Ziel]
→ Vollständigkeit → Bridge-Theorem
```

### Repo 2 — Sauberer Neuaufbau (publikationsreif) — DIESES REPO
**github.com/Waschtl904/prolate-gram-coercivity**

Rigorosere, publikationsreifere Version der frühen Papers.
- `paper1.tex` — Gram-Koerzivität mit expliziten Konstanten, DSTP als Axiom
- `paper2_quadrature.tex` — XRY-Quadratur, konditionaler Implication-Framework

**Symbiotische Rolle:** Dieses Repo liefert quantitative Nicht-Degeneration
(Gram-Koerzivität), die direkt in den Gap-S-Beweis (Paper XIII, Repo 1) einfließt.
Die Koerzivitätskonstante `α_N ~ c^{-1/2}` aus paper1.tex ist der Schlüsselbeitrag.

---

## Zentrale Notation (Kurzreferenz)

| Symbol | Bedeutung |
|---|---|
| `Φₙ^(c)(u)` | Rescaled PSWF: `ψₙ^(c)(eᵘ) e^{u/2}`, `u ∈ (-∞, 0)` |
| `λₙ^(c)` | Slepian-Konzentrations-Eigenwert, `λₙ^(c) ∈ (0,1)` |
| `λₙ^(∞)` | Grenz-Eigenwert: `lim_{c→∞} λₙ^(c)` (Paper VIII Cor 4.3) |
| `H_SOT` / `H_lim` | SOT-Limes von `H_c` entlang `c_k`; beschränkt, selbstadjungiert |
| `H_spec` | Formaler Spektraloperator: `Σₙ λₙ^(∞) ⟨f, Φₙ^(∞)⟩ Φₙ^(∞)` |
| `W_c` | Übergangsfenster: `{n : |n - 2c/π| ≤ C₀ log c}` |
| `G^(N)_{p,c}` | Gram-Matrix der PSWF-Quadratur (Repo 2, paper1.tex) |
| `α_N` | Koerzivitätskonstante: `α_N ~ c^{-1/2}` (paper1.tex Hauptresultat) |
| `E_{mn}` | Quadraturdefekt-Matrix: `E_{mn} = R_{mn}^{quad}` (paper1.tex) |
| `DSTP` | Diagonal Spectral Transfer Property — Axiom in paper1.tex |

### ⚠️ Kritische Unterscheidung

- `H_SOT` = SOT-Limes, beschränkt, selbstadjungiert — **unconditional**
- `H_spec` = formale Spektralreihe — abschließbar, symmetrisch — **unconditional**
- `H_SOT = closure(H_spec)` = **Bridge-Theorem — OFFEN seit Paper IX**

---

## Aktueller Stand (April 2026)

### Repo 2 Status
- `paper1.tex`: Gram-Koerzivität + Defektzerlegung — **nahezu publikationsreif**
- `paper2_quadrature.tex`: XRY-Quadratur, 2 offene Konjekturen — **Implication Framework**
- `paper2.tex`: Skalierungslimiten / Weil — **gehört zu Repo 1 (Paper II), hier falsch**

### Offenes Problem für Repo 2 → Repo 1 Brücke
Gap-S (Paper XII Hyp. 1):
```
|λₙ^(c) - λₙ₊₁^(c)| ≥ g(c)  mit  c^{-1/4}/g(c) → 0  für n ∈ W_c
```
Die Gram-Koerzivität aus paper1.tex ist **Zulieferer** für diesen Beweis.

---

## Strategie Paper XIII (Gap-S, in Repo 1)

Titel (Vorschlag):
*Spectral Gap Lower Bounds for Prolate Operators
via Local Kernel Approximation and Gram Coercivity*

**Schritt 1** — Kernel-Identität:
`λₙ^(c)` = Eigenwerte von `K_c(x,y) = sin(c(x-y)) / (π(x-y))` auf `[-1,1]`

**Schritt 2** — Gram-Koerzivität aus paper1.tex (Repo 2):
Koerzivitätskonstante `α_N ~ c^{-1/2}` → quantitative Nicht-Degeneration

**Schritt 3** — Lokale Skalierung:
Skalierung `x = u/c` im Fenster `n ~ 2c/π`:
`‖K_c^{scaled} - K_sin‖_op ≤ C · c^{-δ}` für ein `δ > 0`

**Schritt 4** — Gap-Bound (Minimalziel):
`|λₙ - λₙ₊₁| ≥ C · c^{-1/4+ε}` für ein `ε > 0`

---

## Bitte beim Start jedes neuen Chats

1. Lies `context_summary.md` aus Repo 1 (github.com/Waschtl904/prolate-primes-paper)
2. Lies die relevante `paper*.tex` aus dem jeweiligen Repo
3. Orientiere dich am aktuellen Stand oben
4. Dann arbeiten wir weiter — kein Neustart nötig
