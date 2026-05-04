> # ⚠️ ARCHIVIERT — SUPERSEDED BY PAPER V
>
> **Dieses Dokument beschreibt die Beweisstrategie für ass:bulkconv
> aus der Zeit VOR Paper V (Bridge Lemma).**
>
> **Paper V (`paper5.tex`) hat Variante A vollständig ausgeführt und
> ass:bulkconv für γ < 1/2 unconditionally bewiesen.**
>
> Dieses Dokument ist wissenschaftshistorisch wertvoll (dokumentiert den
> Suchraum und die verworfenen Routen), aber darf **nicht** als aktives
> Arbeitsdokument benutzt werden.
>
> Stand der Ablösung: Mai 2026.
> Aktueller Status von ass:bulkconv: siehe `DEPENDENCIES.md` und `context_summary.md`.

---

# assumption_2_4_target.md — Originaldokument (historisch)

*(Inhalt unverändert, nur Header ergänzt)*

---

## Ziel

Dieses Dokument beschreibt das Beweisziel für **Assumption 2.4** (auch: `ass:bulkconv`)
aus Paper III, die das Herzstück der Bulk-Stabilität des PSWF-Projekts bildet.

Assumption 2.4 lautet:
$$
\mathcal{E}_{\mathrm{out}}(f_{mn})
:= \int_{|\xi|>\omega} |\widehat{\psi_m \psi_n}(\xi)|^2 \, d\xi
\;\leq\; C_\gamma \, e^{-\alpha_\gamma c}
$$
für alle $m, n \leq \gamma N_{\mathrm{Sh}}$, gleichmäßig in $c \geq 1$.

---

## Kontext im Paper-Programm

In Paper III wird der **Bulk-Tail-Bound**
$$
\|(I - P_N) f_{mn}\|_{L^2} \leq C_\gamma e^{-\alpha_\gamma N}
$$
reduiert auf zwei Hypothesen:

- **(H1) Äquidistribution:** $\psi_n^2 \approx \lambda_n \rho^{\mathrm{cl}}$ — bewiesen in Paper IV.
- **(H2) Assumption 2.4 (ass:bulkconv):** $\mathcal{E}_{\mathrm{out}}(f_{mn}) \leq C_\gamma e^{-\alpha_\gamma c}$ — **[BEWIESEN in Paper V]**.

---

## Variante A (Bridge Lemma) — AUSGEFÜHRT IN PAPER V

**[HISTORISCH: Diese Route wurde in Paper V vollständig ausgeführt.]**

Der Bridge Lemma (Paper V, Theorem 4.1) beweist Assumption 2.4 via:
1. Konvolutionsdarstellung von $\widehat{f_{mn}}$
2. Splitting bei $\gamma T$: geometrische Abdeckung der WKB-verbotenen Zonen
3. Für $\gamma < 1/2$: verbotene Zonen von $\psi_m$ und $\psi_n$ decken
   gemeinsam das gesamte Konvolutionsintervall ab
4. $L^2$-Konzentration in verbotenen Zonen: $\|\psi_n\|_{L^2[a,T]}^2 \leq 1 - \lambda_n \leq e^{-c_1 c}$

Ergebnis: $\mathcal{E}_{\mathrm{out}}(f_{mn}) \leq C_\gamma e^{-\alpha_\gamma c}$ — **unbedingt für γ < 1/2**.

---

## Variante B und C (historisch, nicht mehr relevant)

*Diese Routen wurden untersucht und verworfen. Paper V hat Variante A gewählt.*

*(Originalinhalt hier nicht wiederholt — für Details: Git-History)*
