from bateau import Bateau
from grille import Grille

def test_init():
    bateau_test = Bateau(1, 2)
    assert isinstance(bateau_test, Bateau)

def test_bateau_paramètres():
    bateau_test_1 = Bateau(2, 3)
    assert bateau_test_1.longueur == 1
    assert not bateau_test_1.vertical
    bateau_test_2 = Bateau(2, 3, longueur = 3, vertical = True)
    assert bateau_test_2.longueur == 3
    assert bateau_test_2.vertical

def test_positions():
    bateau_test_1 = Bateau(2, 3, longueur = 3)
    bateau_test_2 = Bateau(2, 3, longueur = 3, vertical = True)
    assert bateau_test_1.positions() == [(2, 3), (2, 4), (2, 5)]
    assert bateau_test_2.positions() == [(2, 3), (3, 3), (4, 3)]

def test_coulé():
    grille_test = Grille(5, 5)
    bateau_test = Bateau(2, 3, longueur = 3)
    grille_test.ajoute(bateau_test)
    assert not bateau_test.coulé(grille_test)
    grille_test.tirer(2, 3)
    assert not bateau_test.coulé(grille_test)
    grille_test.tirer(2, 4)
    grille_test.tirer(2, 5)
    assert bateau_test.coulé(grille_test)
