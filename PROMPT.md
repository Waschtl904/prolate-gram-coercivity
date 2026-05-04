# Kontext: Mathematisches Forschungsprojekt — Prolate–Weil Program

> **Verwendung:** Diesen Prompt am Anfang jedes neuen KI-Chats einfügen.
> Danach `context_summary.md` aus diesem Repo laden lassen — sie enthält
> die vollständige Notation, alle Paper-Abhängigkeiten und offenen Probleme.
> **Repo:** `github.com/Waschtl904/prolate-gram-coercivity`
> **Stand: Mai 2026** — Papers I–VII vorhanden. Nicht veraltet benutzen.

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

Rigoros, selbstenthaltend. Sieben Papers in verschiedenen Fertigungsstadien:

| File | Inhalt | Status |
|---|---|---|
| `paper1.tex` | Gram-Koerzivität, Defektzerlegung, DSTP | Near publication-ready |
| `paper2.tex` | Skalierungslimiten, Spurformel, Weil-Verbindung | Near publication-ready |
| `paper2_quadrature.tex` | XRY-Quadratur, konditionaler Implication-Framework | Reinschrift |
| `paper3.tex` | PSWF-Produkt-Spektral-Tail-Schätzungen | Reinschrift |
| `paper4_semiclassical.tex` | Semiklassische Äquidistribution der PSWF-Dichten | Vollständig bewiesen |
| `paper5.tex` | WKB Cover, Schur Control, Bridge Lemma | **Vollständig bewiesen** |
| `paper6.tex` | Galerkin Norm Estimates, No-Go-Theorem, Layer 0–2 | **Publikationsreif (No-Go stark)** |
| `paper7_skeleton.tex` | Dyadic Cancellation, Reduktion auf B-strong + Conj. amplitude | Referee Draft |

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
Paper VII  (Dyadic Cancellation: Reduktion auf H2 = Conj.amplitude + H3 = B-strong)
```

---

## Aktueller Stand (Mai 2026)

### Was unbedingt bewiesen ist
- Gram-Koerzivität unter DSTP mit expliziten Schranken (Paper I) ✅
- Exakte Defektzerlegung `E_{mn} = R_{mn}^quad` (Paper I) ✅
- DSTP verifiziert für Zufalls- und Gauß-PSWF-Sampling (Paper I) ✅
- Kompaktheit normierter Gram-Operatoren im Skalierungslimes (Paper II) ✅
- Spurformel mit PNT-Konsistenz (Paper II) ✅
- Uniforme Off-diagonal-Schranke `‖(I-P_N)f_{mn}‖ ≤ CT^{1/2}` (Paper III) ✅
- Mittlere Spektrallokalisierung + exakte Energieformel (Paper III) ✅
- Spektrale untere Schranke + Kantenobstruktion (Paper III) ✅
- Schwache Konvergenz ψ_n² → λ_n ρ^cl, Rate O(1/n) (Paper IV) ✅
- Bulk-Dekorrelationsreduktion vollständig geliefert (Paper IV → III) ✅
- **ass:bulkconv (Assumption 2.4 / Paper III) für γ < 1/2 BEWIESEN (Paper V, Bridge Lemma) ✅**
- Unconditional Bulk-Tail-Bound `‖(I-P_N)f_{mn}‖ ≤ Ce^{-αN}` für γ < 1/2 (Paper V) ✅
- No-Go-Theorem: nicht-oszillatorische Schur-Klasse gibt `‖T‖ ≥ κ/2 · log c` — optimal, unlösbar (Paper VI) ✅
- Layer-0 Geometrie der Obstruktion vollständig (Paper VI) ✅
- H1 (Phase non-degeneracy) bewiesen für Summabilitätsbedingung — Non-Degeneracy α ∉ {0,π} noch zu referenzieren (Paper VII, ⚠️ offener Punkt) ✅/⚠️
- Abstrakte Dyadic Cancellation unter H1–H3 vollständig bewiesen (Paper VII, Appendix) ✅
- Reduktion der Kontraktion auf B-strong (H3) + Conj.amplitude (H2) (Paper VII) ✅

### Was noch offen ist
- **Phase Non-Degeneracy α^(c) ∉ {0,π} an s* = 1 - c^{-2/3}** — kritisch für Paper VII H1
  → Lemma oder explizite Conjecture nötig, NICHT implizit lassen
- **B-strong** (`P_{kl} ≤ C₂ c^{1/2}`) — erfordert WKB/Airy-Matching, eigenes Paper-Level-Problem
- **Conjecture amplitude** (H2): Lipschitz-Kontrolle der Amplituden auf dyadischen Blöcken
- **Conjecture phase** (H1 Non-Degeneracy): explizite quantitative Aussage über α^(c)
- DSTP für Primzahl-Sampling (Paper I)
- Off-diagonal-Abfall: Assumption 3.1 (Paper III) für Kantenregime
- Identifikation von G_∞ als Weil-Operator (Paper II)
- XRY-Stabilitätskonjektur (Paper II_quad)
- Kantenregime m,n ~ N: Airy-Methoden nötig

### Strategische Prioritäten (Mai 2026)
1. **Phase Non-Degeneracy** isolieren: kurzes Lemma oder explizite Conjecture
2. **B-strong**: Modellproblem für WKB/Airy-Route formulieren
3. **Conjecture amplitude**: Lipschitz-Regularity der PSWFs in Transition Zone

### Was assumption_2_4_target.md war
Dieses Dokument beschrieb die Beweisstrategie für ass:bulkconv **vor Paper V**.
Es ist jetzt archiviert (Supersession-Header vorhanden).
**Paper V hat Variante A vollständig ausgeführt. ass:bulkconv ist geschlossen.**

---

## Zentrale Notation (Kurzreferenz)

| Symbol | Bedeutung |
|---|---|
| `ψ_n^(c)` | PSWF auf [-T,T] mit Bandbreite ω, Zeitbandbreite c = ωT |
| `λ_n(c)` | Slepian-Konzentrations-Eigenwert |
| `χ_n(c)` | Sturm-Liouville-Eigenwert von D_c: `χ_n ~ n(n+1) + c²/2` |
| `K_N(x,y)` | Christoffel-Darboux-Kern: `∑_{n=0}^{N-1} ψ_n(x) ψ_n(y)` |
| `P_N` | Orthogonalprojektor auf `span{ψ_0,...,ψ_{N-1}}` in L²([-T,T]) |
| `G^(N)_{p,c}` | Gram-Matrix der PSWF-Quadratur |
| `DSTP` | Discrete Spectral Transfer Property — zentrales Axiom (Paper I) |
| `f_{mn}` | Produktfunktion: `ψ_m^(c) · ψ_n^(c)` |
| `μ_{mn}` | Summe der SL-Eigenwerte: `χ_m + χ_n` |
| `E_{mn}[χ_k]` | Spektralmittelwert von D_c im Zustand f_{mn} |
| `ρ^cl(x)` | Klassische Gleichgewichtsdichte |
| `θ_n(x)` | Prüfer-Phase von ψ_n (Paper IV) |
| `r_n(x)` | Prüfer-Amplitude von ψ_n (Paper IV) |
| `r_n^WKB(x)` | WKB-Referenzamplitude (Paper IV) |
| `N_Sh = 2c/π` | Shannon-Zahl |
| `s* = 1-c^{-2/3}` | Übergangspunkt (transition point), Paper VI/VII |
| `α^(c)` | WKB-Phase an s* — Non-Degeneracy offen |
| `T_{ij}` | Galerkin-Matrixeinträge von DT_c^(N) (Paper VI/VII) |
| `B-strong` | Ass.: `P_{kl} ≤ C₂ c^{1/2}` — offen |
| `Conj.amplitude` | H2: Lipschitz-Amplitude auf dyadischen Blöcken — offen |

---

## Bitte beim Start jedes neuen Chats

1. Lies `context_summary.md` aus **diesem Repo** (prolate-gram-coercivity)
2. Lies die relevante `paper*.tex` je nach Thema des Gesprächs
3. Für offene Probleme: `DEPENDENCIES.md` und `PHASE_NONDEG_NOTE.md`
4. **Kein Claim über ζ(s)-Nullstellen** in keinem der Papers
5. **ass:bulkconv ist NICHT mehr offen** — bewiesen in Paper V
6. **assumption_2_4_target.md ist archiviert** — nicht als aktives Dokument benutzen
