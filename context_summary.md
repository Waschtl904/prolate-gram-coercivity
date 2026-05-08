# Context Summary — prolate-gram-coercivity

> Stand: Mai 2026 (aktualisiert). Vollständige Notation, alle Paper-Abhängigkeiten, offene Probleme.
> **Rolle dieses Dokuments:** Notations-Referenz und historischer Überblick für Papers I–XX.
> Für aktive Planung und offene Probleme: `RESEARCH_DIRECTIONS.md`.
> Für Session-Start-Kontext: `PROMPT.md`.
> **Papers I–XX berücksichtigt.**

---

## Überblick: Papers I–XX + Begleitnotizen

| Paper / Datei | Inhalt | Status |
|---|---|---|
| I — `paper1.tex` | Gram-Koerzivität, DSTP, Defektzerlegung | frozen |
| II — `paper2.tex` | Skalierungslimiten, Spurformel, Weil-Verbindung | frozen |
| II_quad — `paper2_quadrature.tex` | XRY-Quadratur, konditionaler Framework | frozen |
| III — `paper3.tex` | PSWF-Produkt Spektral-Tail-Schätzungen | frozen |
| IV — `paper4_semiclassical.tex` | Semiklassische Äquidistribution ψ_n² → ρ^cl | frozen |
| V — `paper5.tex` | WKB Cover, Bridge Lemma, Schur Control | frozen |
| VI — `paper6.tex` | Galerkin Norm, No-Go-Theorem, Layer 0–2 | frozen |
| VII — `paper7_skeleton.tex` | Dyadic Cancellation, H1–H3 Reduktion | frozen |
| VIII — `paper8_scale_separated.tex` | Skalen-separierte dyadische Auslöschung | frozen |
| IX — `paper9_superconcentration.tex` | Superkonzentration | frozen |
| X — `paper10_coercivity_gap.tex` | Koerzivitätslücke | frozen |
| XI — `paper11_fredholm_microlocal.tex` | Fredholm–mikrolokal | frozen |
| XII — `paper12_direct_coercivity.tex` | Direkte Koerzivität | frozen |
| XIII — `paper13_gap_s.tex` | Gap-S Lemma | frozen |
| XIV — `paper14_airy_resolvent.tex` | Airy-Resolvent | frozen |
| XV — `paper15_quasimode.tex` | Quasimode-Konstruktion | frozen |
| XVI — `paper16_bridge.tex` | Bridge Lemma (allgemein) | frozen |
| XVII — `paper17_cliff.tex` | Cliff-Schätzungen | frozen |
| XVIII — `paper18_airy_universality.tex` | BR3: qualitative Airy-Universalität | frozen |
| XIX — `paper19_quantitative_rate.tex` | Quantitative Zwei-Skalen-Rate | frozen |
| XX — `paper20_universality.tex` | Universalität und strukturelle Rigidität | **arXiv-ready** |
| `bridge_lemma.tex` | Bridge Lemma ausformuliert (für paper5.tex) | Einzufügend ✅ |
| `phase_nondeg_lemma.tex` | Phase Non-Degeneracy: α^(c) = π/2 + O(c^{-1/3}) | Bewiesen ✅ |
| `airy_discrete_stability_lemma.tex` | Prop. U(U') + ass:gap bedingungslos | Bewiesen ✅ |
| `ax5_independence_remark.tex` | DSTP logisch unabhängig von AX1–AX4 | Einzufügend ✅ |
| `section5_numerical_evidence.tex` | Numerische Evidenz Spektral-Tail | Einzufügend |

---

## Vollständige Notation: Papers I–VIII

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
| `α^(c)` | WKB-Phaseninkrement an s* — BEWIESEN: α^(c) = π/2 + O(c^{-1/3}) |
| `T_{ij}` | Galerkin-Matrixeinträge von DT_c^(N) |
| `P_{kl}` | Prefaktor: c·|λ_l-λ_k|/((1-λ_k)(1-λ_l)) |
| `B-strong` | Ass.: P_{kl} ≤ C₂ c^{1/2} — offen (früher Kontraktionsstrang) |
| `B_m(i)` | Dyadischer Block {j: 2^m ≤ \|i-j\| < 2^{m+1}} |
| `F_Ai(x)` | ∫_x^∞ Ai(t)² dt — Airy-Näherungsfunktion für λ_l |
| `x_l = (l-N_Sh)(c/2)^{-1/3}` | Skalierter Index (Airy-Skala) |
| `μ_l = χ_l / (2c^{4/3})` | Airy-Parameter (ORX Ch. 4) |
| `E_l(c) = λ_l - F_Ai(x_l)` | Airy-Verbindungsfehler (Eigenwertebene) |
| `S(c) = (log c/π)^{2/3}` | Landau-Widom-Skalenparameter |

## Notation: Trilogie XVIII–XX

| Symbol / Begriff | Bedeutung |
|---|---|
| $K_{B_c}$ | Bandlimitierter Kern (Paper XVIII) |
| $K_{\mathcal{A}_\gamma}$ | Airy-Typ-Kern in Klasse $\mathfrak{T}_\gamma$ |
| $\mathfrak{T}_\gamma$ | Operatorklasse mit Spektralwachstum $a_K \sim K^\gamma$ |
| $a_K$ | Spektralabstände / Turning-Point-Abstände |
| $\gamma$ | Spektralwachstumsexponent |
| $\beta$ | Turning-Point-Fensterexponent: Langer-Fehler $\sim c^{-\beta}$ |
| $A_K^{\rm lin}, A_K^{\rm quad}$ | Lineare / quadratische Interaktionsschicht (Paper XIX) |
| $C_{\rm lin} = O(K^{1+\gamma})$ | Amplitudenkoeffizient lineare Schicht |
| $C_{\rm quad} = O(K^{1+2\gamma})$ | Amplitudenkoeffizient quadratische Schicht |
| $K^*(c) \sim \frac{2\beta}{\alpha}\log c$ | Optimaler Truncation-Index |
| $\mathcal{M}(\mathrm{S1,S2,S3})$ | Methodklasse: S1 = Hüllenbedingung, S2 = Skalenstabilität, S3 = Diagonalsubstitution |
| $\mathfrak{R}: \mathcal{B} \to \mathcal{S}/\!\sim_{\mathcal{S}}$ | Realisierungsabbildung: Bounds → asymptotische Klassen |
| $\succ$ | Formale Ordnung auf $\mathcal{S}/\!\sim_{\mathcal{S}}$ |
| $\rho$ | Deformationsexponent: $A(K,\lambda c)/A(K,c) \to \lambda^\rho$ |
| `thm:universal_rate` | Hauptsatz: Rate $O(c^{-\beta}(\log c)^{1+\gamma})$ |
| `thm:rate_obstruction` | Obstruktionssatz: Rigidität innerhalb $\mathcal{M}$ |
| `lem:S2_knockdown` | S2-Knockdown: ohne S2 kollabiert Platzierung in $\mathcal{S}/\!\sim_{\mathcal{S}}$ |
| `def:realization_map` | Definition von $\mathfrak{R}$ |

---

## Bewiesene Resultate

### Papers I–IV (stabil, frozen)
- Gram-Koerzivität unter DSTP mit expliziten Schranken ✅
- Defektzerlegung $E_{mn} = R_{mn}^{\rm quad}$ ✅
- DSTP verifiziert für Zufalls- und Gauß-PSWF-Sampling ✅
- Kompaktheit normierter Gram-Operatoren im Skalierungslimes ✅
- Spurformel mit PNT-Konsistenz ✅
- Uniforme Off-diagonal-Schranke $\|(I-P_N)f_{mn}\| \leq CT^{1/2}$ ✅
- Schwache Konvergenz $\psi_n^2 \to \lambda_n \rho^{\rm cl}$, Rate $O(1/n)$ ✅

### Paper V — Bridge Lemma ✅
- ass:bulkconv **bewiesen für $\gamma < 1/2$** ✅
- $E_{\rm out}(f_{mn}) \leq C_\gamma \cdot e^{-\alpha_\gamma c}$ für alle $m,n \leq \gamma N_{\rm Sh}$ ✅
- Unconditional Bulk-Tail-Bound ✅

### Paper VI — No-Go + Layer 0 ✅
- No-Go-Theorem: nicht-oszillatorische Schur-Klasse gibt $\|T\| \geq \kappa/2 \cdot \log c$ ✅
- Obstruktion lokalisiert auf $|k-l| \lesssim c^{1/6}$ ✅

### Papers VII–VIII — Dyadic Cancellation ✅ (H1, H2 bedingungslos)
- Abstraktes Dyadic Cancellation Theorem vollständig ✅
- H1 Non-Degeneracy: $\alpha^{(c)} = \pi/2 + O(c^{-1/3})$ ✅
- H2 (Amplitude regularity): bedingungslos via ass:gap + Prop.U(U') ✅
- H3 (B-strong): offen

### Begleitnotizen ✅
- `phase_nondeg_lemma.tex`: Conj.\ 6.1 bewiesen, H1 bedingungslos ✅
- `airy_discrete_stability_lemma.tex`: Prop.\,U(U') + ass:gap bedingungslos ✅
- `ax5_independence_remark.tex`: DSTP $\perp$ AX1–AX4 ✅

### Trilogie XVIII–XX ✅
- BR3: $\|K_{B_c} - K_{\mathcal{A}}\|_{L^2} \to 0$ (Paper XVIII) ✅
- Quantitative Rate $O(c^{-1/3}(\log c)^{5/3})$ im Airy-Fall (Paper XIX) ✅
- Universelle Rate $O(c^{-\beta}(\log c)^{1+\gamma})$ für alle $\mathcal{A}_\gamma \in \mathfrak{T}_\gamma$ (Paper XX) ✅
- Obstruktionssatz: keine Methode in $\mathcal{M}(\mathrm{S1,S2,S3})$ schlägt diese Rate (Paper XX) ✅

---

## Offene Probleme

### Früher Kontraktionsstrang (Papers I–VIII)
- **B-strong** ($P_{kl} \leq C_2 c^{1/2}$): einzig verbleibende Lücke auf dem Weg zu $\|DT_c^{(N)}\| < 1$
- Landau-Widom Konjektur (globales erfc-Gesetz): numerisch gestützt, analytisch offen
- Bridge Lemma Extension $\gamma \geq 1/2$: offen
- Off-diagonal Assumption 3.1 (Kantenregime): offen
- XRY-Stabilitätskonjektur, Weil-Operator-Identifikation, DSTP für Primzahl-Sampling

### Gesamtprogramm (nach Paper XX)
Siehe `RESEARCH_DIRECTIONS.md` für vollständige Klassifikation:
- **O1**: H1-Minimalität / Envelope-Notwendigkeit innerhalb $\mathcal{M}$
- **O3a**: Rate außerhalb $\mathcal{M}(\mathrm{S1,S2,S3})$
- **Realisierungsproblem**: konkrete Operatorklassen mit $\rho \neq 0$
- **Stabilitätsproblem**: S2$^\epsilon$-Deformationen

---

## Archivierte Dokumente

| Datei | Inhalt | Warum archiviert |
|---|---|---|
| `assumption_2_4_target.md` | Beweisstrategie für ass:bulkconv | Superseded by Paper V |
| `PHASE_NONDEG_NOTE.md` | Historische Notiz Phase Non-Degeneracy | Superseded by `phase_nondeg_lemma.tex` |
| `REVIEW_NOTES_paper18.md` | Review-Notizen Paper XVIII | Archiv |

---

## Strategische Diagnose (Mai 2026)

### Früher Kontraktionsstrang
H1 ✅ (bedingungslos), H2 ✅ (bedingungslos). Einzige verbleibende Lücke: B-strong.
```
B-strong → H3 (Paper VII) → ‖DT_c^(N)‖ < 1 → Kontraktion → Assumption A
```

### Gesamtprogramm
Paper XX ist arXiv-ready. Das Programm ist nicht mehr durch eine einzige analytische Lücke
definiert, sondern durch klassifizierte offene Richtungen entlang parametrisierter Achsen.
Die interne Sprache (S1/S2/S3, $\mathfrak{R}$, $\rho$-Klassen) ist fixiert.
Jede weitere Arbeit ist Instanziierung, Reklassifikation oder Erweiterung der erlaubten Morphismengruppe.
