class Bateau:

    sigle = '⛵'

    def __init__(self, ligne : int, colonne : int, longueur = 1, vertical = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self) -> list:
        liste_positions = []
        if self.vertical:
            for index_position in range(self.longueur):
                liste_positions.append((self.ligne + index_position, self.colonne))
        else :
            for index_position in range(self.longueur):
                liste_positions.append((self.ligne, self.colonne + index_position))
        return liste_positions

    def coulé(self, grille) -> bool:
        for ligne, colonne in self.positions():
            if grille.matrice[ligne * grille.nombre_colonnes + colonne] != 'x':
                return False
        return True

class PorteAvion(Bateau):

    sigle = '🚢'

    def __init__(self, ligne: int, colonne: int, vertical = False):
        super().__init__(ligne, colonne, longueur = 4, vertical = vertical)


class Croiseur(Bateau):

    sigle = '⛴'

    def __init__(self, ligne: int, colonne: int, vertical = False):
        super().__init__(ligne, colonne, longueur=3, vertical = vertical)


class Torpilleur(Bateau):

    sigle = '🚣'

    def __init__(self, ligne: int, colonne: int, vertical =  False):
        super().__init__(ligne, colonne, longueur=2, vertical = vertical)


class SousMarin(Bateau):

    sigle = '🐟'

    def __init__(self, ligne: int, colonne: int, vertical = False):
        super().__init__(ligne, colonne, longueur=2, vertical = vertical)