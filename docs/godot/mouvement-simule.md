---
contents:
  - "Utilisation d'un moteur de jeu"
  - "Algorithmes de calcul numérique"
reading_time: "30 minutes"
ai_image: "../../assets/images/ia/IA_NIA.png"
report_url: "https://forms.office.com/r/ccF1FGKW25"
summary: "Applique la méthode d'Euler pour simuler le mouvement."
---

La dernière étape pour obtenir une belle simulation est d'introduire la méthode d'Euler dans notre programme. Pour ce faire, nous aurons besoin des composants suivants :

- Une fonction pour appliquer la méthode d'Euler par écran (*frame*);
- Une fonction pour calculer l'accélération à utiliser pour l'écran

De plus, comme la simulation s'exécute en continu, notre intervalle d'intégration, ce ne sera plus un nombre de périodes déterminées, mais plutôt la fraction d'une période de révolution représentée par un écran. Il faudra donc ajuster nos valeurs de période relative pour satisfaire cette nouvelle contrainte.

## Étape 1 - Ajouter les valeurs pour la simulation

Il faut ajouter les variables suivantes pour simuler correctement le mouvement de Vénus et retirer la variable `rayon`.

```gdscript title="Variables pour gérer la simulation" linenums="1"
@export_group("Simulation gravitationnelle")
@export var masse : float
@export var masse_corps_rotation : float
@export var rayon_initial : float

@export_group("Paramètres de la méthode d'Euler")
@export var etapes_calcul_par_ecran : int

# Groupe de variable masquées pour les calculs
var G : float = 6.673e-11
var r_i : Vector3
var v_i : Vector3
var periode : float
```

On peut également retirer la variable `temps` qui ne sera plus utile.

## Étape 2 - Ajouter une fonction de calcul de l'accélération

Utiliser les équations de la force gravitationnelle et de la seconde loi de Newton pour calculer l'accélération qu'un astre
subit selon sa position réelle. Il est important de corriger la force de l'accélération pour tenir compte du déplacement du centre de masse du système (point de rotation).

```gdscript title="Variables pour gérer la simulation" linenums="1"
func calculer_acceleration_gravitationnelle(position_rellee: Vector3) -> Vector3:
	"""Calcule l'accélération gravitationnelle exercée sur le corps selon sa position
	
	Paramètre:
	position_reelle : sa position dans l'espace en m
	
	Retour:
	L'accélération gravitationnelle exercée sur le corps en m/s^2
	"""
	var facteur = -G * masse * masse_corps_rotation / (position_rellee.length()**3)
	var force = (position_rellee - centre_rotation.position) * facteur
	return force / masse
```

## Étape 3 - Appliquer la méthode d'Euler aux valeurs de position et de vitesse

Les variables `r_i`et `v_i` contiennent l'information sur la position et la vitesse réelle du corps. La méthode de Newton consistera à calculer ces valeurs pour le temps d'un écran.

```
func appliquer_euler(temps_dernier_ecran : float) -> void:
	"""
	Applique la méthode d'Euler pour déterminer la position et la vitesse selon le temps de rendu
	de la simulation.
		
	Paramètre :
	temps_dernier_ecran -- le temps écoulé depuis le dernier écran.
	"""
	#Nombre de période à simuler dans l'écran
	var nb_periode = temps_dernier_ecran  * periode / periode_relative
	#Pas de la simulation
	var h = nb_periode / etapes_calcul_par_ecran
		
	for i in range(etapes_calcul_par_ecran):
		var a_i = calculer_acceleration_gravitationnelle(r_i)
		
		var r_i_plus_1 = r_i + h * v_i
		var v_i_plus_1 = v_i + h * a_i
		
		r_i = r_i_plus_1
		v_i = v_i_plus_1	
```

## Étape 4 - Appeler la méthode d'Euler et utiliser le résultat pour l'affichage des objets de la simulation

On appelle la fonction `appliquer_euler` à chaque écran avec le paramètre de temps écoulé. Cela modifie la fonction `_process`.

```gdscript title="Application de la méthode d'Euler" linenums="1"
func _process(delta: float) -> void:
	# Calcule la position réelle
	appliquer_euler(delta)
	# Converti la position
	position = conv_position_reelle_a_simulee(r_i)

	if centre_rotation != null:
		position += centre_rotation.position
```

## Étape 5 - Initialiser adéquatement les valeurs de la simulation 

Il faut indiquer les valeurs réelles dans les variables créées et modifier la fonction `ready` pour initialiser la position et la vitesse.

```gdscript title="Initialisation de la simulation" linenums="1"
func _ready() -> void:
	r_i = rayon_initial * Vector3(1, 0, 0)
    position = conv_position_reelle_a_simulee(r_i)

	var vitesse_initiale  = sqrt(G * masse_corps_rotation / rayon_initial) # De la loi de Kepler
	v_i = vitesse_initiale * Vector3(0, 0, 1)
	
	periode = 2 * PI * rayon_initial / vitesse_initiale
```

Valeurs initiales de la simulation

|Corps|Masse|Masse corps rotation|Rayon initial|Période relative|
|:--|:--|:--|:--|:--|
|Vénus|$4,868 \times 10^{24}$|$1,988 \times 10^{30}$| $1,0815 \times 10^{11}$ m|6.16|
|Terre|$5,972 \times 10^{24}$ kg|$1,988 \times 10^{30}$| $1,469 \times 10^{11}$ m|10|
|Lune|$7,35 \times 10^{22}$ kg|$5,972 \times 10^{24}$ kg|$3,84 \times 10^{8}$ m|0.75|


On utilise une période relative de 10 pour la Terre pour ralentir la simulation. Dans la prochaine section sur les interfaces utilisateurs, nous verrons comment amener ce paramètre dans la simulation directement.

## Structure du projet

Vous pouvez récupérer le projet dans l'état d'avancement de la fin de cette page de notes ici : [:octicons-mark-github-24: Afficher le projet sur GitHub](https://github.com/simulations-astrophysique/orbite-simulee).