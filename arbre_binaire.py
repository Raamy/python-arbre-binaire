class ArbreBinaire:
    valeur = 0
    noeudGauche = None
    noeudDroit = None

    # ----- Getters et Setters -----

    def getValeur(self):
        return self.valeur

    def getNoeudGauche(self):
        return self.noeudGauche

    def getNoeudDroit(self):
        return self.noeudDroit

    def setValeur(self, valeur):
        self.valeur = valeur

    def setNoeudGauche(self, noeudGauche):
        self.noeudGauche = noeudGauche

    def setNoeudDroit(self, noeudDroit):
        self.noeudDroit = noeudDroit

    # ------------------------------

    # Affiche les données de l'ArbreBinaire()
    def __str__(self):
        return "\n----- Données du noeud -----" \
               + "\nValeur du noeud : " + str(self.valeur) \
               + "\nSous-noeud Gauche : " + str(self.noeudGauche) \
               + "\nSous-noeud Droit : " + str(self.noeudDroit)


class TestArbreBinaire:
    node: ArbreBinaire

    def __init__(self, valeur):
        self.node = ArbreBinaire()
        self.node.setValeur(valeur)
        print(self.node)


testArbreBinaire = TestArbreBinaire(10)
