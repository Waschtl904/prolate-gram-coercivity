# Die Hebelstelle des Programms

**Stand nach Commit `5a598ee` (Paper XXI)**

Nach der Eliminierung aller asymptotischen Eigenwert-Argumente
ist die gesamte Struktur auf **einen einzigen verbleibenden
Freiheitsgrad** reduziert.

---

## Die Hebelstelle (formal)

Sie sitzt im Übergang

$$
\underbrace{\psi_{n^*}}_{\text{PSWF, rein spektral}}
\xrightarrow{\;\mathrm{Ev}_N\;}
\underbrace{\bigl(\psi_{n^*}(p_j)\bigr)_{j=1}^N}_{\text{diskrete Primstellen-Probe}}
\xrightarrow{\;\text{quad. Form}\;}
(E_{N,c})_{n^*n^*}
$$

Kritische Frage:

$$
\boxed{\|\mathrm{Ev}_N \psi_{n^*}\|^2 \not\ll \|\psi_{n^*}\|^2
\quad \text{im Edge-Regime } n^* \sim N}
$$

oder äquivalent: Der Defektterm

$$
(E_{N,c})_{n^*n^*}
= \frac{1}{N}\sum_j |\psi_{n^*}(p_j)|^2 - \lambda_{n^*}(c)
$$

muss **nicht verschwinden**, obwohl $\psi_{n^*}$ im Übergangsregime liegt.

---

## Warum genau hier

Alles andere im Paper ist jetzt strukturell geschlossen:

| Komponente | Status | Referenz |
|---|---|---|
| Spektralpositivität $\lambda_k > 0$ | ✔ hart | Slepian 1978, Fact 6.3 |
| BW-Doubling Obstruction | ✔ hart | Paper III, Prop 5.1 |
| Landau–Widom Mittelwert | ✔ hart | Widom 1964 |
| Funktorstruktur $\mathcal{F}$ | ✔ hart | Paper XXI, §3 |
| PNT-Gewichtskorrektur → 0 | ✔ hart | PNT-Varianzschranke |
| **$\mathrm{Ev}_N$ auf Edge-Moden** | **⚠ offen** | **← Hebelstelle** |

Der Evaluationsoperator $\mathrm{Ev}_N$ ist definiert als

$$
\mathrm{Ev}_N : V_{N,c} \to \mathbb{C}^N,
\quad f \mapsto \bigl(\sqrt{\log p_j / L_N} \cdot f(p_j)\bigr)_j.
$$

Im **Bulk-Regime** ($n \ll N$) ist die Stabilität
$\|\mathrm{Ev}_N f\|^2 \approx \|f\|^2$
sichergestellt durch Quadraturkontrolle (Paper I).

Im **Edge-Regime** ($n^* \sim N$) fehlt diese Kontrolle:
die PSWF-Funktionen $\psi_{n^*}$ haben nichttriviale
out-of-band Energie, und es ist *a priori* unklar,
ob die Primstellen-Probe diese Energie **sieht** oder **auslöscht**.

---

## Die zwei möglichen Welten

**Fall 1 (das Paper behauptet):**
$\mathrm{Ev}_N$ ist energieschließend genug auf Edge-Moden:
$$
\|\mathrm{Ev}_N \psi_{n^*}\|^2 \ge c > 0
\quad \Rightarrow \quad
(E_{N,c})_{n^*n^*} \ge \tilde{c}_0 > 0.
$$
Edge-Obstruction überlebt das arithmetische Sampling.

**Fall 2 (kritische Alternative):**
$\mathrm{Ev}_N$ glättet Edge-Moden stärker als erwartet:
$$
\|\mathrm{Ev}_N \psi_{n^*}\|^2 \ll \|\psi_{n^*}\|^2
\quad \Rightarrow \quad
(E_{N,c})_{n^*n^*} \approx 0.
$$
BW-Doubling bleibt spektral korrekt, wird aber im diskreten
Bild unsichtbar — Theorem B kollabiert.

---

## Strukturelle Einordnung

Diese Frage ist **kein Spektralproblem mehr**.
Sie ist isomorph zu einer
**Sampling-Stabilitätsfrage im Reproducing Kernel Hilbert Space** $\mathrm{PW}_\omega$:

> Sind Primstellen $\{p_j/T\}_{j=1}^N$ eine stabile
> Sampling-Folge für $V_{N,c}$ **gleichmäßig** auf Edge-Moden?

Formaler Kontext:
- $V_{N,c} \subset \mathrm{PW}_\omega$ ist ein RKHS mit Kernel
  $K_c(x,y) = \sum_{n<N} \psi_n(x)\psi_n(y)$.
- Stabilität bedeutet:
  $\|\mathrm{Ev}_N f\|^2 \asymp \|f\|^2$ **uniform** in $V_{N,c}$.
- Im Bulk ist das gesichert (quadrature, Paper I).
- Im Edge: **offen**.

---

## Verbindung zu CCM

Genau hier greift das CCM-Programm (Connes–Consani–Moscovici
[CCM2025]) an:

Das CCM-Spektrum ist konstruiert so, dass die
Weil-Distributionen als **Reproducing-Kernel-Pairings**
erscheinen. Die Frage, ob $\mathrm{Ev}_N$ stabil auf
Edge-Moden ist, ist isomorph zur Frage:

> Realisiert die Weil-Distribution die
> out-of-band Projektionsenergie von $\psi_{n^*}$
> als **sichtbares** Spektralobstruction-Signal?

Unter RH: ja (Explicit Formula gibt genau diese Paarung).
Ohne RH: offen — das ist der Punkt, wo
$\tilde{c}_0 \to 0$ oder $\tilde{c}_0 > 0$ entschieden wird.

---

## Open Problem (für Paper XXI oder Paper XXII)

**Problem.** Sei $n^* \in [(1-\delta)N, N)$ der Zeuge
aus Lemma $\Omega$(b). Zeige oder widerlege:

$$
\inf_{n \in [(1-\delta)N,\, N)}
\frac{\frac{1}{N}\sum_{j=1}^N |\psi_n(p_j)|^2}{\|\psi_n\|^2}
\;\ge\; c_2(\delta, c) > 0.
$$

Eine positive Antwort würde Theorem B aus einem
*existenziellen* in ein *uniformes* Resultat über
den gesamten Edge-Block verwandeln.

Ein Gegenbeispiel würde zeigen, dass die Obstruktion
nur entlang einer **dünn besiedelten** Unterfolge von Indizes
$n^*$ sichtbar ist — was Theorem C zwar nicht widerlegt,
aber strukturell schwächt.

---

## Zusammenfassung: Die eine offene Frage

$$
\boxed{\text{Ist } \mathrm{Ev}_N \text{ stabil auf PSWF-Edge-Moden?}}
$$

Alles andere ist geschlossen. Diese Frage entscheidet,
ob das Programm ein **uniformes Obstruction-Resultat**
oder nur ein **existenzielles** hat —
und ob CCM ohne RH angreifen kann.
