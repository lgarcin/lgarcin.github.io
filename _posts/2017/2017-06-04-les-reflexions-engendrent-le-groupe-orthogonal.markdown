---
title: Les réflexions engendrent le groupe orthogonal
---

De la même façon que les transpositions engendrent le groupe symétrique, les réflexions d'un espace euclidien engendrent le groupe orthogonal. La preuve est d'ailleurs sensiblement la même.


#### Les transpositions engendrent le groupe symétrique

On rappelle rapidement la preuve du fait que les transpositions de $S_n$ engendrent le groupe symétrique $S_n$. On raisonne par récurrence. La propriété est évidemment vraie lorsque $n=1$. On la suppose vraie pour un certain $n\in\dN^*$. On considère alors une permutation $\sigma$ de $S_{n+1}$. Si $\sigma(n+1)=n+1$, alors $\sigma$ induit une permutation de $S_n$ qui est alors un produit de transpositions ; il en est alors de même de $\sigma$. Si $\sigma(n+1)\neq n+1$, on considère la transposition $\sigma'=\tau\circ\sigma$. On a alors à nouveau $\sigma'(n+1)=n+1$ et on se ramène au cas précédent. Ainsi $\sigma'$ est un produit de transpositions et donc $\sigma$ également puisque $\tau^{-1}=\tau$ est une transposition.

#### Les réflexions engendrent le groupe orthogonal

Le groupe $O(E)$ est clairement engendré par les rélexions lorsque $\dim E=1$, puisqu'alors $O(E)=\lbrace\ident_E,-\ident_E\rbrace$ et $-\ident_E$ est une réflexion (la seule d'ailleurs).
On suppose que le groupe orthogonal de tout espace euclidien de dimension $n\in\dN^*$ est engendré par les réflexions. On se donne alors un espace euclidien $E$ de dimension $n+1$ et $u\in O(E)$. Si $u=\ident_E$, $u$ est bien un produit de réflexions. Sinon, il existe $a\in E$ (forcément  non nul) tel que $u(a)\neq a$. Puisque $\lVert u(a)\rVert=\lVert a\rVert$, on peut montrer qu'il existe une réflexion $s$ échangeant $a$ et $u(a)$ (c'est géométriquement clair et on peut préciser que $s$ est la réflexion par rapport à l'hyperplan $\vect(u(a)-a))^\perp$). Alors $s\circ u$ coïncide avec l'identité sur $\vect(a)$. En particulier, $s\circ u$ stabilise $\vect(a)$. Puisque $s\circ u$ est un automorphisme orthogonal, il stabilise également $\vect(a)^\perp$. Ainsi $s\circ u$ induit un automorphisme orthogonal de $\vect(a)^\perp$. Par hypothèse de récurrence, cet automorphisme induit est un produit de réflexions de $\vect(a)^\perp$. On peut prolonger ces réflexions de $\vect(a)^\perp$ en des réflexions de $E$ en les faisant coïncider avec l'identité sur $\vect(a)$. On vérifie alors que $s\circ u$ est le produit de ces réflexions et $u$ est alors également une réflexion puisque $s^{-1}=s$ en est une.
