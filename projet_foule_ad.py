## Projet foule ##

class Voyageur :

def get_position(self):
    """ recupère les coordonnées"""

def get_position_future(self):
    """ recupère les coordonnées de là où il voudrait aller"""
    
class Obstacle :
    pass
class Carte :
    pass


# définition des constantes
dimension_carte=(20,20)
pas = 1

#initialisation des objets
voyageur1 = Voyageur(0,10,pas)
voyageur2 = Voyageur(0,11,pas)
map1 = Carte(dimension_carte)
liste_voyageur = map1.ajout_voyageur(voyageur1,voyageur2)


while len(liste_voyageur):
    for voy in liste_voyageur:
        if voy.projet_deplacement(voy.get_position(),voy.get_position_future()):
            voy.deplacement()
            map1.update_carte(voy)
            if voy.atteinte_objectif():
                map1.retrait_voyageur(voy)
            
