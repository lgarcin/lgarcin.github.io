---
layout: "post"
title: "Signature d'une permutation"
published: true
---

Voici la définition officielle de la signature au programme de MPSI.

**Définition.** Il existe une unique application $\eps$ du groupe symétrique $S_n$ dans $\\{-1,1\\}$ telle que $\eps(\tau)=-1$ pour toute transposition $\tau$ et $\eps(\si\si')=\eps(\si)\eps(\si')$ pour toutes permutations $\si$ et $\si'$.

*Remarque.* En MP, on dira plutôt que la signature est l'unique morphisme non trivial de $S_n$ dans $\\{-1,1\\}$.

L'unicité de la signature est à peu près claire puisque les transpositions engendrent $S_n$. Ainsi, un morphisme de groupe qui est déterminé sur les transpositions est déterminé sur $S_n$ en entier.

L'existence pose plus de problème. Il s'agit de montrer que si une permutation se décompose de deux manières comme un produit de transpositions, les nombres de transpositions intervenant dans ces deux décompositions ont la même parité.


**Lemme.** Soient $\tau_1,\dots,\tau_p$ des transpositions dans $S_n$ et $i\in\lb1,n\rb$. Alors il existe des transpositions $\tau_1',\dots,\tau_q'$ telles que
* $\tau_1\tau_2\dots\tau_p=\tau_1'\tau_2'\dots\tau_q'$ ;
* $p$ et $q$ ont même parité ;
* les supports de $\tau_1',\dots,\tau_{q-1}'$ ne contiennent pas $i$.

*Remarque.* Le support de la "dernière" transposition $\tau_q'$ peut éventuellement contenir $i$.

*Démo.* Pour simplifier, on considérera que des lettres distinctes désignent des entiers de $\lb1,n\rb$ distincts.

---

On traite déjà le cas de deux transpositions $\tau_1$ et $\tau_2$. Si le support de $\tau_1$ ne contient pas $i$, il n'y a rien à faire.
* Si $\tau_1=(i,j)$ et $\tau_2=(k,l)$, alors

$$\tau_1\tau_2=(i,j)(k,l)=(k,l)(i,j)$$

* Si $\tau_1=\tau_2=(i,j)$, alors

$$\tau_1\tau_2=(i,j)(i,j)=\ident$$

L'identité est une composée de "zéro" transposition.

* Si $\tau_1=(i,j)$ et $\tau_2=(i,k)$, alors

$$\tau_1\tau_2=(i,j)(i,k)=(j,i,k)=(k,j,i)=(k,j)(j,i)$$

* Si $\tau_1=(i,j)$ et $\tau_2=(j,k)$, alors

$$\tau_1\tau_2=(i,j)(j,k)=(i,j,k)=(j,k,i)=(j,k)(k,i)$$

---

On traite alors le cas général par récurrence. On note $\cP_p$ l'assertion à démontrer. Les assertions $\cP_0$ et $\cP_1$ sont évidemment vraies. Supposons que $\cP_{p-1}$ et $\cP_{p-2}$ soient vraies. On se donne alors $\tau_1,\tau_2,\dots,\tau_p$ des transpositions dans $S_n$. On observe alors les transpositions $\tau_1$ et $\tau_2$. Si $\tau_1=\tau_2$, alors $\tau_1\tau_2\dots\tau_p=\tau_3\tau_4\tau_p$ et on peut alors utiliser $\cP_{p-2}$. Sinon, il existe une transposition $\tau_1'$ dont le support ne contient pas $i$ et une transposition $\tau_2'$ telles que $\tau_1\tau_2\dots\tau_p=\tau_1'\tau_2'\dots\tau_p$. Il suffit alors d'appliquer $\cP_{p-1}$ à $\tau_2'\tau_3\dots\tau_p$. Il est important de remarquer que dans chaque cas, la condition portant sur la parité est bien remplie. &#9632;

**Exemple.** Un véritable exemple sera probablement plus parlant.
