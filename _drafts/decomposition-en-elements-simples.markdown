---
title: "Décomposition en éléments simples"
published: true
---

On expose ici la décomposition en éléments simples dans le cas d'un corps $\dK$ quelconque.


**Lemme**. Soient $P\in\dK[X]$, $R$ un polynôme irréductible de $\dK[X]$ de degré $r$ et $n\in\dN^*$. Alors il existe $E\in\dK[X]$ et $(P_1,\dots,P_n)\in\dK_{n-1}[X]^r$ tels que

$$
\frac{P}{R^n}=E+\sum_{k=1}^n\frac{P_k}{R^k}
$$

*Preuve*. On procède par récurrence sur $n$. La propriété à montrer est clairement vraie pour $n=0$ (en convenant qu'une somme indexée sur le vide est nulle). On suppose alors la propriété vraie à un certain rang $n\in\dN$. On note $\tilde P$ et $P_{n+1}$ le quotient et le reste de la division euclidienne de $P$ par $R$. On a alors $P=\tilde PR+P_{n+1}$ et $\deg P_{n+1}\leq r-1$ puis $\displaystyle\frac{P}{R^{n+1}}=\frac{\tilde P}{R^n}+\frac{P_{n+1}}{R^{n+1}}$. Par hypothèse de récurrence, il existe $(P_1,\dots,P_n)\in\dK_{n-1}[X]^r$ tels que $\displaystyle\frac{\tilde P}{R^n}=E+\sum_{k=1}^n\frac{P_k}{R^k}$. On a alors bien $\displaystyle\frac{P}{R^{n+1}}=E+\sum_{k=1}^{n+1}\frac{P_k}{R^k}$ avec $(P_1,\dots,P_{n+1})\in\dK_{r-1}[X]^{n+1}$.


*Preuve*.

* **Existence**. Puisque $R_1^{m_1},\dots,R_n^{m_n}$ sont premiers entre eux deux à deux. On prouve alors aisément que les polynômes $\displaystyle Q_j=\prod_{k\neq j}R_k^{(m_k)}$ sont premiers entre eux dans leur ensemble. D'après le théorème de Bézout, il existe donc $(U_1,\dots,U_n)\in\dK[X]^n$ tel que $\displaystyle\sum_{j=1}^nU_jQ_j=1$. On obtient alors $\displaystyle\frac{P}{Q}=\sum_{j=1}^n\frac{PU_j}{R_j^{m_j}}$. D'après le lemme, pour tout $j\in\lb1,n\rb$, il existe $E_j\in\dK[X]$ et $(P_{j,1},\dots,P_{j,m_j})\in\dK_{r_j-1}[X]^{m_j}$ tel que $\displaystyle\frac{PU_j}{R_j^{m_j}}=\sum_{k=1}^{m_j}\frac{P_{j,k}}{R_j^k}$. En posant $E=\sum_{j=1}^nE_j\in\dK[X]$, on a bien

$$
\frac{P}{Q}=E+\sum_{j=1}^n\sum_{k=1}^{m_j}\frac{P_{j,k}}{R_j^k}
$$

* **Unicité**. Supposons que

$$
\frac{P}{Q}=E+\sum_{j=1}^n\sum_{k=1}^{m_j}\frac{P_{j,k}}{R_j^k}=F+\sum_{j=1}^n\sum_{k=1}^{m_j}\frac{Q_{j,k}}{R_j^k}
$$

Alors $E-F$ est une fraction rationnelle de degré strictement négatif mais c'est également un polynôme donc ce ne peut être que le polynôme nul. Ainsi $E=F$.
