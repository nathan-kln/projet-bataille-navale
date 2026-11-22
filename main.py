from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin

import random
from termcolor import cprint

NOMBRE_LIGNES = 8
NOMBRE_COLONNES = 10

type_de_bateau = ["torpilleur", "porte-avion", "sous-marin", "croiseur"]
nombre_bateau = len(type_de_bateau)
bateau_à_abattre = ["Torpilleur", "PorteAvion", "SousMarin", "Croiseur"]
nombre_bateau_à_abattre = len(bateau_à_abattre)

grille_jeu_joueur = Grille(NOMBRE_LIGNES, NOMBRE_COLONNES)
grille_jeu_interne = Grille(NOMBRE_LIGNES, NOMBRE_COLONNES)
places_prises_bateau = set()
liste_bateau_vivant = []

def clear_screen():
    for _ in range(100):
        print('\n')

def enumeration_couple(choix_bateau : str):
    positions_et_bateaux_acceptables = []
    for placement_ligne in range(NOMBRE_LIGNES):
        for placement_colonne in range(NOMBRE_COLONNES):
            for vertical in [True, False]:
                if choix_bateau == "torpilleur":
                    bateau_possible = Torpilleur(placement_ligne, placement_colonne, vertical = vertical)
                if choix_bateau == "porte-avion":
                    bateau_possible = PorteAvion(placement_ligne, placement_colonne, vertical = vertical)
                if choix_bateau == "sous-marin":
                    bateau_possible = SousMarin(placement_ligne, placement_colonne, vertical = vertical)
                if choix_bateau == "croiseur":
                    bateau_possible = Croiseur(placement_ligne, placement_colonne, vertical = vertical)
                positions_à_tester = bateau_possible.positions()
                positions_dans_grille = all(0 <= ligne < NOMBRE_LIGNES and 0 <= colonne < NOMBRE_COLONNES for ligne, colonne in positions_à_tester)

                if all(positions not in places_prises_bateau for positions in positions_à_tester) and positions_dans_grille:
                    positions_et_bateaux_acceptables.append((bateau_possible.positions(), bateau_possible))
    return positions_et_bateaux_acceptables

def choix_coordonnées_tir():
    correct_x = False
    x = 0
    while not correct_x:
        correct_x = True
        str_x = input("Donnez l'abscisse du tir : ")
        try:
            x = int(str_x)
            if not (0 <= x < NOMBRE_COLONNES):
                print(f"L'abscisse doit être comprise entre 0 et {NOMBRE_COLONNES - 1}. Veuillez réessayer.")
                correct_x = False
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
            if not (0 <= y < NOMBRE_COLONNES):
                print(f"L'ordonnée doit être comprise entre 0 et {NOMBRE_LIGNES - 1}. Veuillez réessayer.")
                correct_y = False
        except ValueError:
            correct_y = False
            print("L'ordonnée donnée pour le tir n'est pas un entier. Veuillez réessayer.")
    return x,y


def message_coulé(bateau_coulé : Bateau) -> str:
    if type(bateau_coulé) == PorteAvion :
        return 'Capitaine ! Vous avez coulé un porte-avion !'
    elif type(bateau_coulé) == Torpilleur :
        return 'Capitaine ! Vous avez coulé un torpilleur !'
    elif type(bateau_coulé) == SousMarin :
        return 'Capitaine ! Vous avez coulé un sous-marin !'
    elif type(bateau_coulé) == Croiseur :
        return 'Capitaine ! Vous avez coulé un croiseur !'

for _ in range(nombre_bateau):
    bateau_placé = False
    choix_bateau = random.choice(type_de_bateau)
    type_de_bateau.remove(choix_bateau)
    while not bateau_placé:
        position_choisie, bateau_choisi = random.choice(enumeration_couple(choix_bateau))
        if all(position not in places_prises_bateau for position in position_choisie):
            bateau_placé = True
    grille_jeu_interne.ajoute(bateau_choisi)
    liste_bateau_vivant.append(bateau_choisi)
    for case_occupée in bateau_choisi.positions():
        places_prises_bateau.add(case_occupée)

compteur_tours = 1

while len(liste_bateau_vivant) > 0:
    grille_jeu_joueur.afficher()
    x, y = choix_coordonnées_tir()
    if (x,y) in places_prises_bateau:
        clear_screen()
        cprint("Touché !", "red", attrs=["bold"])
        compteur_tours += 1
        grille_jeu_interne.tirer(x, y, touche = 'x')
        grille_jeu_joueur.tirer(x, y, touche = "💣")
        for bateau_vivant in liste_bateau_vivant:
            if bateau_vivant.coulé(grille_jeu_interne):
                cprint("Coulé !", "red", "on_white", attrs=["bold"])
                cprint(message_coulé(bateau_vivant), "green", attrs=["italic"])
                liste_bateau_vivant.remove(bateau_vivant)
                for ligne, colonne in bateau_vivant.positions():
                    grille_jeu_joueur.tirer(ligne, colonne, touche=bateau_vivant.sigle)
    else :
        compteur_tours += 1
        grille_jeu_interne.tirer(x, y)
        grille_jeu_joueur.tirer(x, y)
        clear_screen()
        cprint("Plouf !", "blue", attrs=["bold"])

grille_jeu_joueur.afficher()
cprint("Jeu terminé !", "yellow", "on_green", attrs=["blink"])
cprint(f"Félicitations ! Vous avez décimé la flotte en {compteur_tours} coups.", attrs=["italic"])
    