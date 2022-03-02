---
layout: post
title: Simulation de variables aléatoires
---

```python
from random import random
from math import floor, log
```

Python dipose d'un module `random` dans la bibliothèque standard. La fonction du même nom de ce module renvoie un nombre aléatoire suivant une loi uniforme sur $[0,1[$. La variable aléatoire $X$ associée n'est pas une variable aléatoire discrète puisque son support $[0,1[$ n'est pas dénombrable. On sort donc du cadre du programme de classes préparatoires en probabilités. Néanmoins, il suffit de comprendre pour la suite que cette variable aléatoire vérifie la propriété suivante

$$
\forall(a,b)\in[0,1]^2,\;a\leq b\implies \dP(X\in[a,b[)=b-a
$$

### Loi de Bernoulli

Il est alors très simple de simuler une variable aléatoire suivant une loi de Bernoulli de paramètre $p\in[0,1]$. En effet, en posant $Y=\un_{\lbrace X<p\rbrace}$, on a

$$
\begin{aligned}
\dP(Y=1)&=\dP(X<p)=\dP(X\in[0,p[)=p-0=p\\
\dP(Y=0)&=\dP(X\geq p)=\dP(X\in[p,1[)=1-p
\end{aligned}
$$

On peut alors définir une fonction ```bernoulli``` simulant une variable aléatoire de Bernoulli de paramètre $p$.

```python
def bernoulli(p):
  return 1 if random()<p else 0
```

### Loi binomiale

Comme on sait que la somme de $n$ variables aléatoires indépendantes suivant la même loi de Bernoulli de paramètre $p$ suit la loi binomiale de paramètres $n$ et $p$, il n'est alors pas difficile d'écrire une fonction simulant une variable aléatoire suivant cette loi.

```python
def binomial(n,p):
  return sum(bernoulli(p) for _ in range(n))
```

### Loi uniforme

Si l'on souhaite simuler une loi uniforme sur $\lbrace0,1,\dots,n-1\rbrace$, on pose $Y=\lfloor nX\rfloor$. Ainsi

$$
\begin{aligned}
\forall k\in\lbrace0,1,\dots,n-1\rbrace,\;\dP(Y=k)&=\dP(\lfloor nX\rfloor=k)\\
&=\dP(nX\in[k,k+1[)\\
&=\dP\left(X\in\left[\frac{k}{n},\frac{k+1}{n}\right[\right)\\
&=\frac{k+1}{n}-\frac{k}{n}=\frac{1}{n}
\end{aligned}
$$

```python
def uniform(n):
    return floor(n*random())
```

Si l'on souhaite simuler une variable aléatoire sur un ensemble fini $E=\lbrace e_0,\dots,e_{n-1}\rbrace$, il suffit de modéliser cet ensemble par une liste $\mathtt{[e_0,\dots,e_{n-1}]}$.

```python
def uniform(n):
  if type(n)==int:
    return floor(n*random())
  if type(n)==list:
    return n[uniform(len(n))]
```

### Loi géométrique

```python
def geometric(p):
  n=1
  while(bernoulli(p)==0):
    n+=1
  return n
```

```python
def geometric(p):
  return floor(log(1-random())/log(1-p))+1
```
