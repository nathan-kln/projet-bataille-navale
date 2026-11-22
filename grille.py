class Grille:

    vide = '∿'

    def __init__(self, nombre_lignes : int, nombre_colonnes : int):
        self.nombre_colonnes = nombre_colonnes
        self.matrice = [Grille.vide for _ in range(nombre_colonnes * nombre_lignes)]

    def tirer(self, ligne, colonne, touche = 'x'):
        self.matrice[ligne * self.nombre_colonnes + colonne] = touche

    def __str__(self) -> str:
        grille_print_str = ''
        for case_index in range(len(self.matrice)):
            if (case_index != 0) and (case_index % self.nombre_colonnes == 0):
                grille_print_str += '\n'
            grille_print_str += self.matrice[case_index]
        return grille_print_str

    def afficher(self):
        print(self)

    def ajoute(self, bateau):
        nombre_lignes = len(self.matrice) // self.nombre_colonnes
        positions_bateau = bateau.positions()
        for ligne, colonne in positions_bateau:
            if (ligne >= nombre_lignes) or (colonne >= self.nombre_colonnes):
                print('Le bateau dépasse.')
                return False
        for ligne, colonne in positions_bateau:
            self.matrice[ligne * self.nombre_colonnes + colonne] = bateau.sigle
        return True