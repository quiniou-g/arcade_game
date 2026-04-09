import pyxel
from random import randint
class Enemy :
    """
    Une classe pour les ennemis du jeu
    """
    def __init__(self, jeu, x, y):
        """Initialisation des enenemis

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.jeu = jeu
        # position initiale de l'ennemi
        self.x = x
        self.y = y
        # largeur (width) et hauteur de l'ennemi (height)
        self.w = 8
        self.h = 8
    
    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour du vaisseau (30FPS)
        """
        self.y+=2
        
        
    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin d'un ennemi
        """
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8)
