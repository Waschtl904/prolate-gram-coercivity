# Die Hebelstelle des Programms

**Stand nach Commit `5a598ee` (Paper XXI)**

Die gesamte Theorie ist jetzt auf **eine einzige strukturelle Frage** reduziert.

---

## Die minimale operative Form (alles in einer Zeile)

Sei
$$
A_{N,c} := \frac{1}{N}\mathrm{Ev}_N^*\mathrm{Ev}_N, \qquad K_c := \mathcal{K}_c.
$$

Die gesamte Obstruktion ist äquivalent zu:

$$
\boxed{
\|(A_{N,c} - K_c)|_{\mathrm{Edge}}\|_{\mathrm{coercive}} > 0
}
$$

oder explizit:

$$
\boxed{
\inf_{\substack{f \in \mathrm{Edge}\\ \|f\|=1}}
\langle (A_{N,c} - K_c)\,f,\, f\rangle
\;\stackrel{?}{>}\; 0
}
$$

**Das ist der Hebel.** Alles andere folgt daraus oder setzt es voraus.

---

## Drei Fälle, direkt ablesbar

| Regime | Aussage | Konsequenz |
|---|---|---|
| **Bulk** ($n \ll N$) | $\\|(A_{N,c}-K_c)f\\| \to 0$ | Asymptotische Kommutativität (Theorem A) |
| **Edge** (Hebelstelle) | $\exists\, f_{n^*}:\; \langle(A_{N,c}-K_c)f_{n^*}, f_{n^*}\rangle \ge \tilde{c}_0 > 0$ | Theorem B: Obstruction existenziell |
| **Edge uniform** (XXII) | $\inf_{f \in \mathrm{Edge}, \|f\|=1} \langle(A_{N,c}-K_c)f,f\rangle > 0$ | Theorem B uniform: Obstruction geometrisch |

Der Unterschied zwischen Zeile 2 und Zeile 3 ist der einzige
offene Freiheitsgrad im Programm.

---

## Die eine strukturelle Gleichung

Der Defektterm ist:

$$
\underbrace{\frac{1}{N}\sum_{j=1}^N |\psi_{n^*}(p_j)|^2}_{\text{diskrete Beobachtung}}
= \underbrace{\lambda_{n^*}(c)}_{\text{PSWF-Geometrie}}
+ \underbrace{(E_{N,c})_{n^*n^*}}_{\text{sichtbarer Defekt}}
$$

Theorem B $\iff$ $(E_{N,c})_{n^*n^*} \not\to 0$.

Das ist identisch mit drei äquivalenten Formen:

| Sprache | Aussage |
|---|---|
| Sampling | $\|\mathrm{Ev}_N \psi_{n^*}\|^2 \not\approx \lambda_{n^*}(c)\cdot N$ |
| Operator | $\langle A_{N,c}\, \psi_{n^*}, \psi_{n^*}\rangle \ne \langle K_c\, \psi_{n^*}, \psi_{n^*}\rangle$ |
| Ma\xdfklasse | $\mu_{\text{arith}}(|\psi_{n^*}|^2) \ne \lambda_{n^*}(c)$ |

---

## Geometrischer Inhalt

**Bulk:** $A_{N,c}$ und $K_c$ sind asymptotisch ko-diagonalisierbar
im PSWF-Frame. Kommutativität gilt bis auf $O(\log N/\sqrt{N})$.

**Edge:** Zwei inkompatible Geometrien kollidieren:
- PSWF-Eigenstruktur (kontinuierlich, $L^2$)
- Prim-Sampling-Geometrie (diskret, $\ell^2(\{p_j\})$)

Der Kommutator $[A_{N,c},\, K_c]$ auf dem Edge-Raum ist
der geometrische Ausdruck dieser Inkompatibilität.
Theorem B sagt: er **kollabiert nicht**.

---

## Warum BW-Doubling die Koerzivität erzwingt

$$
\langle (A_{N,c} - K_c)\psi_{n^*}, \psi_{n^*}\rangle
= \underbrace{\mathcal{E}_{\mathrm{out}}(|\psi_{n^*}|^2)}_{\ge\, c_0^{\mathrm{III}} > 0}
- \underbrace{\text{(PNT-Korrektur)}}_{= O(\log N / \sqrt{N}) \to 0}
$$

Die out-of-band Energie (BW-Doubling, Paper III) ist genau der Anteil,
den $\mu_{\mathrm{arith}}$ von der spektralen Geometrie abweicht.
PNT sorgt dafür, dass die arithmetische Korrektur diesen Anteil
nicht auslöschen kann.

**Deshalb:** die Differenzform ist positiv auf $\psi_{n^*}$,
unabhängig davon, ob $\lambda_{n^*}$ groß oder klein ist.

---

## RH als Schließpunkt

Unter RH wird die Explicit Formula zu einer
Reproducing-Kernel-Paarung:

$$
\sum_j \Lambda(p_j)\, f(p_j)
= \hat{f}(0) - \sum_{\rho}\hat{f}(\rho) + \text{Fehler}
$$

Das identifiziert $A_{N,c}$ mit einem Spektralmaß auf der
kritischen Linie. Der Defektterm $(E_{N,c})_{n^*n^*}$ wird
dann zu einem Fourier-Trace:

$$
\boxed{\text{Sieht } W(|\psi_{n^*}|^2) > 0
\iff
\hat{\psi}_{n^*}(\tfrac{1}{2} + it) \ne 0}
$$

Edge-Moden tragen per BW-Doubling out-of-band Energie
$\Rightarrow$ ihre Fourier-Transformierten auf der kritischen
Linie verschwinden nicht $\Rightarrow$ $W$ sieht den Defekt.

**Ohne RH:** offen. Das ist der einzige Punkt,
wo RH das Programm schließt.

---

## Statusblock

| Komponente | Status |
|---|---|
| Spektralpositivität $\lambda_k > 0$ | ✔ Slepian 1978 |
| BW-Doubling Obstruction | ✔ Paper III |
| Landau–Widom Mittelwert | ✔ Widom 1964 |
| Funktorstruktur $\mathcal{F}$ | ✔ Paper XXI |
| PNT-Gewichtskorrektur $\to 0$ | ✔ PNT |
| Theorem B (existenziell, $\exists n^*$) | ✔ Paper XXI |
| **Theorem B uniform** ($\inf_{\mathrm{Edge}} > 0$) | **⚠ Paper XXII** |
| **Koerzivität von** $(A_{N,c}-K_c)|_{\mathrm{Edge}}$ | **⚠ Paper XXII** |
| CCM-Ankopplung ohne RH | **⚠ offen** |
| Theorem D ohne GRH | **⚠ offen** |

---

## Open Problem (Paper XXII)

**Problem (Edge Coercivity).**
Zeige oder widerlege:

$$
\inf_{\substack{f \in V_{N,c},\; \|f\|=1\\
\mathrm{spec}(f) \subseteq [(1-\delta)N,\, N)}}
\langle (A_{N,c} - K_c)\,f,\, f\rangle
\;\ge\; c_2(\delta, c) > 0.
$$

Eine positive Antwort:
- macht Theorem B **uniform** über den Edge-Block
- macht $\tilde{c}_0$ **scharf und explizit**
- zeigt, dass die Obstruktion eine **globale geometrische
  Eigenschaft** des Edge-Raums ist,
  nicht nur ein Zeugenphänomen

Zugang: Uniform RKHS-Stabilität von $V_{N,c}$ unter
Primstellen-Sampling im Edge-Regime;
vermutlich Explicit Formula +
quantitative PSWF-Oszillationsabschätzungen
im Airy-Übergangsregime.
