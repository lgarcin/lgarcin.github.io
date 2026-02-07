---
title: Interversion limite/intégrale
---

Intervertir sans précaution limite et intégrale, c'est MAL.

Posons $f_n(x)=(n+1)x^n$ pour $x\in[0,1]$ et $n\in\mathbb N$. Alors pour tout $n\in\mathbb N$, $\int_0^1f_n(x)\,dx=1$. Pourtant pour tout $x\in[0,1[$, $\lim_{n\to+\infty}f_n(x)=0$ par croissancces comparées. Ainsi
$$
1=\lim_{n\to+\infty}\int_0^1f_n(x)\,dx\neq\int_0^1\lim_{n\to+\infty}f_n(x)\,dx=0
$$
