---
layout: post
title: Réduction des endomorphismes en dimension 2 et 3
date: 2026-11-28 14:53 +0100
---
On considère un endomorphisme $u$ d'un $\dK$-espace vectoriel $E$ de dimension $2$ ou $3$. $\dK$ désigne les corps $\dR$ ou $\dC$.

On propose des méthodes efficaces pour trouver une base de $E$ dans laquelle la matrice de $u$ admet une forme simple (une [forme normale de Jordan](https://fr.wikipedia.org/wiki/R%C3%A9duction_de_Jordan) si le polynôme caractéristique est scindé).

## Réduction des endomorphismes en dimension 2

On suppose ici que $\dim E=2$.

### Cas $\chi_u=(X-\lambda)(X-\mu)$

On considère le cas où $\chi_u=(X-\lambda)(X-\mu)$ avec $\lambda\neq\mu$. Comme $\chi_u$ est simplement scindé, $u$ est diagonalisable et il existe une base de $E$ formée de vecteurs propres de $u$ dans laquelle la matrice de $u$ est $\begin{pmatrix}\lambda&0\newline0&\mu\end{pmatrix}$.

**Exemple.** Considérons la matrice $A=\begin{pmatrix}-2&-4\newline3&5\end{pmatrix}$. Alors $\chi_A=(X-1)(X-2)$. La matrice $A$ est donc semblable à $D=\begin{pmatrix}1&0\newline0&2\end{pmatrix}$. On a $\Ker(A-I_2)=\vect(C_1)$ avec $C_1=\begin{pmatrix}4\newline-3\end{pmatrix}$ et $\Ker(A-2I_2)=\vect(C_2)$ avec $C_2=\begin{pmatrix}1\newline-1\end{pmatrix}$. En posant $P=\begin{pmatrix}C_1\mid C_2\end{pmatrix}=\begin{pmatrix}4&1\newline-3&-1\end{pmatrix}$, on a donc $A=PDP^{-1}$.

### Cas $\chi_u=(X-\lambda)^2$

{: #dim2-sp1 }

On considère le cas où $\chi_u=(X-\lambda)^2$.

---

Si $\dim\Ker(u-\lambda\ident_E)=2$, alors il est clair que $u=\lambda\ident_E$ et la matrice de $u$ dans n'importe quelle base de $E$ est $\begin{pmatrix}\lambda&0\newline0&\lambda\end{pmatrix}$.

---

Sinon, $\dim\Ker(u-\lambda\ident_E)=1$. En vertu du théorème de Cayley-Hamilton, $(u-\lambda\ident_E)^2=0$ de sorte que $\Im(u-\lambda\ident_E)\subset\Ker(u-\lambda\ident_E)$. Mais en vertu du théorème du rang, $\dim\Ker(u-\lambda\ident_E)=\dim\Im(u-\lambda\ident_E)=1$ puis $\Ker(u-\lambda\ident_E)=\Im(u-\lambda\ident_E)$.

On peut alors choisir un vecteur $e_2$ dans $E\setminus\Ker(u-\lambda\ident_E)$. En pratique, on peut choisir ce vecteur aléatoirement car il y a peu de chances de tomber sur un vecteur de la droite $\Ker(u-\lambda\ident_E)$. On pose alors $e_1=(u-\lambda\ident_E)(e_2)$ de sorte que $u(e_2)=\lambda e_2+e_1$. De plus, $e_1\in\Im(u-\lambda\ident_E)=\Ker(u-\lambda\ident_E)$ i.e. $u(e_1)=\lambda e_1$. Enfin, $e_2$ n'appartenant pas à la droite $\Ker(u-\lambda\ident_E)$, il n'est pas colinéaire à $e_1$. La famille $(e_1,e_2)$ est donc libre et c'est une base de $E$. La matrice de $u$ dans cette base est $\begin{pmatrix}\lambda&1\newline0&\lambda\end{pmatrix}$.

**Exemple.** Considérons la matrice $A=\begin{pmatrix}-2&2\newline-8&6\end{pmatrix}$. On a $\chi_A=(X-2)^2$. Comme $A\neq2I_2$, $A$ est semblable à $T=\begin{pmatrix}2&1\newline0&2\end{pmatrix}$. Calculons explicitement une matrice de passage. Choisissons $C_2=\begin{pmatrix}1\newline0\end{pmatrix}$ qui n'est clairement pas un vecteur propre de $A$ puis $C_1=(A-2I_2)C_2=\begin{pmatrix}-4\newline-8\end{pmatrix}$. En posant $P=\begin{pmatrix}C_1 \mid C_2\end{pmatrix}=\begin{pmatrix}-4&1\newline-8&0\end{pmatrix}$, on a donc $A=PTP^{-1}$.

### Cas $\chi_u$ irréductible

{: #dim2-irreductible }

Lorsque $\dK=\dR$, $\chi_u$ peut être un polynôme irréductible de degré $2$. Notamment $\chi_u$ ne possède pas de racine réelle et $\sp(u)=\emptyset$.

On choisit un vecteur $e_1$ non nul de $E$. Comme le spectre de $u$ est vide, $e_1$ ne peut être un vecteur propre de $u$ i.e. $u(e_1)$ ne peut être colinéaire à $e_1$. En posant $e_2=u(e_1)$, la famille $(e_1,e_2)$ est donc une base de $E$.

En notant $\chi_u=X^2+aX+b$, $u^2+au+b\ident_E=0$ en vertu du théorème de Cayley-Hamilton. Ainsi $u(e_2)=u^2(e_1)=-be_1-au(e_1)=-be_1-ae_2$. La matrice de $u$ dans la base $(e_1,e_2)$ est donc $\begin{pmatrix}0&-b\newline1&-a\end{pmatrix}$.

**Exemple.** On considère $A=\begin{pmatrix}4&-2\newline7&-2\end{pmatrix}$. Alors $\chi_A=X^2-2X+6$ est irréductible dans $\dR[X]$. En posant $C_1=\begin{pmatrix}1\newline0\end{pmatrix}$, $C_2=AC_1\begin{pmatrix}3\newline7\end{pmatrix}$ et enfin $P=\begin{pmatrix}C_1\mid C_2\end{pmatrix}=\begin{pmatrix}1&3\newline0&7\end{pmatrix}$, on a $A=PMP^{-1}$ avec $M=\begin{pmatrix}0&-6\newline1&2\end{pmatrix}$.

## Réduction des endomoprhismes en dimension $3$

On suppose ici que $\dim E=3$.

### Cas $\chi_u=(X-\lambda)(X-\mu)(X-\nu)$

On considère le cas où $\chi_u=(X-\lambda)(X-\mu)(X-\nu)$ avec $\lambda$, $\mu$ et $\nu$ deux à deux distincts. Comme $\chi_u$ est simplement scindé, $u$ est diagonalisable et il existe une base de $E$ formée de vecteurs propres de $u$ dans laquelle la matrice de $u$ est $\begin{pmatrix}\lambda&0&0\newline0&\mu&0\newline0&0&\nu\end{pmatrix}$.

**Exemple.** Soit $A=A=\begin{pmatrix}
1&-1&1\newline
3&-7&5\newline
9&-21&13
\end{pmatrix}$. On trouve $\chi_A=(X-1)(X-2)(X-4)$. Ainsi $A$ est semblable à $D=\begin{pmatrix}
1&0&0\newline
0&2&0\newline
0&0&4
\end{pmatrix}$. On trouve $\Ker(A-I_3)=\vect(C_1)$ avec $C_1=\begin{pmatrix}1\newline1\newline1\end{pmatrix}$, $\Ker(A-2I_3)=\vect(C_2)$ avec $C_2=\begin{pmatrix}1\newline2\newline3\end{pmatrix}$ et $\Ker(A-4I_3)=\vect(C_3)$ avec $C_3=\begin{pmatrix}1\newline3\newline6\end{pmatrix}$. Ainsi $A=PDP^{-1}$ avec

$$
P=\begin{pmatrix}C_1\mid C_2\mid C_3\end{pmatrix}=\begin{pmatrix}1&1&1\newline1&2&3\newline1&3&6\end{pmatrix}
$$

### Cas $\chi_u=(X-\lambda)^2(X-\mu)$

On considère le cas où $\chi_u=(X-\lambda)^2(X-\mu)$ avec $\lambda\neq\mu$. Remarquons déjà que $\dim\Ker(u-\mu\ident_E)=1$.

---

Si $\dim\Ker(u-\lambda\ident_E)=2$, alors $u$ est diagonalisable et il existe une base de $E$ formée de vecteurs propres de $u$ dans laquelle la matrice de $u$ est $\begin{pmatrix}\lambda&0&0\newline0&\lambda&0\newline0&0&\mu\end{pmatrix}$.

**Exemple.** Soit $A=\begin{pmatrix}
0  & 3  & 2 \newline
2 & 5  & 2 \newline
2  & -3 & 0
\end{pmatrix}$. On calcule $\chi_A=(X-2)^2(X-1)$. On trouve $\Ker(A-2I_3)=\vect(C_1,C_2)$ avec $C_1=\begin{pmatrix}1\newline0\newline1\end{pmatrix}$ et $C_2=\begin{pmatrix}3\newline2\newline0\end{pmatrix}$ et $\Ker(A-I_3)=\vect(C_3)$ avec $C_3=\begin{pmatrix}1\newline1\newline-1\end{pmatrix}$. On a donc bien $A=PDP^{-1}$ avec

$$
D=\begin{pmatrix}2&0&0\newline0&2&0\newline0&0&1\end{pmatrix}
\qquad\text{et}\qquad
P=\begin{pmatrix}C_1\mid C_2\mid C_3\end{pmatrix}=\begin{pmatrix}1&3&1\newline0&2&1\newline1&0&-1\end{pmatrix}
$$

---

Sinon, $\dim\Ker(u-\lambda\ident_E)=1$ et on peut se donner un vecteur directeur $e_1$ de la droite $\Ker(u-\lambda\ident_E)$. D'après le théorème de Cayley-Hamilton et le lemme des noyaux :

$$
E=\Ker(u-\lambda\ident_E)^2\oplus\Ker(u-\mu\ident_E)
$$

Posons $F=\Ker(u-\lambda\ident_E)^2$. On ait que $\dim F=2$ et que $F$ est stable par $u$. Notons $v$ l'endomorphisme de $F$ induit par $u$. En écrivant la matrice de $u$ dans une base adaptée à la décomposition en somme directe précédente, on se rend compte que $\chi_u=\(X-\mu)\chi_v$ de sorte que $\chi_v=(X-\lambda)^2$. De plus,

$$
\Ker(v-\lambda\ident_F)=\Ker(u-\lambda\ident_E)\cap F=\Ker(u-\lambda\ident_E)
$$

car $\Ker(u-\lambda\ident_E)\subset\Ker(u-\lambda\ident_E)^2=F$. Notamment, $\dim\Ker(v-\lambda\ident_F)=1$ et on peut utiliser le cas étudié [plus haut](#dim2-sp1) : il existe une base $(e_1,e_2)$ de $F$ dans laquelle la matrice de $v$ est $\begin{pmatrix}\lambda&1\newline0&\lambda\end{pmatrix}$. En notant $e_3$ un vecteur directeur de la droite $\Ker(u-\mu\ident_E)$, la matrice de $u$ dans la base $(e_1,e_2,e_3)$ est $\begin{pmatrix}\lambda&1&0\newline0&\lambda&0\newline0&0&\mu\end{pmatrix}$.

Par contre, si l'on veut déterminer $e_1$ et $e_2$ comme il a été fait dans le cas étudié [plus haut](#dim2-sp1), il faut déterminer $F=\Ker(u-\lambda\ident_E)^2$. Il est alors plus efficace de déterminer un vecteur directeur $e_1$ de la droite $\Ker(u-\lambda\ident_E)$ et de remarquer que l'on a montré [plus haut](#dim2-sp1) que $\Ker(v-\lambda\ident_F)=\Im(v-\lambda\ident_F)$. Puisque

$$
e_1\in\Ker(u-\lambda\ident_E)=\Ker(v-\lambda\ident_F)=\Im(v-\lambda\ident_F)\subset\Im(u-\lambda\ident_E)
$$

on peut trouver $e_2\in E$ tel que $e_1=(u-\lambda\ident_E)(e_2)$. Puisque $e_1\in\Ker(u-\lambda\ident_E)$, $e_2\in\Ker(u-\lambda\ident_E)^2=F$. Enfin, $(u-\lambda\ident_E)(e_2)=e_1\neq0$ donc $e_2\notin\Ker(u-\lambda\ident_E)=\vect(e_1)$. La famille $(e_1,e_2)$ est donc bien une base de $F$ dans laquelle la matrice de $v$ est $\begin{pmatrix}\lambda&1\newline0&\lambda\end{pmatrix}$.

**Exemple.** Soit $A=\begin{pmatrix}0&-3&-1\newline-1&2&1\newline-2&-3&1\end{pmatrix}$. On trouve $\chi_A=(X-2)^2(X+1)$. On trouve $\Ker(A-2I_3)=\vect(C_1)$ avec $C_1=\begin{pmatrix}1\newline-1\newline1\end{pmatrix}$ et $\Ker(A+I_3)=\vect(C_3)$ avec $C_3=\begin{pmatrix}1\newline0\newline1\end{pmatrix}$. Comme $\dim\Ker(A-2I_3)=1$, on sait que $A$ est semblable à $T=\begin{pmatrix}2&1&0\newline0&2&0\newline0&0&-1\end{pmatrix}$. On cherche alors $C_2$ tel que $(A-2I_3)C_2=C_1$. En résolvant un système, on trouve par exemple $C_2=\begin{pmatrix}0\newline0\newline-1\end{pmatrix}$. On a alors bien $A=PTP^{-1}$ en posant

$$
P=\begin{pmatrix}C_1\mid C_2\mid C_3\end{pmatrix}=\begin{pmatrix}1&0&1\newline-1&0&0\newline1&-1&1\end{pmatrix}
$$

### Cas $\chi_u=(X-\lambda)^3$

On considère le cas où $\chi_u=(X-\lambda)^3$. Pour simplifier, on pose $v=u-\lambda\ident_E$. D'après le théorème de Cayley-Hamilton, $v^3=0$.

---

Si $\dim\Ker v=3$, alors $u=\lambda\ident_E$ et la matrice de $u$ dans n'importe quelle base de $E$ est $\begin{pmatrix}\lambda&0&0\newline0&\lambda&0\newline0&0&\lambda\end{pmatrix}$.

---

Supposons maintenant que $\dim\Ker v=2$. On se donne une base $(e_1,e_2)$ de $\Ker v$. Comme $\Ker v\subset\Ker v^2$, $\dim\Ker v^2\in\\{2,3\\}$. Supposons que $\dim\Ker v^2=2$, alors $\Ker v=\Ker v^2$ puis $v^{-1}(\Ker v)=v^{-1}(\Ker v^2)$ i.e. $\Ker v^2=\Ker v^3$. Ainsi $\Ker v=\Ker v^2=\Ker v^3=E$, ce qui est incompatible avec la dimension de $\Ker v$. On a donc $\dim\Ker v^2=3$ i.e. $v^2=0$. On en déduit que $\Im v\subset\Ker v$. On choisit alors un vecteur $e_3\in E\setminus\Ker v$. En pratique, on peut le choisir aléatoirement. On pose alors $e_2=v(e_3)\in\Im v\subset\Ker v$. On choisit enfin dans $\Ker v$ un vecteur $e_1$ non colinéaire à $e_2$. Comme $e_3\notin\Ker v=\vect(e_1,e_2)$, $(e_1,e_2,e_3)$ est une base de $E$ et la matrice de $u$ dans cette base est $\begin{pmatrix}\lambda&0&0\newline0&\lambda&1\newline0&0&\lambda\end{pmatrix}$.

**Exemple.** Soit $A=\begin{pmatrix}
4 & 1 & -1\newline
2 & 5 & -2\newline
3 & 3 & 0
\end{pmatrix}$. On calculde $\chi_A=(X+3)^3$. On voit que $\Ker(A-3I_3)=\vect\left(\begin{pmatrix}1\newline-1\newline0\end{pmatrix},\begin{pmatrix}1\newline0\newline1\end{pmatrix}\right)$. Notamment, $\dim\Ker(A-3I_3)=2$ de sorte que $A$ est semblable à $T=\begin{pmatrix}3&0&0\newline0&3&1\newline0&0&3\end{pmatrix}$. Posons $C_3=\begin{pmatrix}1\newline0\newline0\end{pmatrix}$, $C_2=(A-3I_3)C_3=\begin{pmatrix}1\newline2\newline3\end{pmatrix}$ et enfin $C_1=\begin{pmatrix}1\newline-1\newline0\end{pmatrix}$ qui appartient bien à $\Ker(A-3I_3)$ mais n'est pas colinéaire à $C_2$. Alors on a bien $A=PTP^{-1}$ en posant

$$
P=\begin{pmatrix}C_1\mid C_2\mid C_3\end{pmatrix}=\begin{pmatrix}
1&1&1\newline
-1&2&0\newline
0&3&0
\end{pmatrix}
$$

---

Supposons enfin que $\dim\Ker v=1$. D'après le théorème du rang, $\dim\Im v=2$. Puisque $v^3=0$, $\Im v\subset\Ker v^2$. Ainsi $\dim\Ker v^2\geq2$. De plus, on ne peut avoir $v^2=0$, car sinon on aurait $\Im v\subset\Ker v$, ce qui est incompatible avec les dimensions de $\Im v$ et $\Ker v$. Ainsi $\dim\Ker v^2=2$. On peut alors choisir $e_3\in E\setminus\Ker v^2$. En pratique, on peut choisir $e_3$ aléatoirement car il y a peu de chances de tomber sur un vecteur du plan $\Ker v^2$. On pose alors $e_2=v(e_3)$ et $e_1=v(e_2)$. Remarquons alors que $e_2\in\Ker v^2\setminus\Ker v$ et que $e_1\in\Ker v$. Comme $\dim\Ker v=1$ et $\dim\Ker v^2=2$, on obtient $\Ker v=\vect(e_1)$ et $\Ker v^2=\vect(e_1,e_2)$. Ainsi $e_2\notin\Ker v=\vect(e_1)$ et $e_3\notin\Ker v^2=\vect(e_1,e_2)$. La famille $(e_1,e_2,e_3)$ est donc une base de $E$ et la matrice de $u$ dans cette base est $\begin{pmatrix}\la&1&0\newline0&\la&1\newline0&0&\lambda\end{pmatrix}$.

**Exemple.** Soit $A=\begin{pmatrix}-2&0&-1\newline2&-4&-5\newline-1&1&0\end{pmatrix}$. On trouve $\chi_A=(X+2)^3$. On voit aisément que $\rg(A+2I_3)=2$ de sorte que $\dim\Ker(A+2I_3)=1$. On sait alors que $A$ est semblable à $T=\begin{pmatrix}-2&1&0\newline0&-2&1\newline0&0&-2\end{pmatrix}$. On pose alors $C_3=\begin{pmatrix}1\newline0\newline0\end{pmatrix}$, $C_2=(A+2I_3)C_3=\begin{pmatrix}0\newline2\newline-1\end{pmatrix}$ et $C_1=\begin{pmatrix}1\newline1\newline0\end{pmatrix}$. On a lors bien on a bien $A=PTP^{-1}$ en posant

$$
P=\begin{pmatrix}C_1\mid C_2\mid C_3\end{pmatrix}=\begin{pmatrix}
1&0&1\newline
1&2&0\newline
0&-1&0
\end{pmatrix}
$$

### Cas $\chi_u=(X-\lambda)P$ et $P$ irrédudctible

Lorsque $\dK=\dR$, $\chi_u$ peut être de la forme $(X-\lambda)P$ avec $P$ un polynôme unitiare irréductible de degré $2$. Comme $X-\lambda$ et $P$ sont premiers entre eux, on obtient avec le théorème de Cayley-Hamilton et le lemme des noyaux

$$
E=\Ker P(u)\oplus\Ker(u-\lambda\ident_E)
$$

De plus, $Q(u)\circ(u-\lambda\ident_E)=0$ donc $\Im(u-\lambda\ident_E)\subset\Ker(u-\lambda\ident_E)$. Mais d'après le théorème du rang,

$$
\dim\Im(u-\lambda\ident_E)=\dim E-\dim\Ker(u-\lambda\ident_E)=\dim\Ker P(u)
$$

Ainsi $\Im(u)=\Ker P(u)$. Comme $\Ker P(u)$ est stable par $u$, on peut considérer l'endomorphisme $v$ de $\Ker P(u)$ induit par $u$. Quitte à considérér la matrice de $u$ dans une base adaptée à la décomposition $E=\Ker P(u)\oplus\Ker(u-\lambda\ident_E)$, on montre que $\chi_v=P$. D'après un cas étudié [plus haut](#dim2-irreductible), en choissisant un vecteur non nul $e_1$ dans $\Ker P(u)=\Im u$ et en notant $e_2=u(e_1)$, $(e_1,e_2)$ est une base de $\Ker P(u)$ et la matrice de $v$ dans cette base est $\begin{pmatrix}0&-b\newline1&-a\end{pmatrix}$ si $P=X^2+aX+b$. Il suffit alors de se donner un vecteur directeur $e_3$ de la droite $\Ker(u-\lambda\ident_E)$ pour obtenir une base $(e_1,e_2,e_3)$ de $E$. La matrice de $u$ dans cette base est alors $\begin{pmatrix}0&-b&0\newline1&-a&0\newline0&0&\lambda\end{pmatrix}$.

**Exemple.** Soit $A=\begin{pmatrix}
5 & 6 & -3 \newline
-8 & -8 & 6 \newline
-2 & -1 & 3
\end{pmatrix}$. On trouve $\chi_A=(X-2)(X^2+2X+3)$. La matrice $A$ est donc semblable à $M=\begin{pmatrix}
0&-3&0\newline
1&-2&0\newline
0&0&2
\end{pmatrix}$. On trouve $\Ker(A-2I_3)=\vect(C_3)$ avec $C_3=\begin{pmatrix}1\newline1\newline3\end{pmatrix}$. Remarquons ensuite que la première colonne de $A-2I_3$ est bien dans $\Im(A-2I_3)$. On prend donc $C_1=\begin{pmatrix}3\newline-8\newline-2\end{pmatrix}$ et $C_2=AC_1=\begin{pmatrix}-27\newline28\newline-4\end{pmatrix}$. On a alors bien $A=PMP^{-1}$ en posant

$$
P=\begin{pmatrix}C_1\mid C_2\mid C_3\end{pmatrix}=\begin{pmatrix}
3&-27&1\newline
-8&28&1\newline
-2&-4&3
\end{pmatrix}
$$
