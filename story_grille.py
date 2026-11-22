from grille import Grille

'''
Nom : "Plouf dans l'eau"
Utilisateur : un joueur
Story : On veut pouvoir gérer les tirs de l'adversaire
Actions :

    1) créer une grille à 5 lignes et 8 colonnes
    2) afficher la grille à l'écran
    3) demande à l'utilisateur de rentrer deux coordonnées x et y
    4) tirer à l'endroit indiqué sur la grille
    5) afficher de nouveau la grille

'''

grille_de_jeu = Grille(5, 8)
grille_de_jeu.afficher()

correct_x = False
x = 0

while not correct_x:
    correct_x = True
    str_x = input("Donnez l'abscisse du tir : ")
    try:
        x = int(str_x)
    except ValueError:
        correct_x = False
        print("L'abscisse donnée pour le tir n'est pas un entier. Veuillez réessayer.")

correct_y = False
y = 0

while not correct_y:
    correct_y = True
    str_y = input("Donnez l'ordonnée du tir : ")
    try:
        y = int(str_y)
    except ValueError:
        correct_y = False
        print("L'ordonnée donnée pour le tir n'est pas un entier. Veuillez réessayer.")

grille_de_jeu.tirer(x, y)
grille_de_jeu.afficher()