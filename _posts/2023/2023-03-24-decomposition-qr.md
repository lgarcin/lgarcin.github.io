---
layout: post
title: Décomposition QR
css:
- "/css/theorems.css"
date: 2023-03-24 18:20 +0100
---
Tous le code Python proposé est accessible dans un [notebook Jupyter interactif](https://www.kaggle.com/lgarcin/d-composition-qr).

## Notations

On adopte les notations suivantes :

- $\cT_n^{++}(\dR)$ désigne l'ensemble des matrices triangulaires supérieures de $\cM_n(\dR)$ à coefficients diagonaux strictement positifs.
- $\langle\cdot,\cdot\rangle$ désigne le produit scalaire usuel sur $\cM_{n,1}(\dR)$ i.e. $\forall(X,Y)\in\cM_{n,1}(\dR)^2$, $\langle X,Y\rangle=X^\top Y$.

## Théorème

Soit $A\in GL_n(\dR)$. Alors il existe $Q\in O_n(\dR)$ et $R\in\cT_n^{++}(\dR)$ telles que $A=QR$.

## Intérêt

Dès lors que l'on a une décomposition QR d'une matrice $A$, il devient trivial de résoudre un sytème $AX=Y$. En effet ce système équivaut à $RX=Q^{-1}Y=Q^\top Y$. Le calcul de $Q^\top$ est immédiat et ce dernier système est triangulaire : il se résout donc très simplement.

## Rappels sur le procédé d'orthonormalisation de Gram-Schmidt

Si $(f_1,\dots,f_n)$ est une base d'un espace euclidien $E$ de dimension $n$, on peut la transformer en une base **orthonormée** $(e_1,\dots,e_n)$ en appliquant le procédé suivant :

- on norme le premier vecteur $f_1$ en un vecteur $e_1$ ;
- une fois construits les vecteurs $e_1,\dots,e_k$, on norme le projeté orthogonal de $f_{k+1}$ sur $\vect(e_1,\dots,e_k)^\perp$ pour obtenir le vecteur $e_{k+1}$.

Du point de vue du calcul, cela revient à construire par récurrence les vecteurs $f_1,\dots,f_n$ via la relation de récurrence

$$
\forall k\in\lb0,n-1\rb,\;
e_{k+1}=\frac{\tilde e_{k+1}}{\|\tilde e_{k+1}\|}
\text{ où }\tilde e_{k+1}=f_{k+1}-\sum_{j=1}^k\langle f_{k+1},e_j\rangle e_j
$$

_Remarque_. On convient que la somme est nulle lorsque $k=0$.

En plus du fait que $(e_1,\dots,e_n)$ est une base orthonormée de $E$, on vérifie aisément que

$$
\forall k\in\lb1,n\rb,\;\left(\vect(e_1,\dots,e_k)=\vect(f_1,\dots,f_k)\right)\wedge\left(\langle e_k,f_k\rangle>0\right)
$$

## La décomposition QR via le procédé de Gram-Schmidt

Notons $f_1,\dots,f_n$ les colonnes de la matrice $A\in GL_n(\dR)$. Comme la matrice $A$ est inversible, la famille $(f_1,\dots,f_n)$ est une base de $\cM_{n,1}(\dR)$. On lui applique le procédé d'orthonormalisation de Gram-Schmidt pour obtenir une base orthonormée (pour le produit scalaire canonique) $(e_1,\dots,e_n)$ de $\cM_{n,1}(\dR)$.

Notons $Q$ la matrice dont les colonnes sont $e_1,\dots,e_n$. Comme $(e_1,\dots,e_n)$ est une base orthonormée, $Q$ est une matrice orthogonale. En notant $R$ la matrice de la base $(f_1,\dots,f_n)$ dans la base $(e_1,\dots,e_n)$, on a alors bien $A=QR$.

De plus, on rappelle que

$$
\forall k\in\lb1,n\rb,\;\left(\vect(e_1,\dots,e_k)=\vect(f_1,\dots,f_k)\right)\wedge\left(\langle e_k,f_k\rangle>0\right)
$$

donc la matrice $R$ est triangulaire supérieure et ses coefficients diagonaux sont strictement positifs. En effet, comme $(e_1,\dots,e_n)$ est une base orthonormée, $R_{i,j}=\langle f_j,e_i\rangle$ pour tout $(i,j)\in\lb1,n\rb^2$ et notamment $R_{k,k}=\langle f_k,e_k\rangle>0$ pour tout $k\in\lb1,n\rb$.

## Algorithme en Python

```python
import numpy as np

def QR_gram_schmidt(A):
    Q = np.zeros_like(A)
    R = np.zeros_like(A)
    for i in range(A.shape[1]):
        dp = Q[:, :i].T@A[:, i]
        R[:i, i] = dp
        Q[:, i] = A[:, i]-Q[:, :i]@dp
        Q[:, i] = Q[:, i]/np.linalg.norm(Q[:, i])
        R[i, i] = Q[:, i].T@A[:, i]
    return Q, R
```

## Méthode de Householder

Dans ce qui suit, $E$ désigne un espace euclidien de dimension $n$ et $\cB$ une base **orthonormée** de $E$.

### Matrices de Householder

Soient $n$ un vecteur non nul de $E$ et $s$ la réflexion par rapport à l'hyperplan $\vect(n)^\perp$. Le projeté orthogonal d'un vecteur $x\in E$ sur $\vect(n)$ est $\frac{\langle n,x\rangle}{\|n\|^2}n$. On en déduit que

$$
s(x)=x-2\frac{\langle n,x\rangle}{\|n\|^2}n
$$

Si on note $N$ sa matrice de $n$ dans la base $\cB$, alors la matrice de $s$ dans la base $\cB$ est donc

$$
I_n-2\frac{NN^\top}{N^\top N}
$$

Une telle matrice est appelée une **matrice de Householder**.

### Réflexion échangeant deux vecteurs de même norme

Soient $E$ un espace euclidien de dimension $n$ ainsi que $u$ et $v$ deux vecteurs distincts et de même norme. Il existe alors une (unique) réflexion $s$ échangeant $u$ et $v$. Il s'agit de la réflexion par rapport à l'hyperplan $\vect(v-u)^\perp$.

Notamment si $S$, $U$ et $V$ sont respectivement les matrices de $s$, $u$ et $v$ dans cette base $\cB$, alors

$$
S=I_n-2\frac{(U-V)(U-V)^\top}{(U-V)^\top(U-V)}
$$

### Application à la décomposition QR

On procède à un raisonnement par récurrence. Il est clair que toute matrice de $GL_1(\dR)$ admet une décomposition $QR$. Supposons que ce soit vrai pour toute matrice de $GL_{n-1}(\dR)$, où $n$ est un entier supérieur ou égal à $2$.

Soit $A\in GL_n(\dR)$. Notons $U$ sa première colonne (nécessairement non nulle). Comme les vecteurs $U$ et $V=(\|U\|,0,\dots,0)^\top$ ont même norme, il existe une matrice de réflexion $S$ telle que $SU=V$. La première colonne de $SA$ est alors $V$. Notons $\tilde A$ la matrice $SA$ dont on a supprimé les premières lignes et premières colonnes. Autrement dit

$$
SA=\begin{pmatrix}
\|U\|&\begin{matrix}\star&\dots&\star\end{matrix}\\
\begin{matrix}0\\\vdots\\0\end{matrix}&\tilde A
\end{pmatrix}
$$

Comme $S$ et $A$ sont inversibles, $\det(SA)=\|U\|\det(\tilde A)\neq0$ donc $\tilde A\in GL_{n-1}(\dR)$. Il existe donc une matrice $\tilde Q\in O_{n-1}(\dR)$ et $\tilde R\in\cT_{n-1}^{++}(\dR)$ telle que $\tilde A=\tilde Q\tilde R$. Puisque $S=S^{-1}$ ($S$ est une matrice de réflexion), on a alors $A=QR$ avec

$$
Q=S\begin{pmatrix}
1&\begin{matrix}0&\dots&0\end{matrix}\\
\begin{matrix}0\\\vdots\\0\end{matrix}&\tilde Q
\end{pmatrix}\in O_n(\dR)
\qquad\text{et}\qquad
R=\begin{pmatrix}
\|U\|&\begin{matrix}\star&\dots&\star\end{matrix}\\
\begin{matrix}0\\\vdots\\0\end{matrix}&\tilde R
\end{pmatrix}\in\cT_n^{++}(\dR)
$$

On en déduit également un algorithme :

---

**Entrée** Une matrice $A\in GL_n(\dR)$

- Initialisation
  - $R\gets A$
  - $Q\gets I_n$

- Pour $k$ variant de $1$ à $n$ :
  - On extrait la première colonne $U\in\cM_{n-k+1,1}(\dR)$ de la matrice extraite $(R_{i,j})_{k\leq i,j\leq n}$
  - Si $U_1\neq\|U\|$
    - $V\gets(\|U\|,0,\dots,0)$.
    - $S\gets I_{n-k+1}-2\frac{(U-V)(U-V)^\top}{(U-V)^\top(U-V)}$
    - $Q_1\gets\begin{pmatrix}I_{k-1}&0\newline0&S\end{pmatrix}$
    - $Q\gets QQ_1$
    - $R\gets Q_1R$

**Renvoyer** $Q$ et $R$

---

On définit d'abord une fonction calculant la matrice de Householder associée à un vecteur $U$.

```python
import numpy as np

def matrice_householder(U):
    return np.eye(U.shape[0]) - 2 * (U@U.T) / (U.T@U)
```

On implémente alors un algorithme itératif calculant la décomposition QR d'une matrice inversible $A$.

```python
def QR_householder(A):
    n = A.shape[0]
    R = A.copy()
    Q = np.eye(n)
    for k in range(n):
        U = R[k:, k].copy()
        norme_U = np.linalg.norm(U)
        if U[0] != norme_U:
            U[0] -= norme_U
            S = matrice_householder(U)
            Q[:, k:] = Q[:, k:]@S
            R[k:, :] = S@R[k:, :]
    return Q, R
```

On peut également proposer une fonction récursive.

```python
def QR_householder_recu(A):
    if A.shape[0] == 1:
        return (np.matrix([[1]]), A) if A[0, 0] > 0 else (np.matrix([[-1]]), -A)
    U = A[:, 0].copy()
    norme_U = np.linalg.norm(U)
    if U[0] != norme_U:
        U[0] -= norme_U
        Q = matrice_householder(U)
        R = Q@A
    else:
        Q = np.eye(A.shape[0])
        R = A
    Q1, R1 = QR_householder_recu(R[1:, 1:])
    Q[:, 1:] = Q[:, 1:]@Q1
    R[1:, 1:] = R1
    return Q, R
```
