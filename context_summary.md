# Context Summary — prolate-gram-coercivity

> Stand: Mai 2026. Vollständige Notation, alle Paper-Abhängigkeiten, offene Probleme.
> Für neuen KI-Chat: dieses Dokument + relevante paper*.tex lesen.

---

## Überblick: Papers I–VII

| Paper | Datei | Inhalt | Status |
|---|---|---|---|
| I | `paper1.tex` | Gram-Koerzivität, DSTP, Defektzerlegung | Near publication-ready |
| II | `paper2.tex` | Skalierungslimiten, Spurformel, Weil-Verbindung | Near publication-ready |
| II_quad | `paper2_quadrature.tex` | XRY-Quadratur, konditionaler Framework | Reinschrift |
| III | `paper3.tex` | PSWF-Produkt Spektral-Tail-Schätzungen | Reinschrift |
| IV | `paper4_semiclassical.tex` | Semiklassische Äquidistribution ψ_n² → ρ^cl | Vollständig bewiesen |
| V | `paper5.tex` | WKB Cover, Bridge Lemma, Schur Control | **Vollständig bewiesen** |
| VI | `paper6.tex` | Galerkin Norm, No-Go-Theorem, Layer 0–2 | **Publikationsreif** |
| VII | `paper7_skeleton.tex` | Dyadic Cancellation, Reduktion auf B-strong + Conj.amp | Referee Draft |

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
| `α^(c)` | WKB-Phase an s* — Non-Degeneracy α ∉ {0,π} offen |
| `T_{ij}` | Galerkin-Matrixeinträge von DT_c^(N) |
| `P_{kl}` | Prefaktor: c·|λ_l-λ_k|/((1-λ_k)(1-λ_l)) |
| `B-strong` | Ass.: P_{kl} ≤ C₂ c^{1/2} |
| `B'` | Schur-Summabilitätsbedingung |
| `B_m(i)` | Dyadischer Block {j: 2^m ≤ |i-j| < 2^{m+1}} |

---

## Bewiesene Resultate (Mai 2026)

### Papers I–IV (stabil, nicht wiederholen)
- Gram-Koerzivität unter DSTP ✅
- Defektzerlegung E_{mn} = R_{mn}^quad ✅
- Kompaktheit Gram-Operatoren im Skalierungslimes ✅
- Spurformel mit PNT-Konsistenz ✅
- Bulk-Tail-Bound ‖(I-P_N)f_{mn}‖ ≤ CT^{1/2} (Paper III) ✅
- Schwache Konvergenz ψ_n² → λ_n ρ^cl, Rate O(1/n) (Paper IV) ✅

### Paper V (Bridge Lemma) — NEU ✅
- **ass:bulkconv BEWIESEN für γ < 1/2** (Bridge Lemma, Theorem 4.1)
- E_out(f_{mn}) ≤ C_γ · e^{-α_γ c} für alle m,n ≤ γ N_Sh ✅
- K_N(x,x) ≤ C · Nc/(πT) auf I_δ (Schur-Diagonal-Bound) ✅
- Unconditional Bulk-Tail-Bound ‖(I-P_N)f_{mn}‖ ≤ Ce^{-α'N} für γ<1/2 ✅
- Mechanismus: geometrische Abdeckung der WKB-verbotenen Zonen ✅
- Extension zu γ ≥ 1/2: offen (Remark 4.3)

### Paper VI (No-Go + Layer 0) — STARK ✅
- **No-Go-Theorem:** ‖T‖ ≥ κ/2 · log c — optimal in nicht-oszillatorischer Schur-Klasse ✅
- Konsequenz: Kontraktion erfordert zwingend oszillatorische (signierte) Cancellation ✅
- Obstruktion lokalisiert auf |k-l| ≲ c^{1/6}, relative Bandbreite c^{-1/6} → 0 ✅
- c^{1/6}-Schwelle eindeutig aus Drei-Regime-Balance ✅
- Near/Far-Zerlegung T = T^near + T^far ✅

### Paper VII (Dyadic Cancellation) — Referee Draft ✅/⚠️
- **Abstrakte Dyadic Cancellation (Theorem 1) vollständig bewiesen** (Appendix) ✅
- H1 (Phase): Summabilitätsbedingung Σ ε_m^(N) = o(1) bewiesen ✅
- ⚠️ **H1 Non-Degeneracy:** α^(c) ∉ {0,π} — noch zu referenzieren (kritisch!)
- H2 (Amplitude regularity): unter Conj.amplitude (offen)
- H3 (Uniform bound): unter B-strong (offen)
- Corollary 3.1: B-strong + Conj.phase + Conj.amp → Kontraktion → Assumption A ✅

---

## Offene Probleme (priorisiert)

### 🔥 Priorität 1 — Phase Non-Degeneracy (Paper VII)
**Gap:** α^(c) ∉ {0,π} an s* = 1-c^{-2/3} ist nicht explizit referenziert.
Ohne das kollabiert die Cancellation-Struktur im Resonanzfall.
**Optionen:**
1. Kurzes Lemma aus Widom-Daten + Sturm-Liouville
2. Explizite Conjecture mit quantitativer Schranke: α^(c) ≥ ε₀ > 0
**Details:** `PHASE_NONDEG_NOTE.md`

### 🔥 Priorität 2 — B-strong
**Gap:** P_{kl} ≤ C₂ c^{1/2} ist nicht bewiesen.
**Warum schwer:** zwei konkrete Failure-Modes (Paper VI, Remark 5.2):
- Nicht-uniforme stationäre Phase in der Transition Zone
- Korrelierte Airy-Faktoren (Eigenwert-Spacing und Amplitude nicht unabhängig)
**Route:** WKB/Airy-Matching an s*, Modellproblem formulieren
**Einschätzung:** eigenes Paper-Level-Problem, nicht eine Section

### 🔥 Priorität 3 — Conjecture amplitude
**Gap:** Lipschitz-Kontrolle A_{ij} in j auf dyadischen Blöcken.
**Verbindung:** tief gekoppelt mit B-strong (beide brauchen Transition-Zone-Kontrolle)
**Route:** PSWF-Transition-Asymptotics, Olver 1974

### 🔶 Mittelfristig
- ass:gap (Uniform Gap Condition) — Paper III, Ziel Paper IX
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

## Strategische Diagnose

Der Bulk (γ < 1/2) ist durch Papers IV + V **abgeschlossen**.
Das verbleibende Problem — Kontraktion von T_c^(N) — ist ein **anderer Mechanismus**:
kein weiteres Estimate-Farming, sondern oscillatory cancellation.

Das System ist nicht mehr linear rückständig:
- Phase, B-strong, Amplitude sind **gekoppelt**
- Einziger aktuell lokal angreifbarer Punkt: **Phase Non-Degeneracy**

Das ist der nächste gezielte Angriff.
