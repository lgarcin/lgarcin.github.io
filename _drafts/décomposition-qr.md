---
layout: post
title: Décomposition QR
css:
  - "/css/theorems.css"
---

## Notations

On adopte les notations suivantes :

- $\cT_n^+(\dR)$ (resp. $\cT_n^{++}(\dR)$) désigne l'ensemble des matrices triangulaires supérieures de $\cM_n(\dR)$ à coefficients diagonaux positifs (resp. strictement positifs).
- $\langle\cdot,\cdot\rangle$ désigne le produit scalaire usuel sur $\cM_{n,1}(\dR)$ i.e. $\forall(X,Y)\in\cM_{n,1}(\dR)^2$, $\langle X,Y\rangle=X^\top Y$.

## Théorème

Soit $A\in GL_n(\dR)$. Alors il existe $Q\in O_n(\dR)$ et $R\in\cT_n^{++}(\dR)$ telles que $A=QR$.

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

*Remarque*. On convient que la somme est nulle lorsque $k=0$.

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

def QR_decomposition(A):
    Q = np.zeros_like(A)
    R = np.zeros_like(A)
    for i in range(A.shape[1]):
        dp = [np.dot(A[:, i], Q[:, j]) for j in range(i)]
        R[:i, i] = dp
        Q[:, i] = A[:, i]-sum(dp[j]*Q[:, j] for j in range(i))
        Q[:, i] = Q[:, i]/np.linalg.norm(Q[:, i])
        R[i, i] = np.dot(A[:, i], Q[:, i])
    return Q, R
```

[toto](https://replit.com/join/pkatmrjsws-laurentgarcin)

## Matrices de Householder
