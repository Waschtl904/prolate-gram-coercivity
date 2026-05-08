# Die Hebelstelle des Programms

**Stand nach Commit `5a598ee` (Paper XXI)**

Die gesamte Theorie ist auf **eine einzige strukturelle Frage** reduziert.

---

## Die kanonische Endform

$$
\boxed{
\text{Prolate–Weil Obstruktion}
\;\equiv\;
\text{Nicht-Koerzivität von }
A_{N,c} - K_c \text{ auf Edge}
}
$$

Mit
$$
A_{N,c} := \frac{1}{N}\mathrm{Ev}_N^*\mathrm{Ev}_N,
\qquad K_c := \mathcal{K}_c,
$$
ist die gesamte Obstruktionsstruktur äquivalent zur Frage:

$$
\boxed{
\inf_{\substack{f \in \mathrm{Edge}\\ \|f\|=1}}
\langle (A_{N,c} - K_c)\,f,\, f\rangle
\;\stackrel{?}{>}\; 0
}
$$

---

## Die drei logischen Welten

| Regime | Aussage | Bedeutung |
|---|---|---|
| **Bulk** | $A_{N,c} \approx K_c$ | Gleiche RKHS-Geometrie; Sampling funktioniert |
| **Edge (existenziell)** | $\exists f_{n^*}: \langle(A_{N,c}-K_c)f_{n^*},f_{n^*}\rangle \ge \tilde{c}_0 > 0$ | Singulärer Zeuge trägt Obstruktion (Theorem B ✓) |
| **Edge (uniform)** | $\inf_{\mathrm{Edge}} \langle(A_{N,c}-K_c)f,f\rangle > 0$ | Edge-Raum vollständig entkoppelt (Paper XXII) |

Der Unterschied zwischen Zeile 2 und Zeile 3:
$$
\boxed{\exists \;\ne\; \forall}
$$
nicht trivial, sondern als: **lokale Instabilität** vs. **globale geometrische Trennung**.

---

## Operatoralgebraische Charakterisierung (XXII-Proposition)

Sei $\Pi_{\mathrm{Edge}}$ der Spektralprojektor auf den Edge-Block.
Definiere den **Randkompressions-Operator**:

$$
D_{\mathrm{Edge}} := \Pi_{\mathrm{Edge}}\,(A_{N,c} - K_c)\,\Pi_{\mathrm{Edge}}
: \mathrm{Edge} \to \mathrm{Edge}.
$$

Dann:

$$
\boxed{
\|(A_{N,c}-K_c)|_{\mathrm{Edge}}\|_{\mathrm{coercive}} > 0
\;\iff\;
\inf\,\sigma(D_{\mathrm{Edge}}) > 0
\;\iff\;
D_{\mathrm{Edge}} \text{ ist positiv definit auf Edge}
}
$$

**Proposition-Kandidat für Paper XXII.**
*Sei $N = \lfloor \alpha c \rfloor$, $\alpha < 2/\pi$,
$\mathrm{Edge} = \Pi_{[(1-\delta)N, N)} V_{N,c}$. Dann:*

$$
\sigma(D_{\mathrm{Edge}}) \subseteq [c_2(\delta,c),\, 1]
\quad \text{mit } c_2(\delta,c) > 0,
$$

*d.h. $D_{\mathrm{Edge}}$ ist gleichmäßig positiv definit auf dem Edge-Block.*

Das wäre die **endgültige operatoralgebraische Form** der Prolate–Weil-Obstruktion.

---

## Warum das äquivalent zur Koerzivität ist

Der Spektralradius von $D_{\mathrm{Edge}}$ von unten:

$$
\inf\,\sigma(D_{\mathrm{Edge}})
= \inf_{\substack{f \in \mathrm{Edge}\\ \|f\|=1}}
\langle D_{\mathrm{Edge}}\,f,\,f\rangle
= \inf_{\substack{f \in \mathrm{Edge}\\ \|f\|=1}}
\langle (A_{N,c}-K_c)\,f,\,f\rangle.
$$

Die drei Schritte zum Beweis der positiven Definitheit:

1. **BW-Doubling** (Paper III): für jedes $f \in \mathrm{Edge}$,
   $\mathcal{E}_{\mathrm{out}}(|f|^2) \ge c_0^{\mathrm{III}} \|f\|^2$
   (im existenziellen Sinne: mindestens ein $f = \psi_{n^*}$).

2. **Spektralpositivität**: $\lambda_k \ge \lambda_{\min}(N,c) > 0$
   konvertiert out-of-band Energie in Normunterschied.

3. **PNT-Kontrolle**: arithmetische Korrektur
   $O(\log N/\sqrt{N}) \ll c_0^{\mathrm{III}}$
   für $N \ge N_0$.

Schritte 1–3 liefern
$\langle D_{\mathrm{Edge}} \psi_{n^*}, \psi_{n^*}\rangle \ge \tilde{c}_0$
(**existenziell, Theorem B**).

Den Sprung zum **uniformen** $\inf\,\sigma(D_{\mathrm{Edge}}) > 0$
braucht man:
- entweder **uniformes BW-Doubling** über den gesamten Edge-Block;
- oder **RKHS-Stabilität** von $\mathrm{Ev}_N$ auf Edge-Moden;
- oder beides via **Airy-Oszillationsabschätzungen**.

---

## RH als Schließpunkt

Unter RH identifiziert die Explicit Formula $A_{N,c}$ mit einem
Spektralmaß auf der kritischen Linie $\{\tfrac{1}{2}+it\}$:

$$
\text{RH} \iff \sigma(D_{\mathrm{Edge}}) \text{ wird durch Weil-Nullstellen geometrisch kontrolliert}
$$

Ohne RH bleibt $\inf\,\sigma(D_{\mathrm{Edge}})$ offen — das ist der einzige Punkt,
wo RH das Programm schließt.

$$
\boxed{
\text{RH} \iff
\text{Koerzivität wird eliminierbar}
\iff
\inf\,\sigma(D_{\mathrm{Edge}}) \xrightarrow{\mathrm{RH}} 0
}
$$

*(Unter RH kollabiert die Obstruction nicht — aber sie wird
durch die Nullstellen-Geometrie kanonisch erklärt und
in $\mathbf{QF}_{\lim}$ repräsentierbar.)*

---

## Statusblock

| Komponente | Status |
|---|---|
| Spektralpositivität $\lambda_k > 0$ | ✔ Slepian 1978 |
| BW-Doubling (existenziell) | ✔ Paper III |
| Landau–Widom Mittelwert | ✔ Widom 1964 |
| Funktorstruktur $\mathcal{F}$ | ✔ Paper XXI |
| PNT-Gewichtskorrektur $\to 0$ | ✔ PNT |
| $D_{\mathrm{Edge}}$ hat positiven Eigenwert ($\exists$) | ✔ Paper XXI, Theorem B |
| **$\inf\,\sigma(D_{\mathrm{Edge}}) > 0$ (uniform)** | **⚠ Paper XXII** |
| **BW-Doubling uniform über Edge-Block** | **⚠ Paper XXII** |
| CCM-Ankopplung ohne RH | **⚠ offen** |
| Theorem D ohne GRH | **⚠ offen** |

---

## Paper XXII: Das Programm in einem Satz

> Zeige $\inf\,\sigma(D_{\mathrm{Edge}}) \ge c_2(\delta,c) > 0$
> durch uniforme RKHS-Stabilität von $\mathrm{Ev}_N$
> auf PSWF-Edge-Moden im Airy-Übergangsregime.
