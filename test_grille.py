from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin

def test_init():
    grille_de_test = Grille(7, 7)
    assert isinstance(grille_de_test, Grille)

def test_contructeur():
    grille_de_test = Grille(2, 4)
    assert grille_de_test.matrice == [Grille.vide] * (2 * 4)

def test_tirer():
    grille_test = Grille(3, 2)
    grille_test.tirer(1, 1)
    assert grille_test.matrice == [Grille.vide, Grille.vide, Grille.vide, 'x', Grille.vide, Grille.vide]

def test_str():
    grille_test = Grille(5, 8)
    assert str(grille_test) == '∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿'
    grille_test.tirer(2, 3)
    assert str(grille_test) == '∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿x∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿'

def test_ajoute():
    grille_test = Grille(2, 3)
    bateau_test = Bateau(1, 0, longueur = 2, vertical = False)
    grille_test.ajoute(bateau_test)
    assert grille_test.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]
    nouvelle_grille_test = Grille(2, 3)
    nouveau_bateau_test_1 = Bateau(1, 0, longueur = 2, vertical = True)
    nouveau_bateau_test_2 = Bateau(1, 0, longueur = 4, vertical = True)
    nouvelle_grille_test.ajoute(nouveau_bateau_test_1)
    nouvelle_grille_test.ajoute(nouveau_bateau_test_2)
    assert nouvelle_grille_test.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]

def test_ajoute_porte_avion():
    grille_test = Grille(2, 5)
    bateau_test = PorteAvion(0, 1)
    assert isinstance(bateau_test, PorteAvion)
    grille_test.ajoute(bateau_test)
    assert grille_test.matrice == ['∿', '🚢', '🚢', '🚢', '🚢', '∿', '∿', '∿', '∿', '∿']

def test_ajoute_croiseur():
    grille_test = Grille(3, 3)
    bateau_test = Croiseur(0, 1, vertical = True)
    assert isinstance(bateau_test, Croiseur)
    grille_test.ajoute(bateau_test)
    assert grille_test.matrice == ['∿', '⛴','∿',
                                   '∿', '⛴', '∿',
                                   '∿', '⛴', '∿']

def test_ajoute_torpilleur():
    grille_test = Grille(2, 3)
    bateau_test = Torpilleur(1, 0)
    assert isinstance(bateau_test, Torpilleur)
    grille_test.ajoute(bateau_test)
    assert grille_test.matrice == ['∿', '∿', '∿', '🚣', '🚣', '∿']

def test_ajoute_sous_marin():
    grille_test = Grille(2, 3)
    bateau_test = SousMarin(1, 0)
    assert isinstance(bateau_test, SousMarin)
    grille_test.ajoute(bateau_test)
    assert grille_test.matrice == ['∿', '∿', '∿', '🐟', '🐟', '∿']