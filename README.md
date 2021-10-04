# Mes projets

Cette partie présente mes projets Python développés ces 4 dernières semaines

## Calculator 

Calculator est une calculatrice en ligne de commande qui demande à l'utilisateur de saisir deux nombres. Ensuite, Calculator affichera le résultat de l'addition des nombres saisis par l'utilisateur.

Quand l'utilisateur ne rentre pas de données, Calculator les lui réclamerons jusqu'à ce qu'il les renseigne.

## Carré Magic

Dans ce projet, j’ai créé 4 fonctions qui return un carré vide, un carré plein, un carré avec ses deux diagonales principales et un concentric.

La fonction final_pattern fait appelle aux fonctions créées en amont en fonction des arguments renseignés ([type de forme] hauteur, largeur).

```python
final_pattern(["full", "concentric"], 23, 23)
# return un carré full et un concentric de taille 23 hateur et 23 largeur
# PS: le concentric ne fnctionne que si la taille du carré - 3 est un mutltiple de 4.
```
## find_mail_operator
Programme qui demande à l'utilisateur de saisir un email et renvoie l'opérateur de l'email saisi.

## ip_validator

Fonction qui return True si une adresse est valide et False si elle ne l'est pas. 
Pour qu'une ip soit valide, il faut qu'elle soit composée de 4 nombres compris entre 0 et 255 et séparés par des points.
```python
ip_validator("192.2.3.155")  => True
ip_validator("192.2.3.285")  => False
ip_validator("192.2.155")    => False
```
## le_nombre_mystere

Mini jeu qui consiste à deviner un nombre aléatoire compris entre 0 et 100. Vous avez 10 essais pour trouver le bon nombre. Vous avez des indications (plus grand ou plus petit que le nombre renseigné) à chaque essai.

## minesweeper (projet encours)

C'est le jeu du démineur. Encours de dév...



