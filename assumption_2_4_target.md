# Assumption 2.4 — Beweisbare Zielgestalten

> **Kontext.** Die Kette
> ```
> Paper IV thm:weak-limit
>   → Paper III lem:bulk-reduction (Lemma 6.3)
>   → Paper III prob:comm-refined
>   → Bulk tail bound ‖(I−P_N)f_{mn}‖ ≤ Ce^{−αN}
> ```
> ist vollständig — aber der letzte Schritt braucht:
> **Paper II Assumption 2.4** = uniforme L²-Bound auf den Bulk-Projektionskern.
>
> Dieses Dokument formuliert drei explizite, beweisbare Zielgestalten.
> Jede ist eine hinreichende Bedingung für das Programm.
> Die einfachste (Variante A) ist wahrscheinlich direkt beweisbar.

---

## Was Ass. 2.4 strukturell braucht

Der Kern des Problems ist der prolate Projektionsoperator

$$
(P_N f)(x) = \sum_{n=0}^{N-1} \langle f, \psi_n^{(c)} \rangle \psi_n^{(c)}(x)
= \int_{-T}^{T} K_N(x,y)\, f(y)\, dy,
$$

mit dem Christoffel-Darboux-Kern

$$
K_N(x,y) = \sum_{n=0}^{N-1} \psi_n^{(c)}(x)\, \psi_n^{(c)}(y).
$$

Das Programm braucht eine **uniforme Operatornorm-Kontrolle** in der Form:

$$
\text{Ass. 2.4:}\quad
\left\| \int_{-T}^{T} K_N(x,y)\, f(y)\, dy \right\|_{L^2_\mu(\text{bulk})}
\leq C \| f \|_{L^2([-T,T])},
\quad \text{uniform in } N, c, \text{ bulk sector}.
$$

**Der qualitative Unterschied zu Paper IV:**

| | Paper IV | Ass. 2.4 |
|---|---|---|
| Aussage | für festes $f \in C^1$, punktweise | für *alle* $f \in L^2$, Operatornorm |
| Methode | Oszillationsmittelung | Kernel-Struktur / Schur |
| Natur | semiklassisch | funktionalanalytisch |

---

## Variante A: Schur-Test (empfohlen, direkt angreifbar)

### Ziellemma A

> **Lemma (Schur-Kontrolle des CD-Kerns im Bulk).**
> Sei $I_\delta = [-(1-\delta)T, (1-\delta)T]$ für $\delta > 0$ fest.
> Dann gilt uniform in $N \leq \gamma N_{\rm Sh}$ (mit $N_{\rm Sh} = 2c/\pi$):
>
> $$
> \sup_{x \in I_\delta} \int_{-T}^{T} |K_N(x,y)|\, dy \leq C_{\delta,\gamma},
> \qquad
> \sup_{y \in [-T,T]} \int_{I_\delta} |K_N(x,y)|\, dx \leq C_{\delta,\gamma}.
> $$
>
> Der Schur-Test liefert dann $\| P_N \|_{L^2 \to L^2(I_\delta)} \leq C_{\delta,\gamma}$.

### Beweisstrategie für Lemma A

**Schritt 1: Diagonal-Bound.**
Aus Paper IV `lem:bohr-sommerfeld-pswf` und `lem:amplitude-drift`:
$$
K_N(x,x) = \sum_{n=0}^{N-1} \psi_n^{(c)}(x)^2
\leq \sum_{n=0}^{N-1} \frac{C r_n(x)^2}{1} \leq C \sum_{n=0}^{N-1} \lambda_n \rho_n^{\rm cl}(x).
$$
Mit $\rho_n^{\rm cl}(x) \sim 1/(\pi K_n \omega_n^{\rm cl}(x))$ und $K_n \sim \pi/\lambda_n$:
$$
K_N(x,x) \lesssim \sum_{n=0}^{N-1} \frac{\omega_n^{\rm cl}(x)}{\pi} \lesssim N \cdot \frac{c}{\pi T},
$$
da $\omega_n^{\rm cl}(x) \leq c/T$ für $x \in I_\delta$. Das ist der **Landau-Widom Diagonal-Bound**.

**Schritt 2: Off-diagonal Decay.**
Der CD-Kern hat die WKB-Darstellung (formal):
$$
K_N(x,y) \approx \sum_{n=0}^{N-1} \frac{\sin(\theta_n(x) - \theta_n(y))}{\pi(\theta_n(x) - \theta_n(y))} \cdot \frac{1}{\sqrt{p(x)p(y)}\, \omega_n^{\rm cl}},
$$
also ein gewichtetes Summe von Sinc-artigen Kernen.
Für $|x-y| \geq 1/n$: Abfall wie $1/|x-y|$.
Für $|x-y| \leq 1/n$: kontrolliert durch den Diagonal-Bound.

**Schritt 3: Schur-Integral.**
$$
\int_{-T}^{T} |K_N(x,y)|\, dy
\leq K_N(x,x)^{1/2} \cdot \left( \int_{-T}^{T} K_N(y,y)\, dy \right)^{1/2}
= K_N(x,x)^{1/2} \cdot N^{1/2}
$$
Das ist zu grob (gibt $O(N)$, nicht $O(1)$).
Besser: direktes Schur mit $|K_N(x,y)| \leq C(N/T) \cdot \min(1, (N/c|x-y|)^{-1})$:
$$
\int_{-T}^{T} |K_N(x,y)|\, dy \leq \frac{CN}{T} \int_0^T \min\!\left(1, \frac{1}{N|x-y|/c}\right) dy
\leq \frac{CN}{T} \cdot \frac{c}{N} \cdot (1 + \log(NT/c)).
$$
Da $c \leq \pi N_{\rm Sh}/2$ und $N \leq \gamma N_{\rm Sh}$:
$$
\sup_{x} \int |K_N(x,y)|\, dy \leq C_{\delta,\gamma} (1 + \log(1/\gamma)).
$$

**Fazit Variante A:** Dieser Weg ist vollständig durchführbar mit bekannten PSWF-Schranken
aus ORX Kap. 6. Das zentrale Input ist der Diagonal-Bound
$K_N(x,x) \leq CN\omega/\pi$, der aus dem Landau-Widom-Theorem folgt.

### Klassischer Satz dahinter

> **Schur-Test** (Schur 1911, [Reed-Simon I, Thm. VI.23]):
> Sei $K: L^2(\mu) \to L^2(\nu)$ ein Integraloperator mit Kern $k(x,y)$.
> Existieren $h > 0$ messbar mit
> $\int |k(x,y)| h(y) d\mu(y) \leq C h(x)$
> und $\int |k(x,y)| h(x) d\nu(x) \leq C h(y)$,
> dann $\|K\|_{L^2 \to L^2} \leq C$.
>
> Im Bulk: wähle $h \equiv 1$ und verifiziere die zwei Schur-Integrale wie oben.

---

## Variante B: Pseudodifferentielle Approximation

### Ziellemma B

> **Lemma (PseudoDO-Darstellung von $P_N$).**
> Im Bulk $I_\delta$ gilt:
> $$
> P_N = \mathrm{Op}(\mathbf{1}_{|\xi| \leq \omega_N^{\rm cl}(x)}) + R_N,
> \qquad \|R_N\|_{L^2 \to L^2} \leq \frac{C_{\delta,\gamma}}{\sqrt{N}},
> $$
> wobei $\mathrm{Op}$ der Weyl-Quantisierung auf dem bulk-Symbol entspricht.

### Beweisstrategie für Lemma B

Der Operator $P_N = \chi(D_c \leq \chi_N)$ ist der Spektralprojektor des
Sturm-Liouville-Operators $D_c$ unterhalb der $N$-ten Eigenfrequenz.

- Im Bulk gilt $D_c \approx -\partial_x^2 + V_c(x)$ mit $V_c(x) = c^2x^2/T^2/(1-x^2/T^2)$.
- Nach dem Egorov-Theorem / symbolischer Kalkül ist $P_N$ moduliert pseudodifferentiell:
  das Hauptsymbol ist $\mathbf{1}_{\{\xi^2 + V_c(x) \leq \chi_N\}}$,
  was genau der Bulk-Sektor $|\xi| \leq \omega_N^{\rm cl}(x)$ ist.
- Der Rest $R_N$ kommt aus dem Turning-Point-Fehler (Airy-Korrektur)
  und ist $O(c^{-1/3})$ in Operatornorm.

Das ist technisch aufwändiger als Variante A, aber liefert eine stärkere Aussage:
nicht nur die Operatornorm, sondern auch den funktionalen Kalkül von $P_N$.

### Klassischer Satz dahinter

> **Egorov-Theorem** (Egorov 1969, [Zworski, Semiclassical Analysis, Thm. 11.1]):
> Sei $P = \mathrm{Op}(p)$ ein selbstadjungierter PseudoDO, $A = \mathrm{Op}(a)$.
> Dann $e^{itP} A e^{-itP} = \mathrm{Op}(a \circ \Phi_t) + O(\hbar)$
> wo $\Phi_t$ der Hamiltonfluss zu $p$ ist.
> Angewendet auf $P = D_c$, $A = P_N$: liefert symbolische Kontrolle von $P_N$ im Bulk.

**Severity für das Programm:** Diese Variante ist deutlich technischer als Variante A
und nicht notwendig für das Bulk-Programm.
Sie wäre relevant wenn man auch Operatornorm-Bounds für die Off-diagonal-Terme braucht.

---

## Variante C: Kernel Splitting (direkte PSWF-Methode)

### Ziellemma C

> **Lemma (Kernel Splitting im Bulk).**
> Schreibe $K_N = K_N^{\rm diag} + K_N^{\rm off}$ mit
> $$
> K_N^{\rm diag}(x,y) := K_N(x,y) \cdot \mathbf{1}_{|x-y| \leq c/N},
> \qquad
> K_N^{\rm off}(x,y) := K_N(x,y) \cdot \mathbf{1}_{|x-y| > c/N}.
> $$
> Dann:
> - $\| \mathrm{Op}(K_N^{\rm diag}) \|_{L^2 \to L^2} \leq C_{\delta,\gamma}$ (Young-Ungleichung)
> - $\| \mathrm{Op}(K_N^{\rm off}) \|_{L^2 \to L^2} \leq C_{\delta,\gamma}$ (Riemann-Lebesgue)

### Beweisstrategie für Lemma C

Für den diagonalen Teil:
$$
\| \mathrm{Op}(K_N^{\rm diag}) f \|_{L^2}^2
\leq \left( \sup_x \int |K_N^{\rm diag}(x,y)| dy \right) \cdot \| f \|_{L^2}^2.
$$
Mit $K_N(x,x) \leq CN^2/c$ (Diagonal-Bound) und $|K_N(x,y)| \leq K_N(x,x)$
für $|x-y| \leq c/N$:
$$
\int_{|x-y| \leq c/N} |K_N(x,y)| dy \leq K_N(x,x) \cdot \frac{2c}{N} \leq C.
$$

Für den off-diagonalen Teil: Slepians Reproduktionskern-Formel
$$
K_N(x,y) = \frac{c}{\pi} \frac{\sin(c(x-y)/T)}{c(x-y)/T} + \text{Korrekturen},
$$
gibt $|K_N^{\rm off}(x,y)| \leq C T / (c|x-y|)$ für $|x-y| > c/N$, also:
$$
\int_{|x-y|>c/N}^T \frac{C T}{c|x-y|} dy \leq C(1 + \log(NT/c)).
$$

### Klassische Sätze dahinter

> **Young-Ungleichung**: $\| K \|_{L^2 \to L^2} \leq \| K \|_{L^1(dy)}$
> wenn $\sup_x \int |K(x,y)| dy < \infty$ (das ist Schur mit $h \equiv 1$).
>
> **Slepian 1964** [Slepian, Bell Syst. Tech. J., Eq. 3.6]: Explizite Formel
> für $K_N(x,y)$ als Sinc-Kern mit PSWF-Korrekturen.

---

## Zusammenfassung: Welche Variante für das Programm?

| Variante | Methode | Stärke | Technischer Aufwand | Empfehlung |
|---|---|---|---|---|
| **A: Schur-Test** | Diagonal-Bound + Schur | $\|P_N\|_{L^2 \to L^2} \leq C$ | Niedrig | **Jetzt angehen** |
| B: PseudoDO | Egorov-Theorem | Symbolische Kontrolle | Hoch | Für späteres Paper |
| C: Kernel Splitting | Young + Slepian-Sinc | Expliziter Kern | Mittel | Alternative zu A |

**Variante A ist der richtige nächste Schritt.** Alle Inputs sind bereits im Programm:
- Diagonal-Bound $K_N(x,x) \leq CN\omega/\pi$: folgt aus Landau-Widom + Paper IV `lem:normalization`
- Off-diagonal Abfall: folgt aus Sinc-Struktur des CD-Kerns (Slepian 1964)
- Schur-Test: klassisches funktionalanalytisches Standardresultat

Das würde Ass. 2.4 zu einem bewiesenen Lemma machen und die Kette
$$
\text{Paper IV} \Rightarrow \text{Paper III} \Rightarrow \text{Bulk tail bound (unconditional)}
$$
vollständig schließen — **ohne neue externe Annahmen**.

---

## Verbindung zu Paper III Ass. 3.1 (Off-diagonal)

Variante B (PseudoDO) würde auch Ass. 3.1 abdecken:
die Phasenentkopplung $\theta_m - \theta_n$ für $|m-n| \geq \delta N$
ist im symbolischen Kalkül die Separation der Hamiltonfluss-Orbits,
die für gut-getrennte Wendepunkte $x_+(m) \neq x_+(n)$ automatisch folgt.
Aber: das ist nicht notwendig für den Bulk-Kern — nur ein Bonus.

---

*Erstellt nach Commit b8b16e2 (Paper IV) und ac82ec7 (DEPENDENCIES), April 2026.*
