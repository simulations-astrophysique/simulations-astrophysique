---
contents:
  - "Réviser les concepts de programmation en python"
reading_time: "120 minutes"
ai_image: "../../assets/images/ia/IA_NIA.png"
report_url: "https://forms.office.com/r/ccF1FGKW25"
summary: "Exercices de révision sur le langage de programmation Python, en particulier l'utilisation des conteneurs de données et de la bibliothèque *Numpy*."
---

Cette page contient des Certains problèmes font appel à des notions de physique ou mathématiques que vous pourriez ne pas avoir vues, selon votre parcours scolaire. N'hésitez pas à demander de l'aide pour ces notions.

Pour référence : [Notes de cours de programmation en science](https://programmation-en-sciences.github.io/).

1. On souhaite tester empiriquement le [paradoxe des anniversaires](https://fr.wikipedia.org/wiki/Paradoxe_des_anniversaires). Faites une simulation où l'on sélectionne une date d'anniversaire (un nombre entre 0 et 364 inclus) aléatoire dans un groupe de 23 personnes. Répétez la simulation 50 fois et calculez quelle proportion des groupes possède au moins 2 individus qui ont la même date d'anniversaire.
2. Importez les fonctions de l'exercice 1 dans un nouveau fichier [et revoir cette section](https://programmation-en-sciences.github.io/bases-de-programmation/fonctions/#structurer-un-programme). À partir de cela, calculez, avec 100 répétitions de l'exécution :

    1. La plus petite proportion observée et le numéro de la simulation associée
    2. La plus grande proportion observée et le numéro de la simulation associée
    3. La moyenne et l'écart-type
    4. L'intervalle de confiance à 5% ($z_{0.975}=1.96$)
    5. Tous les résultats en ordre croissant

    !!! info "Intervalle de confiance"

        L'intervalle de confiance pour une moyenne est donné par 

        $$
        \left[\bar{x} - z_{0.975}\frac{\sigma}{\sqrt{n}}; \bar{x} + z_{0.975}\frac{\sigma}{\sqrt{n}} \right]
        $$


3. On souhaite mesurer des positions d'un objet en chute libre (initialement au repos) pendant un certain intervalle de temps. Les mesures se prennent à intervalle régulier de 0.1 seconde. On lance l'objet d'une masse de 3kg d'une hauteur de 50m. Vous devez mesurer jusqu'à ce que l'objet atteigne le sol (hauteur de 0). Vous devez ensuite lire à la console un choix de temps à afficher et afficher la position de l'objet à ce moment.
4. Tracez le graphique de la hauteur de l'objet en fonction du temps écoulé. Faites-le pour un intervalle de temps entre 0 et 4 secondes par intervalle de 0.1 seconde. Faites générer un graphique de type nuage de points et un graphique avec la courbe. En extra, gérez le fait que le sol est à 0m et que l'objet ne peut descendre sous cette limite.
4. Évaluez les expressions suivantes :

    1. $log(5)$
    2. $log_4(91)$
    2. $ln(7)$
    3. $e^8$
    4. $|-6|$
    5. $\sqrt[3]475$    
    6. $sin(\frac{\pi}{4})$
    7. $sec(\frac{\pi}{2})$
    8. $arctan(0.1)$
