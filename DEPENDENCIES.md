# DEPENDENCIES — prolate-gram-coercivity

> Stand: Mai 2026 (aktualisiert). Papers I–VIII + alle Begleitnotizen berücksichtigt.

---

## Implikationskette

```
Paper I  (Gram-Koerzivität, DSTP)
  ↓  liefert: Koerzivität, Defektzerlegung, DSTP-Verifikation
Paper II  (Skalierungslimiten, Spurformel, Weil)
  ↓  liefert: Kompaktheit, Spurformel, PNT-Konsistenz
Paper II_quad  (XRY-Quadratur, konditionaler Framework)
  ↓  bedingt: Konj.(i)+(ii) → DSTP für XRY
Paper III  (Bulk-Tail, Off-diagonal, Kantenobstruktion)
  ←  INPUT: Paper IV (Äquidistribution), Paper V (Bridge Lemma)
  ↓  liefert (unbedingt für γ<1/2): ‖(I-P_N)f_{mn}‖ ≤ Ce^{-αN}
Paper IV  (Semiklassische Äquidistribution)
  ↓  liefert: H1-Input für Paper III + Prüfer-Amplituden für Paper V
              + χ_l-Abstandsformel für airy_discrete_stability_lemma
Paper V  (WKB Cover, Bridge Lemma, Schur Control)
  ↓  BEWIESEN: ass:bulkconv (Assumption 2.4) für γ < 1/2
Paper VI  (Galerkin Norm, No-Go-Theorem, Layer 0–2)
  ↓  liefert: Methodenbarriere (Schur-Klasse tot)
             Layer-0 Geometrie der Obstruktion
             Conj. 6.1 (Phase Non-Degeneracy) — BEWIESEN via Begleitnotiz
Paper VII  (Dyadic Cancellation, Reduktion)
  ↓  liefert: Abstraktes Cancellation-Theorem unter H1–H3 (vollständig)
              H1 BEDINGUNGSLOS (phase_nondeg_lemma.tex)
              Reduktion auf B-strong (H3) + [H2 via Paper VIII]
Paper VIII  (Skalen-separierte Auslöschung)
  ↓  liefert: H2 bedingungslos (ass:gap + Prop.U(U') beide bewiesen)
              Dyadisches Trennungsprinzip (Lemma F) bedingungslos
              Drei-Skalen-Struktur: kombinatorisch / lokal / global

Begleitnotizen:
  phase_nondeg_lemma.tex              → H1 Non-Degeneracy (Paper VII) bedingungslos ✅
  airy_discrete_stability_lemma.tex   → ass:gap + Prop.U(U') (Paper VIII) bedingungslos ✅
  bridge_lemma.tex                    → Bridge Lemma (für paper5.tex, einzufügend) ✅
  ax5_independence_remark.tex         → DSTP ⊥ AX1-AX4 (für paper1.tex, einzufügend) ✅
```

---

## Status aller Assumptions und Conjectures

| ID | Beschreibung | Status | In Paper / Datei |
|---|---|---|---|
| ass:bulkconv (Ass. 2.4) | E_out(f_{mn}) ≤ Ce^{-αc} für γ<1/2 | ✅ **BEWIESEN** (Bridge Lemma) | Paper V |
| ass:gap | Uniform Gap Condition: λ_l - λ_{l+1} ≥ κ_0(c/2)^{-1/3} | ✅ **BEWIESEN** | `airy_discrete_stability_lemma.tex` → Paper VIII |
| Prop. U | \|λ_l - F_Ai(x_l)\| ≤ C₁ c^{-2/3} | ✅ **BEWIESEN** (aus ORX) | `airy_discrete_stability_lemma.tex` |
| Prop. U' | \|(λ_l-λ_{l+1}) - (F_Ai(x_l)-F_Ai(x_{l+1}))\| ≤ C₂ c^{-2/3} | ✅ **BEWIESEN** (sogar O(c^{-5/3})) | `airy_discrete_stability_lemma.tex` |
| Conj. 6.1 (phase) | dist(α^(c),{0,π}) ≥ π/4 | ✅ **BEWIESEN**: α^(c) = π/2 + O(c^{-1/3}) | `phase_nondeg_lemma.tex` |
| H1 (Paper VII) | Phase summability + Non-Degeneracy | ✅ **BEDINGUNGSLOS** | Paper VII + `phase_nondeg_lemma.tex` |
| H2 (Paper VII) | Amplitude regularity auf dyadischen Blöcken | ✅ **BEDINGUNGSLOS** | Paper VIII + `airy_discrete_stability_lemma.tex` |
| H3 (Paper VII) | Uniform bound B-strong | 🔴 **offen** — einzig verbleibende Hauptlücke | Paper VII |
| DSTP | Discrete Spectral Transfer Property | ✅ verifiziert (Zufalls-/Gauß-Sampling) | Paper I |
| DSTP ⊥ AX1-AX4 | Logische Unabhängigkeit (Riemann-Zeuge) | ✅ **BEWIESEN** | `ax5_independence_remark.tex` |
| DSTP (Primes) | DSTP für Primzahl-Sampling | 🔴 offen | Paper I |
| Assumption 3.1 Off-diag | Off-diagonal decay, Kantenregime | 🔴 offen | Paper III |
| B-strong | P_{kl} ≤ C₂ c^{1/2} | 🔴 **offen** — WKB/Airy-Route nötig | Paper VI, VII |
| B' | Summabilitätsbedingung (folgt aus B-strong) | 🔴 offen (bedingt) | Paper VI, VII |
| Conj. ULW | Landau-Widom globales erfc-Gesetz | 📊 empirisch | Paper VIII, numerics/ |
| β(∞) | Limes des Zentrierungsparameters β(c) | 📊 empirisch: β(∞) ∈ [-0.30,-0.21] | Paper VIII |
| Weil-Operator | G_∞ = Weil-Operator | 🔴 offen | Paper II |
| XRY-Stabilität | XRY-Stabilitätskonjektur | 🔴 offen (bedingt) | Paper II_quad |

---

## Vollständige Abhängigkeitskette der Begleitnotizen

### `phase_nondeg_lemma.tex` → H1 Non-Degeneracy (Paper VII)

```
Paper IV  [BS-Halbinkrement: (1/2)(S+(χ_{k+1})-S+(χ_k)) = π/2 + O(1/k²)]
  +
ORX Thm. 4.6  [Airy-Verbindungsfehler E_k(c) = O(c^{-1/3})]
  +
Langer-Transformation  [Phasenoffset T_k = (2√2/3)U_k^{3/2} + O(c^{-1/3})]
  ↓
Lemma A:  α^(c) = (1/2)(S+(χ_{k+1})-S+(χ_k)) + R_{k+1} - R_k
Lemma B:  T_k(c) = (2√2/3)U_k^{3/2} + O(c^{-1/3}), |T_{k+1}-T_k| = O(c^{-4/3})
Lemma B': Θ_k(s*) = Φ_k(s*) + T_k(c) + O(c^{-1/3})
Lemma C:  R_k(c) = E_k(c) = O(c^{-1/3})  [T_k kürzt sich exakt heraus]
Lemma D:  |R_{k+1} - R_k| = O(c^{-4/3})
  ↓
Prop.:    |α^(c) - π/2| ≤ C_A c^{-1/3}  gleichmäßig in k ≤ N
Cor. 1:   dist(α^(c), {0,π}) ≥ π/4  für c ≥ c_0(A)  →  Conj. 6.1 bewiesen
Cor. 2:   H1 (Paper VII) bedingungslos
```

### `airy_discrete_stability_lemma.tex` → ass:gap + Prop.U(U') (Paper VIII)

```
ORX Thm. 4.6  [λ_l - F_Ai(x_l) = E_l(c), |E_l| ≤ C₁ c^{-2/3}]
  ↓
Lemma U:   |λ_l - F_Ai(x_l)| ≤ C₁ c^{-2/3}  [recalled]
  +
C¹-Regularität E_l = E(μ_l, c) in μ_l  [ORX Ch.4, Gl.(4.31)]
  +
|μ_{l+1} - μ_l| = O(c^{-1})  [|χ_{l+1}-χ_l| = O(c^{1/3}), Paper IV]
  ↓
Lemma U':  |(λ_l-λ_{l+1}) - (F_Ai(x_l)-F_Ai(x_{l+1}))| ≤ C₂ c^{-2/3}
           [tatsächlich O(c^{-5/3}) — viel besser als benötigt]
  +
Ai(x)² ≥ c_min > 0 auf [-A_0, A_0]
  ↓
ass:gap:   λ_l - λ_{l+1} ≥ κ_0 (c/2)^{-1/3}  bedingungslos, κ_0 = c_min/2
```

### Gesamte Kette zu ‖DT_c^(N)‖ < 1

```
H1:  phase_nondeg_lemma.tex  →  α^(c) = π/2 + O(c^{-1/3})  ✅
H2:  airy_discrete_stability_lemma.tex → ass:gap → Lemma F → Kor.C(a)  ✅
     airy_discrete_stability_lemma.tex → Prop.U(U') → Lemma A → Kor.C(b)  ✅
H3:  B-strong  →  🔴 offen

H1 + H2 + H3  →  Theorem 1 (Paper VII)  →  ‖DT_c^(N)‖ ≤ C c^{-1/2} log c < 1
             →  Kontraktion  →  Fixpunkt  →  Assumption A
```

---

## Was Paper VIII konkret liefert (Drei-Skalen-Struktur)

- **Kombinatorische Skala** (Dyadische Trennung): ass:gap → Lemma F → Kor.C(a) — **bedingungslos** ✅
- **Lokale Skala** (Airy/WKB): Prop.U(U') → Lemma A → Kor.C(b) — **bedingungslos** ✅
- **Globale Skala** (Landau-Widom): Konjektur ULW — numerisch gestützt, offen
- **Entscheidende Kürzung in Kor.C, Term 1:** (c/2)^{-1/3} kürzt sich exakt aus Zähler und Nenner → Ergebnis O(2^{-m}) unabhängig von c ✅

---

## Was Paper V konkret schließt

Paper V beweist Assumption ass:bulkconv **unconditionally für γ < 1/2** via:
1. **Bridge Lemma** (Theorem 4.1): geometrische Abdeckung der verbotenen Zonen
   → `E_out(f_{mn}) ≤ C_γ · e^{-α_γ c}` für alle m,n ≤ γ N_Sh
2. **Schur-Diagonal-Bound** (Prop. 3.1 + Schur-Test, Section 5):
   → `K_N(x,x) ≤ C · Nc/(πT)` auf Bulk-Intervallen
3. **Corollary 5.2**: Bulk-Tail-Bound `‖(I-P_N)f_{mn}‖ ≤ Ce^{-α'N}` unbedingt

**Voraussetzung:** γ < 1/2. Extension zu γ ∈ [1/2, 1) bleibt offen.

---

## Was Paper VI konkret liefert (No-Go)

- **Theorem 2 (No-Go):** Jede Matrix T mit `T_{ii}=0`, `|T_{ij}| ≤ κ/|i-j|`
  erfüllt `‖T‖ ≥ κ/2 · H_{N-1} ~ κ/6 · log c` — optimal in dieser Klasse.
- **Konsequenz:** Nicht-oszillatorische Schur-Argumente können `‖T‖ < 1` nicht liefern.
- **Layer-0 Geometrie (unbedingt):**
  - Obstruktion lokalisiert auf `|k-l| ≲ c^{1/6}`
  - `c^{1/6}` ergibt sich eindeutig aus Drei-Regime-Balance

---

## Strategische Diagnose (Mai 2026, aktualisiert)

**Gelöste Probleme seit letztem Update:**
- Phase Non-Degeneracy → H1 bedingungslos ✅
- ass:gap → Dyadisches Trennungsprinzip bedingungslos ✅
- Proposition U(U') → H2 bedingungslos ✅
- DSTP ⊥ AX1-AX4 konstruktiv bestätigt ✅

**Einzige verbleibende Hauptlücke:** B-strong (`P_{kl} ≤ C₂ c^{1/2}`)

Sobald B-strong fällt: H3 ✅ → Theorem 1 (Paper VII) unbedingt → Kontraktion → Assumption A → vollständige Theorie.

**Bulk-Programm (γ < 1/2):** abgeschlossen durch Papers IV + V.
Das verbleibende Problem ist die Kontraktion von DT_c^(N) — ein separater Mechanismus.
