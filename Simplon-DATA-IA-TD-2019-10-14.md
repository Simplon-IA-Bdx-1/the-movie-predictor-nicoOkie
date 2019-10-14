# Travaux Dirigés du lundi 14 octobre 2019

## Objectifs

- Manipuler l'outil git en CLI
- Manipuler Docker
- Écrire des requêtes SQL
- Ajouter des functionnalités à une application en Python

## Avant-Propos

### Présentation

Précédemment, dans Simplon DATA/IA Bordeaux Saison 1.
Nous avons vu ensemble MySQL, Docker, git et python. Vous devrez mettre en oeuvre l'ensemble de vos
connaissances dans ces domaines afin d'arriver à vos fins. Vous allez travailler sur des fichiers
indépendants de vos fichiers écrit durant les cours. Si
vous n'arrivez pas à tout faire, pas de panique, c'est normal. N'hésitez pas à utiliser les salons 
Discord pour vous entraider ! Je serai peut etre sur Discord de temps en temps... qui sait ?!

### Rendu OBLIGATOIRE

A la fin de la journée, vous devrez avoir commité et pushé vos modifications sur votre dépôt git, puis
m'envoyer un email (arnaud@admds.net) et mettre Perrine en copie (pferre@simplon.co). Dans cet email,
vous indiquerez l'adresse web de votre dépôt git, ainsi que toute remarque que vous souhaitez me partager.

### Liens utiles

- [Les bases de git](https://git-scm.com/book/fr/v1/Les-bases-de-Git)
- [module argparse de python](https://docs.python.org/3/library/argparse.html)
- [module csv de python](https://docs.python.org/3/library/csv.html)

## Instructions

1. Rendez-vous sur le dép$ot git à l'adresse suivante https://github.com/dehy/themoviepredictor-td
2. Cliquer sur le bouton "Fork" en haut à droit afin d'en créer un copie personnelle sur votre compte
3. Sur votre machine locale et à l'aide de la commande "git clone", cloner ce nouveau dépôt sur votre
   machine locale. (Astuce : un bouton vert "Clone or Download" est disponible sur la page de votre projet 
   cloné. Vous trouverez dans ce projet tout le nécessaire pour réaliser les instructions suivantes.
4. À l'aide de la commande "docker-compose", démarrer les services du projet (base de donnée + adminer)
5. Importer le fichier TheMoviePredictor_create.sql dans la base de donnée avec la méthode de votre choix
   (cli ou adminer)
6. Tester le script app.py en executant des commandes de lecture (find ou list). Une liste de films ou
   de personnes doit vous être retournée.
7. Modifier le script app.py pour y ajouter la fonctionnalité suivante :
  - Pouvoir insérer de nouvelles personnes avec la commande suivante :
    $ python app.py people insert --firstname "John" --lastname "Doe"
8. Commiter vos modifications avec les commandes "git add" ainsi que "git commit"
9. Modifier le script app.py pour y ajouter la fonctionnalité suivante :
  - Pouvoir insérer de nouveaux films avec la commande suivante :
    $ python app.py movies insert --title "Star Wars, épisode VIII : Les Derniers Jedi" --duration 152 --original-title "Star Wars: Episode VIII – The Last Jedi" --origin-country US
10. Commiter vos modifications avec les commandes "git add" ainsi que "git commit"
11. Modifier le script app.py afin de pouvoir importer le fichier csv new_movies.csv avec la commande
   suivante :
   $ python app.py movies import --file new_movies.csv
12. Commiter vos modifications avec les commandes "git add" ainsi que "git commit"
13. Pusher votre branche git vers le dépôt github avec la commande git push
14. Well done! Danse de la victoire : \\o o// \\o o// \o/

BONUS LEVEL

15. En utilisant le module python "BeautifulSoup", scrapez Wikipedia pour récupérer des informations sur des
    films (Aide : https://www.dataquest.io/blog/web-scraping-tutorial-python/)
16. Modifier les options de app.py pour automatiser la tâche
    $ python app movies scrap https://fr.wikipedia.org/wiki/Les_Bronzés