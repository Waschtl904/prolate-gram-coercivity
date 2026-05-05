# Kontext: Mathematisches Forschungsprojekt — Prolate–Weil Program

> **Verwendung:** Diesen Prompt am Anfang jedes neuen KI-Chats einfügen.
> Danach `context_summary.md` aus diesem Repo laden lassen — sie enthält
> die vollständige Notation, alle Paper-Abhängigkeiten und offenen Probleme.
> **Repo:** `github.com/Waschtl904/prolate-gram-coercivity`
> **Stand: Mai 2026** — Papers I–VIII + alle Begleitnotizen vorhanden.

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
Kernmethode: PSWF-Konzentrationsoperator + Gram-Formenrahmen.

**Kein Paper in diesem Repo macht eine Behauptung über Nullstellen von ζ(s).**

---

## Die zwei GitHub-Repos

### Repo 1 — Großes Vorprojekt (17 Papers)
**github.com/Waschtl904/prolate-primes-paper**

Historische Entwicklung des Programms. Enthält Paper XIII (Gap-S) als
langfristiges Ziel. `context_summary.md` dort für den Repo-1-Kontext.

### Repo 2 — Sauberer Neuaufbau (publikationsreif) — DIESES REPO
**github.com/Waschtl904/prolate-gram-coercivity**

Rigoros, selbstenthaltend. Acht Papers + vier Begleitnotizen:

| File | Inhalt | Status |
|---|---|---|
| `paper1.tex` | Gram-Koerzivität, Defektzerlegung, DSTP | Near publication-ready |
| `paper2.tex` | Skalierungslimiten, Spurformel, Weil-Verbindung | Near publication-ready |
| `paper2_quadrature.tex` | XRY-Quadratur, konditionaler Implication-Framework | Reinschrift |
| `paper3.tex` | PSWF-Produkt-Spektral-Tail-Schätzungen | Reinschrift |
| `paper4_semiclassical.tex` | Semiklassische Äquidistribution der PSWF-Dichten | Vollständig bewiesen |
| `paper5.tex` | WKB Cover, Schur Control, Bridge Lemma | **Vollständig bewiesen** |
| `paper6.tex` | Galerkin Norm Estimates, No-Go-Theorem, Layer 0–2 | **Publikationsreif** |
| `paper7_skeleton.tex` | Dyadic Cancellation, H1 bedingungslos, Reduktion auf B-strong | **H1 bedingungslos** |
| `paper8_scale_separated.tex` | Skalen-separierte dyadische Auslöschung, H2 bedingungslos | Submission-ready (bedingt) |
| `phase_nondeg_lemma.tex` | Phase Non-Degeneracy: α^(c) = π/2 + O(c^{-1/3}) | **Bewiesen** ✅ |
| `airy_discrete_stability_lemma.tex` | Prop. U(U') + ass:gap bedingungslos | **Bewiesen** ✅ |
| `bridge_lemma.tex` | Bridge Lemma ausformuliert (einzufügen in paper5.tex) | Einzufügend ✅ |
| `ax5_independence_remark.tex` | DSTP logisch unabhängig von AX1–AX4 (einzufügen in paper1.tex) | Einzufügend ✅ |
| `section5_numerical_evidence.tex` | Numerische Evidenz Spektral-Tail (einzufügen in paper2_quadrature.tex) | Einzufügend |

---

## Logische Implikationskette

```
Paper I  (Gram-Koerzivität, DSTP-Axiom)
  ↓
Paper II  (Skalierungslimiten, Spurformel, Weil-Verbindung)
  ↓
Paper II_quad  (Implikation: Konj.(i)+(ii) → DSTP für XRY)
  ↓
Paper III  (Bulk-Tail-Bound, Off-diagonal, Kantenobstruktion)
  ↓
Paper IV  (Semiklassische Äquidistribution ψ_n² → ρ^cl, O(1/n))
  ↓
Paper V  (Bridge Lemma: ass:bulkconv BEWIESEN für γ < 1/2)
  ↓
Paper VI  (No-Go: nicht-oszillatorische Schur-Klasse provably insufficient)
  ↓
Paper VII  (Dyadic Cancellation: H1 BEDINGUNGSLOS, Reduktion auf H2+H3)
  ↓
Paper VIII  (H2 BEDINGUNGSLOS via ass:gap + Prop.U(U'))
  ↓
[B-strong → H3 → ‖DT_c^(N)‖ < 1 → Kontraktion → Assumption A]
```

---

## Aktueller Stand (Mai 2026, vollständig aktualisiert)

### Was unbedingt bewiesen ist
- Gram-Koerzivität unter DSTP mit expliziten Schranken (Paper I) ✅
- Exakte Defektzerlegung E_{mn} = R_{mn}^quad (Paper I) ✅
- DSTP verifiziert für Zufalls- und Gauß-PSWF-Sampling (Paper I) ✅
- DSTP logisch unabhängig von AX1–AX4 — konstruktiver Zeuge (ax5_independence_remark.tex) ✅
- Kompaktheit normierter Gram-Operatoren im Skalierungslimes (Paper II) ✅
- Spurformel mit PNT-Konsistenz (Paper II) ✅
- Uniforme Off-diagonal-Schranke ‖(I-P_N)f_{mn}‖ ≤ CT^{1/2} (Paper III) ✅
- Schwache Konvergenz ψ_n² → λ_n ρ^cl, Rate O(1/n) (Paper IV) ✅
- **ass:bulkconv für γ < 1/2 BEWIESEN** (Paper V, Bridge Lemma) ✅
- Unconditional Bulk-Tail-Bound ‖(I-P_N)f_{mn}‖ ≤ Ce^{-αN} für γ < 1/2 ✅
- No-Go-Theorem: nicht-oszillatorische Schur-Klasse gibt ‖T‖ ≥ κ/2 · log c (Paper VI) ✅
- Abstrakte Dyadic Cancellation unter H1–H3 (Paper VII, Appendix) ✅
- **H1 Non-Degeneracy: α^(c) = π/2 + O(c^{-1/3}) BEWIESEN** (phase_nondeg_lemma.tex) ✅
  → dist(α^(c), {0,π}) ≥ π/4 für alle c ≥ c_0(A) ✅
  → Conj. 6.1 aus Paper VI bewiesen ✅
  → Paper VII gilt bedingungslos für H1 ✅
- **Proposition U(U') BEWIESEN** (airy_discrete_stability_lemma.tex) ✅
  → Lemma U: |λ_l - F_Ai(x_l)| ≤ C₁ c^{-2/3} ✅
  → Lemma U': |(λ_l-λ_{l+1}) - (F_Ai(x_l)-F_Ai(x_{l+1}))| ≤ C₂ c^{-2/3} (sogar O(c^{-5/3})) ✅
- **ass:gap BEWIESEN**: λ_l - λ_{l+1} ≥ κ_0(c/2)^{-1/3} mit κ_0 = c_min/2 ✅
- **H2 (Amplitude regularity) BEDINGUNGSLOS**: ass:gap → Lemma F → Kor.C(a); Prop.U' → Lemma A → Kor.C(b) ✅
- Dyadisches Trennungsprinzip (Lemma F, Paper VIII) bedingungslos ✅
- Skalen-Kürzung in Kor.C, Term 1: (c/2)^{-1/3} kürzt sich exakt aus ✅

### Was noch offen ist
- **B-strong** (`P_{kl} ≤ C₂ c^{1/2}`) — **einzig verbleibende Hauptlücke für Kontraktion**
  → erfordert WKB/Airy-Matching an s*, eigenes Paper-Level-Problem
- **Landau-Widom Konjektur** (globales erfc-Gesetz): λ_l ≈ (1/2) erfc(Z_l) — analytisch offen
- **β(c) → β(∞)**: Limes des Zentrierungsparameters — numerisch β(∞) ∈ [-0.30, -0.21]
- Bridge Lemma Extension zu γ ≥ 1/2 — offen
- Off-diagonal Assumption 3.1 (Kantenregime) — Paper III
- Weil-Operator-Identifikation G_∞ (Paper II)
- XRY-Stabilitätskonjektur (Paper II_quad)
- DSTP für Primzahl-Sampling (Paper I)

### Strategische Priorität (Mai 2026)
**Einziger verbleibender Angriffspunkt: B-strong.**
Alle anderen Hypothesen H1, H2 sind bedingungslos bewiesen.
B-strong → H3 → ‖DT_c^(N)‖ < 1 → vollständige Theorie.

---

## Zentrale Notation (Kurzreferenz)

| Symbol | Bedeutung |
|---|---|
| `ψ_n^(c)` | PSWF auf [-T,T] mit Bandbreite ω, Zeitbandbreite c = ωT |
| `λ_n(c)` | Slepian-Konzentrations-Eigenwert |
| `χ_n(c)` | Sturm-Liouville-Eigenwert von D_c: χ_n ~ n(n+1) + c²/2 |
| `K_N(x,y)` | Christoffel-Darboux-Kern: ∑_{n=0}^{N-1} ψ_n(x) ψ_n(y) |
| `P_N` | Orthogonalprojektor auf span{ψ_0,...,ψ_{N-1}} in L²([-T,T]) |
| `G^(N)_{p,c}` | Gram-Matrix der PSWF-Quadratur |
| `DSTP` | Discrete Spectral Transfer Property — zentrales Axiom (Paper I) |
| `f_{mn}` | Produktfunktion: ψ_m^(c) · ψ_n^(c) |
| `N_Sh = 2c/π` | Shannon-Zahl |
| `s* = 1-c^{-2/3}` | Übergangspunkt (transition point), Paper VI/VII |
| `α^(c)` | WKB-Phaseninkrement an s* — **BEWIESEN: π/2 + O(c^{-1/3})** |
| `T_{ij}` | Galerkin-Matrixeinträge von DT_c^(N) (Paper VI/VII) |
| `B-strong` | Ass.: P_{kl} ≤ C₂ c^{1/2} — **einzig verbleibende Lücke** |
| `F_Ai(x)` | ∫_x^∞ Ai(t)² dt — Airy-Näherungsfunktion für λ_l |
| `x_l = (l-N_Sh)(c/2)^{-1/3}` | Skalierter Index (Airy-Skala) |
| `S(c) = (log c/π)^{2/3}` | Landau-Widom-Skalenparameter |

---

## Bitte beim Start jedes neuen Chats

1. Lies `context_summary.md` aus **diesem Repo** (prolate-gram-coercivity)
2. Lies die relevante `paper*.tex` je nach Thema des Gesprächs
3. Für Abhängigkeiten und offene Probleme: `DEPENDENCIES.md`
4. **Kein Claim über ζ(s)-Nullstellen** in keinem der Papers
5. **ass:bulkconv ist NICHT mehr offen** — bewiesen in Paper V
6. **Phase Non-Degeneracy ist NICHT mehr offen** — bewiesen in `phase_nondeg_lemma.tex`
7. **ass:gap + Prop.U(U') sind NICHT mehr offen** — bewiesen in `airy_discrete_stability_lemma.tex`
8. **H1 und H2 (Paper VII/VIII) sind BEDINGUNGSLOS** — einzig offene Lücke ist B-strong (H3)
9. **assumption_2_4_target.md ist archiviert** — nicht als aktives Dokument benutzen
10. **PHASE_NONDEG_NOTE.md** falls vorhanden: historisch, überholt durch `phase_nondeg_lemma.tex`
