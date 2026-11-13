---
contents:
  - "Algorithmes de calcul numérique"
reading_time: "30 minutes"
ai_image: "../../assets/images/ia/IA_NIA.png"
report_url: "https://forms.office.com/r/ccF1FGKW25"
summary: "Décrit sommairement les techniques de calcul d'erreur et l'erreur théorique des principales méthodes vues dans le cours."
---

Plusieurs façons de considérer les erreurs des méthodes numériques existent. Cette section couvre certains aspects de la couverture des erreurs. L'analyse théorique des erreurs est souvent impossible en pratique, car il faut connaître beaucoup d'information sur les fonctions impliquées afin d'arriver à déterminer la valeur exacte. Toutefois, les formules théoriques donnent une évaluation de la précision des méthodes, et des cas où il est probable qu'une méthode performe moins bien. 

## Notions préalables

### Analyse du pire cas
Dans l'analyse d'erreur, on trouve une valeur majorant l'erreur. Il arrive que l'erreur soit plus petite, mais ce qui est important, c'est qu'elle ne soit jamais supérieure à notre analyse. Cette analyse permet généralement de négliger les petits termes et se concentrer uniquement sur les termes les plus importants.

### La fonction Grand O
Cette fonction exprime un terme qui est au plus aussi grand que son argument. Par exemple $\mathcal{O}(h^2)$ indique un terme qui est au plus de l'ordre de $h^2$, mais pourrait être plus petit. Cette notation permet l'analyse du **pire cas**. 

### Erreur de troncature locale 
Cette erreur indique la perte de précision lors de la troncature effectuée par une erreur de calcul. On note cette erreur par la différence entre l'estimation et la valeur réelle.

$$
y(t_i + h) - y_{i+1}
$$

### Erreur de troncature globale
Cette erreur indique la perte de précision après avoir effectué tous les calculs pour estimer une valeur.

## La méthode d'Euler

Pour la méthode d'Euler, l'erreur de troncature locale est donnée par :

$$
y(t_i + h) - y_{i+1} = \frac{1}{2}h^2+y''(t_i)+\mathcal{O}(h^3)
$$

Ce résultat théorique est valide si la dérivée troisième est bornée sur l'intervalle d'évaluation. On remarque que le terme le plus important de cette équation, pour h petit, est $h^2$. On dit donc que ce terme domine l'erreur et on peut présumer que lorsque $h^2$ devient petit, alors la précision de la méthode devrait augmenter.

Pour l'erreur de troncature globale :

$$
|y(t_n) - y_{n}| \leq \frac{hM}{2L}\left(e^{L(t_n-t_0)} - 1\right)
$$

avec $L$ et $M$ respectivement les bornes de la dérivée première et seconde telles que :

$$
\begin{align*}
L &= \text{max}\left(\left|\frac{d}{dy}[f(t, y)] \right|\right) \\
M &= \text{max}\left(\left|\frac{d^2}{dt^2}[y(t)] \right|\right)
\end{align*}
$$

!!! note "La fonction dérivée n'est pas la même"

    En effet, $L$ prend la fonction du problème et traite $t$ comme une constante, alors que $M$ est la dérivée seconde de la fonction. $L$ est ce que l'on appelle *la constante de Lipschitz*. Cette constante garanti que la pente de la fonction est bornée.

    Ce qui est intéressant avec la constante de Lipschitz, c'est qu'elle permet d'estimer à partir de quel moment un pas serait beaucoup trop grand et va amaner de l'instabilité numérique importante au problème. Cela se produit si $h > \frac{1}{L}$.

Globalement, l'erreur de troncature globale dépend de $h$, d'où la faible précision de la méthode d'Euler, en particulier pour de très grands $h$.

## La méthode de Runge-Kutta d'ordre 4

Pour la méthode RK4, l'erreur de troncature locale est donnée par :

$$
y(t_i + h) - y_{i+1} = Ch^5
$$

Où $C$ est une constante qui dépend de la fonction. Calculer cette constante explicitement est complexe, car elle varie selon la dérivée 4e de $y$. La formule de l'erreur est dominée par $h^5$. Donc même en calculant la constante, le terme le plus important demeure $h^5$. 

L'erreur de troncature globale varie en fonction de $h^4$, ce qui une excellente méthode numérique, peu de méthodes atteignent une erreur globale aussi faible.

[:closed_book: La méthode RK4 et son erreur](https://math.okstate.edu/people/binegar/4513-F98/4513-l21.pdf)

## Sources

BINEGAR, B. (n.d.). Runge-Kutta methods. https://math.okstate.edu/people/binegar/4513-F98/4513-l21.pdf

Wikipedia contributors. (2026, March 6). Euler method. Wikipedia. https://en.wikipedia.org/wiki/Euler_method#Global_truncation_error

Wikipedia contributors. (2026a, February 20). Runge–Kutta methods. Wikipedia. https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods