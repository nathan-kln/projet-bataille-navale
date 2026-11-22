from bateau import Bateau

'''
Nom : "chevauchement"
Utilisateur : un joueur
Story : Positionner des bateaux sans chevauchement
Actions :

    1) Créer un bateau b1
    2) Créer un bateau b2
    3) Vérifier si les deux bateaux se chevauchent
'''

b1 = Bateau(2, 3, longueur = 3)
b2 = Bateau(1, 4, longueur = 4, vertical = True)
print('On chosit des bateaux qui normalement se chevauchent.')
print('Les bateaux se chevauchent-ils ? Réponse :', any(position_prise in b1.positions() for position_prise in b2.positions()))

print("On chosit d'autres bauteaux qui normalement ne se chevauchent pas.")

b1 = Bateau(2, 3, longueur = 3)
b2 = Bateau(4, 5, longueur = 3, vertical = True)

print('Les bateaux se chevauchent-ils ? Réponse :', any(position_prise in b1.positions() for position_prise in b2.positions()))

