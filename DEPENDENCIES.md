# DEPENDENCIES — prolate-gram-coercivity

> Stand: Mai 2026. Alle Papers I–VII berücksichtigt.

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
Paper V  (WKB Cover, Bridge Lemma, Schur Control)
  ↓  **BEWIESEN**: ass:bulkconv (Assumption 2.4) für γ < 1/2
Paper VI  (Galerkin Norm, No-Go-Theorem, Layer 0–2)
  ↓  liefert: Methodenbarriere (Schur-Klasse tot)
             Layer-0 Geometrie der Obstruktion
Paper VII  (Dyadic Cancellation, Reduktion)
  ↓  liefert: Abstrakte Cancellation unter H1–H3 (vollständig)
             Reduktion auf B-strong (H3) + Conj.amplitude (H2)
```

---

## Status aller Assumptions und Conjectures

| ID | Beschreibung | Status | In Paper |
|---|---|---|---|
| ass:bulkconv (Ass. 2.4) | Bulk-Faltungsabfall `E_out(f_{mn}) ≤ Ce^{-αc}` für γ<1/2 | ✅ **BEWIESEN** (Bridge Lemma) | Paper V |
| ass:gap | Uniform Gap Condition | 🔴 offen | Paper III (Ziel: Paper IX) |
| DSTP | Discrete Spectral Transfer Property | ✅ verifiziert (Zufalls-/Gauß-Sampling) | Paper I |
| DSTP (Primes) | DSTP für Primzahl-Sampling | 🔴 offen | Paper I |
| Assumption 2.4 Off-diag (3.1) | Off-diagonal decay, Kantenregime | 🔴 offen | Paper III |
| B-strong | `P_{kl} ≤ C₂ c^{1/2}` | 🔴 offen — Methodenwechsel nötig (WKB/Airy) | Paper VI, VII |
| Conj. phase | α^(c) linear + non-degenerate | 🔴 offen — **kritisch für Paper VII H1** | Paper VI, VII |
| Conj. amplitude | Lipschitz-Amplitude auf dyadischen Blöcken | 🔴 offen | Paper VI, VII |
| B' | Summabilitätsbedingung | 🔴 offen — folgt aus B-strong + Conj.phase + Conj.amplitude | Paper VI, VII |
| Weil-Operator | G_∞ = Weil-Operator | 🔴 offen | Paper II |
| XRY-Stabilität | XRY-Stabilitätskonjektur | 🔴 offen (bedingt) | Paper II_quad |
| ULW | Uniform Large-Width Conjecture | 📊 empirisch stabil | numerics/ |

---

## Was Paper V konkret schließt

Paper V beweist Assumption ass:bulkconv **unconditionally für γ < 1/2** via:
1. **Bridge Lemma** (Theorem 4.1): geometrische Abdeckung der verbotenen Zonen
   → `E_out(f_{mn}) ≤ C_γ · e^{-α_γ c}` für alle m,n ≤ γ N_Sh
2. **Schur-Diagonal-Bound** (Prop. 3.1 + Schur-Test, Section 5):
   → `K_N(x,x) ≤ C · Nc/(πT)` auf Bulk-Intervallen
3. **Corollary 5.2**: Bulk-Tail-Bound `‖(I-P_N)f_{mn}‖ ≤ Ce^{-α'N}` unbedingt

**Voraussetzung:** γ < 1/2. Extension zu γ ∈ [1/2, 1) bleibt offen (Remark 4.3 in Paper V).

---

## Was Paper VI konkret liefert (No-Go)

- **Theorem 2 (No-Go):** Jede Matrix T mit `T_{ii}=0`, `|T_{ij}| ≤ κ/|i-j|`
  erfüllt `‖T‖ ≥ κ/2 · H_{N-1} ~ κ/6 · log c` — optimal in dieser Klasse.
- **Konsequenz:** Nicht-oszillatorische Schur-Argumente können `‖T‖ < 1` nicht liefern.
  Kontrakion erfordert zwingend oszillatorische Cancellation (signierte Struktur).
- **Layer-0 Geometrie (unbedingt):**
  - Obstruktion lokalisiert auf `|k-l| ≲ c^{1/6}` (relative Bandbreite → 0)
  - `c^{1/6}` ergibt sich eindeutig aus Drei-Regime-Balance (Remark 4.2 in Paper VI)

---

## Was Paper VII konkret liefert

- **Theorem 1 (Dyadic Cancellation):** Unter H1–H3 gilt
  `sup_i ∑_{j≠i} |T_{ij}| = O(1)` — vollständig bewiesen (Appendix).
- **Reduktion:** PSWF-Galerkin-Operator erfüllt:
  - H1 (phase): **unbedingt** (Widom + Summabilitätsbedingung) — ABER α ∉ {0,π} noch zu referenzieren
  - H2 (amplitude regularity): unter **Conj.amplitude** (offen)
  - H3 (uniform bound): unter **B-strong** (offen)
- **Corollary 3.1:** Unter B-strong + Conj.phase + Conj.amplitude:
  `‖DT_c^(N)‖ ≤ C c^{-1/2} log c → 0` → Kontraktion → Assumption A

---

## Strategische Diagnose (Mai 2026)

**Verbleibende Hindernisse bilden ein gekoppeltes System:**
- Conj. phase (lokal, am nächsten lösbar)
- B-strong (WKB/Airy-Ebene, eigenes Paper-Level-Problem)
- Conj. amplitude (Lipschitz-Kontrolle, tief gekoppelt mit B-strong)

**Nächster Angriffspunkt:** Phase Non-Degeneracy (Conj. phase)
→ Entweder kurzes Lemma aus Widom-Daten, oder explizite Conjecture isolieren
→ Details: `PHASE_NONDEG_NOTE.md`

**Bulk-Programm (γ < 1/2):** abgeschlossen durch Papers IV + V.
Das verbleibende Problem ist die Kontraktion — ein anderer Mechanismus.
