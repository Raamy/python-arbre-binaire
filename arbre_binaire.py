class ArbreBinaire:
    valeur = 0
    noeudGauche = 0
    noeudDroit = 0

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
        return "\n----------" \
               + "\nValeur du noeud : " + str(self.valeur) \
               + "Sous-noeud Gauche : " + str(self.noeudGauche) \
               + "Sous-noeud Droit : " + str(self.noeudDroit)


