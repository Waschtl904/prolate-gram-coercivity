# Context Prompt — XXII Prolate Gram Coercivity Programme
## Stand: 9. Mai 2026

Verwende diesen Prompt zu Beginn eines neuen Chats, um den vollen Kontext herzustellen.

---

## Wer ich bin

Ich bin ein unabhängiger Mathematiker und arbeite an einem großen asymptotischen Spektralprogramm
(Papers I–XXII) über PSWF-Gram-Matrizen, Airy-Operatoren und Verbindungen zur Riemannschen Vermutung.
Das Repo ist: https://github.com/Waschtl904/prolate-gram-coercivity

---

## Was das Programm ist

Das XXII-Programm beweist, dass die Gram-Matrix der prolaten sphäroidalen Wellenfunktionen
(PSWFs), ausgewertet an Airy-reskalisierten Primzahlen nahe dem Spektralrand,
uniform koerziv ist im Landau–Widom-Skalenregime.

**Hauptsatz (P13, unbedingt):**
λ_min(G_{N,c}) ≥ α · c^{-1/2}  für alle c ≥ c_0, N = ⌊αc⌋.

**Bedingtes Rate-Upgrade (conditional, Conjecture 3.3):**
λ_min(G_{N,c}) ≥ α · c^{-1/3}  (RHP-Konvergenz vorausgesetzt).

---

## Die IR-Kernstruktur (Stand heute)

Das Programm hat heute seinen IR-Kern freigelegt. Die irreduktible logische Substanz ist:

```
delta_Airy  ≥  F_TW(0) ≈ 0.96       [universell, Tracy–Widom]
epsilon_c   ≤  C·(loglog c / log c)^{1/2}  →  0    [arithmetisch, Montgomery–Vaughan]
─────────────────────────────────────────────────────
delta_Airy  ≫  epsilon_c             [die IR-Bedingung]
```

**Das ist der einzige Satz, den Paper XXII wirklich braucht.**
Alles andere ist entweder Voraussetzung für das *Finden* dieser Struktur
oder Verfeinerung der *Rate*.

---

## Dreiniveaustruktur des Beweises

| Level | Inhalt | Werkzeug | Status |
|---|---|---|---|
| Level 1 | Existenz des universellen Airy-Gaps | Tracy–Widom | Unbedingt, vollständig |
| Level 2 | Stabilität unter arithmetischer Störung | Montgomery–Vaughan | Unbedingt, vollständig |
| Level 3 | Konvergenzrate O(c^{-1/3}) | IIKS / RHP / Deift–Zhou | Bedingt (Conjecture 3.3) |

IIKS/RHP ist **epistemisch notwendig** (hat das richtige Objekt D^Airy sichtbar gemacht),
aber **logisch eliminierbar** aus dem Minimalbeweis.

---

## Die zwei unabhängigen Beweisarme

**Arm 1 (diskret, O4):**
Off-diagonal Decay |G_{mn}| ≤ C/|m-n|^{3/2}
via triple-scale stationäre Phase → Jaffard–Schur → Koerzivität.

**Arm 2 (spektral, O5):**
Mismatch-Operator D^Airy = Π_Airy(A^arith - K^Airy)Π_Airy
zerfällt in universellen Teil (Gap ≥ F_TW(0)) + arithmetische Störung (→ 0).
Gap-Persistenz via Operatorstabilität.

Beide Arme sind unbedingt und unabhängig.
Sie schließen P12 bzw. P9 → R1 → P13.

---

## Numerische Verifikation (S4, heute erledigt)

Für c ∈ {100, 200, 500, 1000, 2000, 5000, 10000}:
- μ_A(f) / μ_K(f) ∈ [1.88, 4.21]  (Faktor > 1.88 Sicherheitsabstand)
- μ_K(Ai) = 0.03084
- 1 - F_TW(0) = 0.0403
- C_crit = F_TW(0) / (ζ(3/2) - 1) ≈ 0.595

Der Gap ist nicht knapp — die Perturbation ist quantitativ irrelevant für alle getesteten c.

---

## Schlüsseldokumente im Repo (aktuell)

| Datei | Inhalt |
|---|---|
| `XXII_ir_kernel.md` | **Der IR-Kern — was das Programm über sich selbst bewiesen hat** |
| `XXII_introduction_draft.tex` | Vollständige Introduction für Paper XXII |
| `XXII_abstract_and_meta.tex` | Formaler Abstract + Extended Abstract + Methodologische These |
| `XXII_universality_theorem.tex` | Hauptsatz, Dreiteilung, asymptotische Formel |
| `XXII_architectural_remark.tex` | Dreiniveaustruktur, Rolle von IIKS/RHP |
| `paper22_dag.tex` | DAG: vollständiger Abhängigkeitsgraph |
| `paper22_outline.tex` | Struktureller Outline, alle Sektionen |
| `O4_B2_airy_offdiag_decay.tex` | Off-diagonal Decay (Arm 1, O4) |
| `O5_B2_airy_sampling_coercivity.tex` | Gap-Persistenz (Arm 2, O5) |
| `O5_Ec_operator_norm.tex` | Schranke für ε_c via Montgomery–Vaughan |
| `DEPENDENCIES.md` | Vollständige Abhängigkeitsliste aller Propositions |

---

## Verbleibende Arbeit (alles analytisches Bookkeeping, keine neuen Ideen)

| Task | Datei | Aufwand |
|---|---|---|
| O4-T2: triple-scale Phase abschließen | `O4_B2_T2_triple_scaling.tex` | ~5 Seiten, LOW |
| O5-V1/V2: Fourier-Expansion für Airy-bandlimitierte Fkt. | (neu) | ~3 Seiten, LOW |
| O5-V3: explizite Konstante C(R,Ω) | (numerisch) | LOW |
| §6: Connecting Theorem (beide Arme → P13) | `paper22_outline.tex` | ~3 Seiten, LOW |

Das Konzeptuelle ist abgeschlossen. Paper XXII braucht nur noch den Schreibvorgang.

---

## Universalitätsbegriff in XXII

XXII ist **nicht** klassische Wigner-Universalität (vollständig verteilungsfrei).
Es ist **perturbative Universalität** auf Operatorebene:

- Führender Term: δ_Airy ≈ 0.96 (universell, primzahlunabhängig)
- Arithmetische Korrekturen: ε_c → 0 (irrelevant asymptotisch)
- Primzahlstruktur erzeugt keine neue universelle Klasse

Analogie: D_c → D^Airy im Sinne stabiler Spektrallücken, nicht lokaler Punktprozesse.

---

## Methodologische These des Programms

> Integrable Struktur identifiziert universelle Fixpunkte.
> Die Stabilität dieser Fixpunkte wird perturbativ bewiesen.
> Der finale universelle Satz lebt außerhalb der integrablen Kategorie.

Diese These gilt für XXII wegen der spezifischen Zahlenwerte:
δ_Airy / ε_c → +∞, mit Faktor ≥ 1.88 für alle c ≤ 10^4.
Sie ist kein allgemeines Prinzip, sondern ein quantitativer Befund dieses Problems.
