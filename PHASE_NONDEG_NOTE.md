# Phase Non-Degeneracy — Offener Gap in Paper VII

> Stand: Mai 2026.
> Dieses Dokument isoliert den kritischsten offenen Punkt in Paper VII
> (`paper7_skeleton.tex`) für gezielten Angriff.

---

## Was der Gap ist

In **Paper VII, Proposition 3.1(a)** wird behauptet, H1 (Phase Non-Degeneracy)
sei **unbedingt** (unconditionally) erfüllt.

Der Beweis läuft:
1. Widom-Eigenwertsasymptotik → Phase existiert: `Φ_{ij} = α^(c)(i-j) + O(|i-j|²/c)`
2. Summabilitätsbedingung: `Σ_m ε_m^(N) ≤ C c^{-1/3} log c → 0` ✅ (korrekt)
3. **Non-Degeneracy:** `α^(c) ∉ {0, π}` — NUR als "uniformly in c" behauptet, **ohne Referenz**

---

## Warum das kritisch ist

Der Dirichlet-Kernel-Bound in Paper VII, Step 3 des Beweises:
$$
|B(s,t)| = \left|\frac{e^{i\alpha(i-s)} - e^{i\alpha(i-t-1)}}{1 - e^{-i\alpha}}\right| \leq \frac{2}{|1 - e^{i\alpha}|} =: C_\alpha < \infty
$$
ist **nur endlich, weil α ∉ {0, π}**.

Falls α^(c) → 0 oder α^(c) → π für eine Folge c → ∞:
- `C_α → ∞`
- der Cancellation-Mechanismus kollabiert
- Theorem 1 (Dyadic Cancellation) gilt nicht mehr uniform in c

Ein Referee kann sagen: **"Ihre gesamte Cancellation-Struktur kollabiert im Resonanzfall."**
Das wäre korrekt.

---

## Mathematischer Hintergrund

Die Phase `α^(c)` ist der WKB-Phase-Inkrement an `s* = 1 - c^{-2/3}`:
$$
\alpha^{(c)} = \Theta_{k+1}^{(c)} - \Theta_k^{(c)} \big|_{s=s*}
$$
Diese Größe hängt von der Sturm-Liouville-Eigenwertsabstandsverteilung ab.

**Was Widom gibt:** asymptotische Formeln für λ_n(c), χ_n(c) — aber keine direkte
quantitative untere Schranke für den Abstand von α^(c) zu {0, π}.

**Was gebraucht wird:** eine der folgenden Aussagen:
- `∃ ε₀ > 0` unabhängig von c: `dist(α^(c), {0, π}) ≥ ε₀`
- oder: α^(c) → α₀ ∉ {0, π} für c → ∞ (mit Rate)

---

## Drei Optionen

### Option 1: Kurzes Lemma (optimal)
Aus Sturm-Liouville-Theorie + Widom-Asymptotics:
- Eigenwertabstand `χ_{k+1} - χ_k ≈ 2c + O(1)` im Bulk
- Phase-Inkrement aus expliziter WKB-Formel für `θ_n(s*)`
- Falls beweisbar: `α^(c) → π/2` oder ähnliches (ergibt `C_α = √2` — optimal)

**Aufwand:** 1–2 Seiten, erfordert explizite WKB-Formel für θ_n(s*)

### Option 2: Verweis auf bestehende Literatur
Prüfen ob Osipov–Rokhlin–Xiao 2013, Olver 1974, oder Widom 1964
explizit eine uniforme untere Schranke liefern.

**Aufwand:** Literaturrecherche, ggf. 1 Paragraph in Paper VII

### Option 3: Explizite Conjecture (Fallback)
Formuliere als **Conjecture 1.1** in Paper VII:

> **Conjecture (Phase Non-Degeneracy).**
> Es gibt ε₀ > 0 unabhängig von c ≥ 1, so dass
> dist(α^(c), {0, π}) ≥ ε₀
> für alle c ≥ c₀.

Dann ist H1 in Paper VII **bedingt** (nicht unconditional).
Conj. phase (wie in Paper VI definiert) deckt das ab.

**Aufwand:** 2 Zeilen in Paper VII, 1 Paragraph Begründung

---

## Empfehlung

**Sofort (heute):** Option 3 umsetzen — Non-Degeneracy sichtbar machen.
Eine implizite Lücke ist schlechter als eine explizite Conjecture.

**Mittelfristig:** Option 1 oder 2 versuchen.
Conj. phase liegt auf der natürlichen WKB-Linie — vermutlich lösbar
mit 1–2 Seiten sorgfältiger Rechnung.

---

## Verbindung zu Paper VI

Paper VI definiert **Conjecture 6.1 (Linear phase equidistribution)**:
> Θ_k^(c) = α^(c) k + β^(c) + O(k²/c), α^(c) ∈ (0, 2π) away from 0, π.

Die Non-Degeneracy-Bedingung **ist bereits in Conjecture 6.1 von Paper VI enthalten.**
Paper VII muss nur explizit auf diese Conjecture verweisen, statt sie stillschweigend
zu benutzen.

**Konsequenz:** Paper VII H1 (unconditional) → H1 bedingt auf Conj. 6.1 von Paper VI.
Das ist ehrlicher und konsistent mit der Layer-Struktur.
