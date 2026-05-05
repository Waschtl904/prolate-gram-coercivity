# Context Summary — prolate-gram-coercivity

> Stand: Mai 2026 (aktualisiert). Vollständige Notation, alle Paper-Abhängigkeiten, offene Probleme.
> Für neuen KI-Chat: dieses Dokument + relevante paper*.tex lesen.
> **Papers I–VIII + alle Begleitnotizen berücksichtigt.**

---

## Überblick: Papers I–VIII + Begleitnotizen

| Paper / Datei | Inhalt | Status |
|---|---|---|
| I — `paper1.tex` | Gram-Koerzivität, DSTP, Defektzerlegung | Near publication-ready |
| II — `paper2.tex` | Skalierungslimiten, Spurformel, Weil-Verbindung | Near publication-ready |
| II_quad — `paper2_quadrature.tex` | XRY-Quadratur, konditionaler Framework | Reinschrift |
| III — `paper3.tex` | PSWF-Produkt Spektral-Tail-Schätzungen | Reinschrift |
| IV — `paper4_semiclassical.tex` | Semiklassische Äquidistribution ψ_n² → ρ^cl | Vollständig bewiesen |
| V — `paper5.tex` | WKB Cover, Bridge Lemma, Schur Control | **Vollständig bewiesen** |
| VI — `paper6.tex` | Galerkin Norm, No-Go-Theorem, Layer 0–2 | **Publikationsreif** |
| VII — `paper7_skeleton.tex` | Dyadic Cancellation, H1–H3 Reduktion | **H1 bedingungslos** |
| VIII — `paper8_scale_separated.tex` | Skalen-separierte dyadische Auslöschung | Submission-ready (bedingt) |
| `bridge_lemma.tex` | Bridge Lemma ausformuliert (für paper5.tex) | Einzufügend ✅ |
| `phase_nondeg_lemma.tex` | Phase Non-Degeneracy: α^(c) = π/2 + O(c^{-1/3}) | **Bewiesen** ✅ |
| `airy_discrete_stability_lemma.tex` | Prop. U(U') + ass:gap bedingungslos | **Bewiesen** ✅ |
| `ax5_independence_remark.tex` | DSTP logisch unabhängig von AX1–AX4 (Riemann-Zeuge) | Einzufügend ✅ |
| `section5_numerical_evidence.tex` | Numerische Evidenz Spektral-Tail (für paper2_quadrature.tex) | Einzufügend |

---

## Vollständige Notation

| Symbol | Bedeutung |
|---|---|
| `ψ_n^(c)` | PSWF auf [-T,T], Bandbreite ω, c = ωT |
| `λ_n(c)` | Slepian-Konzentrations-Eigenwert |
| `χ_n(c)` | SL-Eigenwert von D_c: χ_n ~ n(n+1) + c²/2 |
| `K_N(x,y)` | Christoffel-Darboux-Kern |
| `P_N` | Projektor auf span{ψ_0,...,ψ_{N-1}} |
| `G^(N)_{p,c}` | Gram-Matrix PSWF-Quadratur |
| `DSTP` | Discrete Spectral Transfer Property (Paper I) |
| `f_{mn}` | Produktfunktion ψ_m · ψ_n |
| `μ_{mn}` | χ_m + χ_n |
| `E_{mn}[χ_k]` | Spektralmittelwert von D_c in Zustand f_{mn} |
| `ρ^cl(x)` | Klassische Gleichgewichtsdichte |
| `θ_n(x)` | Prüfer-Phase von ψ_n (Paper IV) |
| `r_n(x)` | Prüfer-Amplitude (Paper IV) |
| `r_n^WKB(x)` | WKB-Referenzamplitude (Paper IV) |
| `N_Sh = 2c/π` | Shannon-Zahl |
| `x_+(n)` | Klassischer Wendepunkt von ψ_n |
| `I_δ` | Bulk-Subintervall [-(1-δ)T, (1-δ)T] |
| `E_out(f_{mn})` | Out-of-band Spektralenergie von f_{mn} (Paper V) |
| `s* = 1-c^{-2/3}` | Übergangspunkt (Paper VI/VII) |
| `α^(c)` | WKB-Phaseninkrement an s* — **BEWIESEN: α^(c) = π/2 + O(c^{-1/3})** |
| `T_{ij}` | Galerkin-Matrixeinträge von DT_c^(N) |
| `P_{kl}` | Prefaktor: c·|λ_l-λ_k|/((1-λ_k)(1-λ_l)) |
| `B-strong` | Ass.: P_{kl} ≤ C₂ c^{1/2} — **einzig verbleibende Hauptlücke** |
| `B_m(i)` | Dyadischer Block {j: 2^m ≤ |i-j| < 2^{m+1}} |
| `F_Ai(x)` | ∫_x^∞ Ai(t)² dt — Airy-Näherungsfunktion für λ_l |
| `x_l = (l-N_Sh)(c/2)^{-1/3}` | Skalierter Index (Airy-Skala) |
| `μ_l = χ_l / (2c^{4/3})` | Airy-Parameter (ORX Ch. 4) |
| `E_l(c) = λ_l - F_Ai(x_l)` | Airy-Verbindungsfehler (Eigenwertebene) |
| `S(c) = (log c/π)^{2/3}` | Landau-Widom-Skalenparameter |

---

## Bewiesene Resultate (Mai 2026, vollständig aktualisiert)

### Papers I–IV (stabil)
- Gram-Koerzivität unter DSTP mit expliziten Schranken ✅
- Defektzerlegung E_{mn} = R_{mn}^quad ✅
- DSTP verifiziert für Zufalls- und Gauß-PSWF-Sampling ✅
- Kompaktheit normierter Gram-Operatoren im Skalierungslimes ✅
- Spurformel mit PNT-Konsistenz ✅
- Uniforme Off-diagonal-Schranke ‖(I-P_N)f_{mn}‖ ≤ CT^{1/2} (Paper III) ✅
- Schwache Konvergenz ψ_n² → λ_n ρ^cl, Rate O(1/n) (Paper IV) ✅

### Paper V — Bridge Lemma ✅
- ass:bulkconv **BEWIESEN für γ < 1/2** (Bridge Lemma, Theorem 4.1) ✅
- E_out(f_{mn}) ≤ C_γ · e^{-α_γ c} für alle m,n ≤ γ N_Sh ✅
- Mechanismus: geometrische Abdeckung beider WKB-verbotener Zonen (scharf bei γ = 1/2) ✅
- Unconditional Bulk-Tail-Bound ‖(I-P_N)f_{mn}‖ ≤ Ce^{-α'N} für γ < 1/2 ✅

### Paper VI — No-Go + Layer 0 ✅
- No-Go-Theorem: nicht-oszillatorische Schur-Klasse gibt ‖T‖ ≥ κ/2 · log c — optimal ✅
- Konsequenz: Kontraktion erfordert zwingend oszillatorische Cancellation ✅
- Obstruktion lokalisiert auf |k-l| ≲ c^{1/6} ✅

### Paper VII — Dyadic Cancellation ✅ (H1 jetzt bedingungslos)
- Abstraktes Dyadic Cancellation Theorem vollständig bewiesen ✅
- **H1 Summabilitätsbedingung**: ∑ ε_m^(N) = o(1) ✅
- **H1 Non-Degeneracy**: α^(c) = π/2 + O(c^{-1/3}) — **BEWIESEN** via `phase_nondeg_lemma.tex` ✅
- H2, H3: siehe Paper VIII und B-strong unten

### Paper VIII — Skalen-separierte dyadische Auslöschung ✅/⚠️
- Dyadisches Trennungsprinzip (Lemma F): |λ_i - λ_j| ≥ κ_0 (c/2)^{-1/3} |i-j| ✅
- Korollar C: H2 im dyadischen Sinne unter ass:gap + Prop.U(U') ✅
- **ass:gap BEWIESEN** via `airy_discrete_stability_lemma.tex` ✅
- **Proposition U(U') BEWIESEN** via `airy_discrete_stability_lemma.tex` ✅
- Lemma F, Korollar C(a) und (b): **alle bedingungslos** ✅
- Drei-Skalen-Struktur: kombinatorisch (c^{-1/3}), lokal (Airy), global (Landau-Widom) dokumentiert ✅
- Konjektur ULW (globales erfc-Gesetz): numerisch gestützt, analytisch offen

### Begleitnotizen (neue Resultate)
- **`phase_nondeg_lemma.tex`**: α^(c) = π/2 + O(c^{-1/3}) gleichmäßig in k ≤ N — **Conj. 6.1 aus Paper VI bewiesen** ✅
  - Mechanismus: Bohr-Sommerfeld-Halbinkrement + T_k-Auslöschung (Langer-Transformation)
  - dist(α^(c), {0,π}) ≥ π/4 für alle c ≥ c_0(A) ✅
- **`airy_discrete_stability_lemma.tex`**: Prop. U(U') + ass:gap **bedingungslos bewiesen** ✅
  - Lemma U: |λ_l - F_Ai(x_l)| ≤ C₁ c^{-2/3} (aus ORX)
  - Lemma U': |(λ_l - λ_{l+1}) - (F_Ai(x_l) - F_Ai(x_{l+1}))| ≤ C₂ c^{-2/3} (neu, sogar O(c^{-5/3}))
  - ass:gap mit κ_0 = c_min/2 bedingungslos ✅
- **`ax5_independence_remark.tex`**: DSTP logisch unabhängig von AX1–AX4 (Riemann-Zeuge) ✅

---

## Offene Probleme (priorisiert, aktualisiert)

### 🔥 Priorität 1 — B-strong
**Gap:** P_{kl} ≤ C₂ c^{1/2} ist nicht bewiesen.
**Status:** Einzig verbleibende Hauptlücke auf dem Weg zur Kontraktion.
**Warum schwer:** Zwei konkrete Failure-Modes (Paper VI, Remark 5.2):
- Nicht-uniforme stationäre Phase in der Transition Zone
- Korrelierte Airy-Faktoren (Eigenwert-Spacing und Amplitude nicht unabhängig)
**Route:** WKB/Airy-Matching an s*, Modellproblem formulieren — eigenes Paper-Level-Problem.

### 🔶 Priorität 2 — Landau-Widom Konjektur (global)
**Gap:** λ_l ≈ (1/2) erfc(Z_l) mit S(c) = (log c/π)^{2/3} — kein analytischer Beweis.
**Status:** Numerisch gestützt (Residuen ≈ 2.7·10^{-2} für c ∈ {50,100,200}, abnehmend).
**Teilproblem:** β(c) → β(∞) unbekannt; numerisch β(∞) ∈ [-0.30, -0.21].

### 🔶 Priorität 3 — Bridge Lemma Extension γ ≥ 1/2
**Gap:** Geometrische Überdeckung bricht für γ ≥ 1/2 zusammen.
**Route:** Stationäre Phase / Integrationsaufteilung — offen.

### 🔵 Mittelfristig
- Dominante Eigenvektordelokalisierung (Paper VI, OP 5)
- Off-diagonal Assumption 3.1 (Kantenregime) — Paper III
- XRY-Stabilitätskonjektur — Paper II_quad
- Weil-Operator-Identifikation — Paper II
- DSTP für Primzahl-Sampling — Paper I

---

## Archivierte Dokumente

| Datei | Inhalt | Warum archiviert |
|---|---|---|
| `assumption_2_4_target.md` | Beweisstrategie für ass:bulkconv (Varianten A/B/C) | Superseded by Paper V (Bridge Lemma) |

---

## Strategische Diagnose (Mai 2026, aktualisiert)

**Phase Non-Degeneracy ist gelöst** — H1 von Paper VII gilt bedingungslos.
**ass:gap und Prop. U(U') sind gelöst** — Lemma F und Korollar C von Paper VIII gelten bedingungslos.

Das Programm hängt jetzt an einem einzigen Scharnier: **B-strong** (`P_{kl} ≤ C₂ c^{1/2}`).

Implikationskette zum Ziel:
```
B-strong → H3 (Paper VII) → ‖DT_c^(N)‖ ≤ C c^{-1/2} log c < 1
         → Kontraktion → Fixpunkt → Assumption A → Vollständige Theorie
```

H1 ✅ (bedingungslos), H2 ✅ (via ass:gap + Prop.U(U'), bedingungslos),
H3 ⚠️ (unter B-strong — einzig verbleibend).
