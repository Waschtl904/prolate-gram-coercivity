# Die Hebelstelle des Programms

**Stand nach Commit `5a598ee` (Paper XXI)**

Nach der Eliminierung aller asymptotischen Eigenwert-Argumente
ist die gesamte Struktur auf **einen einzigen verbleibenden
Freiheitsgrad** reduziert.

---

## Die eine strukturelle Gleichung (Kipppunkt)

Theorem B kippt genau dort, wo gilt:

$$
\boxed{
\underbrace{\frac{1}{N}\sum_{j=1}^N |\psi_{n^*}(p_j)|^2}_{\text{arithmetische Probe des Edge-Modus}}
\;=\;
\underbrace{\lambda_{n^*}(c)}_{\text{spektraler Erwartungswert}}
\;+\;
\underbrace{(E_{N,c})_{n^*n^*}}_{\text{sichtbarer Defekt}}
}
$$

Der **Defekt** $(E_{N,c})_{n^*n^*}$ ist genau dann $> 0$,
wenn $\mathrm{Ev}_N$ den Edge-Modus $\psi_{n^*}$
**nicht vollständig im Eigenraum von** $\mathcal{K}_c$ sieht:

$$
\text{Theorem B gilt} \iff
\frac{1}{N}\sum_j |\psi_{n^*}(p_j)|^2
\not\approx \lambda_{n^*}(c)
$$

Anders gesagt:

> **Theorem B kippt genau dann, wenn die Primstellen
> den Edge-Modus $\psi_{n^*}$ so samplen, als wäre er
> ein Bulk-Modus** (d.h. als hätte er out-of-band Energie Null).

---

## Drei äquivalente Formen des Kipppunkts

| Form | Aussage | Sphäre |
|---|---|---|
| **Sampling** | $\|\mathrm{Ev}_N \psi_{n^*}\|^2 \not\approx \lambda_{n^*}(c)\cdot N$ | RKHS-Stabilität |
| **Operator** | $\langle \mathrm{Ev}_N^* \mathrm{Ev}_N \psi_{n^*}, \psi_{n^*}\rangle \ne \langle \mathcal{K}_c \psi_{n^*}, \psi_{n^*}\rangle$ | Kommutator-Versagen |
| **Spektral** | $\mu_{\text{arith}}(|\psi_{n^*}|^2) \ne \lambda_{n^*}(c)$ | Massklass-Singularität |

Alle drei sind dieselbe Aussage, in drei verschiedenen Sprachen.

---

## Warum BW-Doubling hier die Arbeit macht

Der kontinuierliche Raum liefert:

$$
\int_{\mathbb{R}} |\psi_{n^*}|^2 \,dx
= \underbrace{\lambda_{n^*}(c)}_{\text{in-band}}
+ \underbrace{\mathcal{E}_{\mathrm{out}}(|\psi_{n^*}|^2)}_{\ge\, c_0^{\mathrm{III}} > 0}
= 1.
$$

Die arithmetische Probe:

$$
\frac{1}{N}\sum_j |\psi_{n^*}(p_j)|^2
\approx \int |\psi_{n^*}|^2 \,d\mu_{\text{arith}}
= \lambda_{n^*}(c) + (E_{N,c})_{n^*n^*}.
$$

Der Defektterm $(E_{N,c})_{n^*n^*}$ ist **genau der Anteil,
den $\mu_{\text{arith}}$ von $\mathcal{E}_{\mathrm{out}}(|\psi_{n^*}|^2)$ sieht**.

**Hebelstelle:** Wenn $\mu_{\text{arith}}$ die out-of-band Energie
von $\psi_{n^*}$ vollständig ignoriert
(weil die Primstellen im Frequenzraum blind für Energie oberhalb $\omega$ sind),
dann $(E_{N,c})_{n^*n^*} = 0$ und Theorem B kollabiert.

---

## Warum das nicht passiert (heuristisch)

Primstellen samplen $|\psi_{n^*}|^2$ als **reelle Funktion im Zeitraum**,
nicht im Frequenzraum. Die out-of-band Energie von $\psi_{n^*}$
äußert sich als **Nicht-Glätte** von $|\psi_{n^*}|^2$ auf $[-T, T]$ —
genau im Edge-Regime ist $\psi_{n^*}$ **oszillatorisch** (Airy-Übergang),
nicht glättend. Primstellen sind keine gleichmäßige Folge;
aber PNT garantiert, dass sie keine **Nullmenge** in dem für
$\psi_{n^*}$ relevanten Zeitintervall bilden.

Formal wäre ein Beweis über:

$$
\inf_{n \in [(1-\delta)N,N)}
\Bigl|\frac{1}{N}\sum_j |\psi_n(p_j)|^2 - \lambda_n(c)\Bigr|
\ge c_2(\delta, c) > 0
$$

das **uniforme** Resultat, das Theorem B von existenziell
zu global machen würde.

---

## Verbindung zu CCM

Unter RH ist die Explicit Formula:

$$
\sum_{j=1}^N \Lambda(p_j) f(p_j)
= \hat{f}(0) - \sum_{\rho} \hat{f}(\rho) + \text{Fehler}
$$

Das ist genau eine **Reproducing-Kernel-Paarung**:
die Weil-Distribution $W$ wirkt auf $f$ über ihre Nullstellen $\rho$.

Die Hebelstelle lautet damit:

$$
\boxed{
\text{Sieht } W(|\psi_{n^*}|^2) > 0 ?
\iff
\text{Hat die Explicit Formula Energie auf dem Edge-Modus?}
}
$$

Unter RH: ja, weil $\rho = 1/2 + it$ und die
Fourier-Transformierten $\hat{\psi}_{n^*}(\rho)$ für Edge-Moden
nicht verschwinden (sie trägt genau die out-of-band Energie).

**Ohne RH:** offen. Das ist der einzige Punkt,
wo RH das Programm schließt.

---

## Statusblock: Was geschlossen ist, was offen

| Komponente | Status |
|---|---|
| Spektralpositivität $\lambda_k > 0$ | ✔ Slepian 1978 |
| BW-Doubling Obstruction | ✔ Paper III |
| Landau–Widom Mittelwert | ✔ Widom 1964 |
| Funktorstruktur $\mathcal{F}$ | ✔ Paper XXI |
| PNT-Gewichtskorrektur $\to 0$ | ✔ PNT |
| Theorem B (existenziell) | ✔ Paper XXI |
| **Theorem B (uniform über Edge-Block)** | **⚠ offen** |
| **Ev$_N$ stabil auf Edge-Moden** | **⚠ offen** |
| CCM-Ankopplung ohne RH | **⚠ offen** |
| Theorem D (Non-Repr.) ohne GRH | **⚠ offen** |

---

## Open Problem (Paper XXII-Kandidat)

**Problem (Uniform Edge Sampling Stability).**
Sei $n^* \in [(1-\delta)N, N)$. Zeige:

$$
\inf_{n \in [(1-\delta)N,\, N)}
\Bigl(
\frac{1}{N}\sum_{j=1}^N |\psi_n(p_j)|^2 - \lambda_n(c)
\Bigr)
\;\ge\; c_2(\delta, c) > 0.
$$

Eine positive Antwort verwandelt Theorem B in ein
**uniformes geometrisches Resultat** und macht
die Obstruction-Konstante $\tilde{c}_0$ **scharf und explizit**.

Zugang: RKHS-Stabilität von $V_{N,c}$ unter
Primstellen-Sampling im Edge-Regime.
Vermutlich braucht man hier eine Mischung aus
Explicit Formula + quantitative PSWF-Oszillationsabschätzungen
im Airy-Übergangsregime.
