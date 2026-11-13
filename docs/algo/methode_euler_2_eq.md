---
contents:
  - "Algorithmes de calcul numérique"
reading_time: "30 minutes"
ai_image: "../../assets/images/ia/IA_NIA.png"
report_url: "https://forms.office.com/r/ccF1FGKW25"
summary: "Présente le fonctionnement de la méthode d'Euler pour résoudre un système de deux équations différentielles."
---

Comme mentionné précédemment, on peut utiliser la méthode d'Euler pour résoudre des équations d'ordre 1, qui font intervenir seulement une équation et sa dérivée. Que se passe-t\-il lorsqu'on travaille en physique et que l'on doit considérer une accélération qui n'est pas constante : donc un système où la dérivée seconde intervient ? La méthode d'Euler permet de traiter cette situation en décomposant le système en deux équations : 

1. Résoudre la relation entre l'accélération et la vitesse
2. Résoudre la relation entre la vitesse et la position

Par exemple, un objet connait une accélération donnée par l'équation $a(t) = 2p(t)$ où $a(t)$ est la fonction de l'accélération selon le temps et $p(t)$ la position selon le temps. La variable $t$ représente le temps écoulé. On sait que la vitesse initiale est $v(0) = 1m/s$ et que la position initiale est $p(0) = 0m$.

En utilisant les équations de la physique et en introduisant $v(t)$ la fonction de la vitesse selon le temps, on obtient le système.

$$
\begin{align*}
a(t) = \frac{dv(t)}{dt} = \frac{d^2p(t)}{dt^2} = 2p(t)
\end{align*}
$$

À partir de la première égalité, on va poser le système suivant :

$$
\begin{align*}
v_{n+1} &= v_n + h \times a(t_n) \\\\
 &= v_n + h \times 2*p(t_n)
\end{align*}
$$ 

Ensuite, comme l'on connait la vitesse, on peut calculer la position

$$
\begin{align*}
p_{n+1} &= p_n + h \times v(t_n) \\\\
 &= p_n + h \times v_n
\end{align*}
$$

Donc pour $h = 0.5$, si l'on cherche la position après 2 secondes, on a le système suivant.

**Étape 1**

$$
\begin{align*}
v_1 &= v_0 + h \times 2p_0 \\\\
    &= 1 + 0.5 \times 2 \times 0 \\\\
    & = 1 \\\\
p_1 &= p_0 + h \times v_0 \\\\
    &= 0 + 0.5 \times 1 \\\\
    & = 0.5
\end{align*}
$$

Après 0.5 seconde, l'objet a une vitesse de 1m/s et une position de 0.5m par rapport au référentiel de départ.

**Étape 2**

$$
\begin{align*}
v_2 &= v_1 + h \times 2p_1 \\\\
    &= 1 + 0.5 \times 2 \times 0.5 \\\\
    & = 1.5 \\\\
p_2 &= p_1 + h \times v_1 \\\\
    &= 0.5 + 0.5 \times 1 \\\\
    & = 1
\end{align*}
$$

Après 1 seconde, l'objet a une vitesse de 1.5m/s et une position de 1m par rapport au référentiel de départ.

**Étape 3**

$$
\begin{align*}
v_3 &= v_2 + h \times 2p_2 \\\\
    &= 1.5 + 0.5 \times 2 \times 1 \\\\
    & = 2.5 \\\\
p_3 &= p_2 + h \times v_2 \\\\
    &= 1 + 0.5 \times 1.5 \\\\
    & = 1.75
\end{align*}
$$

Après 1.5 secondes, l'objet a une vitesse de 2.5m/s et une position de 1.75m par rapport au référentiel de départ.

**Étape 4**

$$
\begin{align*}
v_4 &= v_3 + h \times 2p_3 \\\\
    &= 2.5 + 0.5 \times 2 \times 1.75 \\\\
    & = 4.25 \\\\
p_4 &= p_3 + h \times v_3 \\\\
    &= 1.75 + 0.5 \times 2.5 \\\\
    & = 3
\end{align*}
$$

Après 2 secondes, l'objet a une vitesse de 4.25m/s et une position de 3m par rapport au référentiel de départ.


!!! info "Le pas en physique"

    En physique, le pas correspond généralement à l'intervalle de temps considéré. On retrouve dans plusieurs source la notation avec $\Delta t = h$.


## Implémentation 

L'implémentation en python se fait de façon analogue à celle pour une équation, car **tous les membres de droites utilisent l'information de l'itération précédente.** 

```py title="Méthode d'Euler à deux équations" linenums="1"
def euler_2eq(a, b, h):
    p_i = 0
    v_i = 1
    t_i = a
    
    while t_i <= b:
        p_i_plus_1 = p_i + h * v_i
        v_i_plus_1 = v_i + h * 2 * p_i
        
        p_i = p_i_plus_1
        v_i = v_i_plus_1
        t_i += h
        
    return {"p": p_i, "v": v_i}

print(euler_2eq(0, 2, 0.5))
```

## Exercice 

4. Soit un objet soumis à une accélération $a(t) = \frac{1}{p(t)}$. La position initiale est de 5m et la vitesse initiale est de -1m/s. Quelle sera sa position et sa vitesse après deux secondes ? Utilisez un pas de 0.005.

??? success "Solution"

    Position : 3.4537 m
    Vitesse : -0.5109 m/s