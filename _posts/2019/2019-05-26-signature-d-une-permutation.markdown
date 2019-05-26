---
layout: post
title: Signature d'une permutation
published: true
---

Voici la définition officielle de la signature au programme de MPSI.

**Définition.** Il existe une unique application $\eps$ du groupe symétrique $S_n$ dans $\\{-1,1\\}$ telle que $\eps(\tau)=-1$ pour toute transposition $\tau$ et $\eps(\si\si')=\eps(\si)\eps(\si')$ pour toutes permutations $\si$ et $\si'$.

*Remarque.* En MP, on dira plutôt que la signature est l'unique morphisme non trivial de $S_n$ dans $\\{-1,1\\}$.

L'unicité de la signature est à peu près claire puisque les transpositions engendrent $S_n$. Ainsi, un morphisme de groupe qui est déterminé sur les transpositions est déterminé sur $S_n$ en entier.

En ce qui concerne l'existence, la signature est la plupart du temps définie à l'aide du nombre d'*inversions*[^1] et on montre après coup qu'ainsi définie, elle vérifie bien les conditions données dans la définition officielle au programme.

Mais cette façon de procéder ne semble pas très naturelle et j'ai donc cherche un moyen de prouver l'existence sans faire appel à la notion d'inversion et en utilisant simplement des transpositions. Il s'agit de montrer que si une permutation se décompose de deux manières comme un produit de transpositions, les nombres de transpositions intervenant dans ces deux décompositions ont la même parité. En effet, on peut alors poser $\eps(\si)=(-1)^{T(\si)}$ où $T(\si)$ est le nombre de transpositions intervenant dans une telle décomposition d'une permutation $\si$, puisque la parité de ce nombre $T(\si)$ est une quantité intrinsèque à la permutation $\si$.

Je ne prétends pas que cette démonstration ait quoi que ce soit d'original ; je suis sûr que beaucoup y ont pensé avant moi. Mais, comme je ne l'ai pas trouvée dans la littérature, je me permets d'en faire profiter les personnes intéressées.

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

On traite alors le cas général par récurrence. On note $\cP_p$ l'assertion à démontrer. Les assertions $\cP_0$ et $\cP_1$ sont évidemment vraies. Supposons que $\cP_{p-1}$ et $\cP_{p-2}$ soient vraies. On se donne alors $\tau_1,\tau_2,\dots,\tau_p$ des transpositions dans $S_n$. On observe alors les transpositions $\tau_1$ et $\tau_2$. Si $\tau_1=\tau_2$, alors $\tau_1\tau_2\dots\tau_p=\tau_3\tau_4\dots\tau_p$ et on peut alors utiliser $\cP_{p-2}$. Sinon, il existe une transposition $\tau_1'$ dont le support ne contient pas $i$ et une transposition $\tau_2'$ telles que $\tau_1\tau_2\dots\tau_p=\tau_1'\tau_2'\dots\tau_p$. Il suffit alors d'appliquer $\cP_{p-1}$ à $\tau_2'\tau_3\dots\tau_p$. Il est important de remarquer que dans chaque cas, la condition portant sur la parité est bien remplie. &#9632;

**Exemple.** Un véritable exemple sera probablement plus parlant. On essaie d'obtenir un produit de transpositions dans lequel seul le support de la transposition la plus "à droite" contient 5.

$$
\begin{align}
\overline{(1, 5) (2, 5)} (5, 1) (5, 3) (4, 1) (3, 5) (1, 2)
&=(2, 1) \overline{(1, 5) (5, 1)} (5, 3) (4, 1) (3, 5) (1, 2) \\
&=(2, 1) \overline{(5, 3) (4, 1)} (3, 1) (1, 2) \\
&=(2, 1) (4, 1) \overline{(5, 3) (3, 1)} (1, 2) \\
&=(2, 1) (4, 1) (3, 1) \overline{(1, 5) (1, 2)} \\
&=(2, 1) (4, 1) (3, 1) (1, 2) (2, 5) \\
\end{align}
$$

On peut maintenant énoncer le lemme suivant.

**Lemme.** L'identité ne peut s'écrire que comme le produit d'un nombre **pair** de transpositions.

**Démo.** Supposons que l'identité de $\lb1,n\rb$ s'écrive comme un produit de $p$ transpositions. D'après le lemme précédent, l'identité peut alors s'écrire comme un produit de $q$ transpositions où $q$ a la même parité que $p$ et où seul le support de la dernière transposition contient éventuellement $n$. Le support de cette dernière transposition ne peut en fait pas contenir $n$ car on voit rapidement que $n$ ne serait pas fixe dans le cas contraire. En réitérant le processus, on peut écrire l'identité comme un produit de transpositions dont les supports ne contiennent aucun des éléments de $\lb1,n\rb$, autrement dit un produit de "zéro" transposition. La parité du nombre de transpositions ayant été conservé au cours du processus, le nombre intial $p$ de transpositions a la parité de $0$ : $p$ est donc pair. &#9632;

On peut maintenant démontrer le résultat final.

**Proposition.** Si deux produits de transpositions sont égaux, les nombres de facteurs dans chacun des deux produits ont la même parité.

**Démo.** Supposons que des transpositions $\tau_1,\dots\tau_p,\tau'_1,\dots\tau'_q$ vérifient $\tau_1\dots\tau_p=\tau'_1\dots\tau'_q$. On en déduit que $\tau_1\dots\tau_p\tau'_q\dots\tau'_1=\ident$. Le lemme précédent montre que $p+q$ est pair, autrement dit que $p$ et $q$ ont même parité.

---

### Notes

[^1]: On dit qu'une paire $\{i,j\}$ est en inversion pour une permutation $\si$ si $i-j$ et $\si(i)-\si(j)$ sont de signes opposés. Si on note $I(\si)$ le nombre de paires en inversion pour $\si$, la signature de $\si$ peut-être définie comme $(-1)^{I(\si)}$.
