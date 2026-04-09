"""
le module principal du projet arcade_game

                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::


                 .:: ::::: ::.
                .::: ::::: :::.
               .:::' ::::: ':::.
              .::::' ::::: '::::.
             .::::'  :::::  '::::.
           .:::::'   :::::   ':::::.
         .::::::'    :::::    '::::::.
    ...:::::::'      :::::      ':::::::...
    :::::::''        :::::        '':::::::
    ::::''           :::::           ''::::

      _______ _______ _______ ______  ___
     |   _   |       |   _   |   _  \|   |(R)
     |.  1   |.|   | |.  1   |.  l   |.  |
     |.  _   `-|.  |-|.  _   |.  _  <|.  |
     |:  |   | |:  | |:  |   |:  |   |:  |
     |::.|:. | |::.| |::.|:. |::.|:. |::.|
     `--- ---' `---' `--- ---`--- ---`---'

"""

import pyxel
from arcade_game.spaceship import Spaceship
from arcade_game.enemy import Enemy
from random import randint
class Game:
    """
    Une classe pour notre jeu
    """
    def __init__(self):
        """
        Initialisation du jeu
        """
        self.w = 128 #largeur de l'écran
        self.h = 256 #hauteur de l'écran
        self.spaceship = Spaceship(self, self.w//2, self.h-8) #instanciation du vaisseau
        self.enemies=[]
        pyxel.init(self.w, self.h, title="Arcade Game")
        # chargement des images
        pyxel.load("images.pyxres")
        # --> appel de la fonction principale
        pyxel.run(self.update, self.draw)
        
        
    # =====================================================
    # == UPDATE (30FPS)
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        for tir in self.spaceship.shoots:
          tir.update()
        self.spaceship.update()
        self.update_shoots()
        self.create_enemy()
        print(len(self.enemies))
        for enemy in self.enemies:
          enemy.update()  
        
    def create_enemy(self):
      nb_frames = pyxel.frame_count
      if nb_frames%30 == 0:
        x = randint(0, 128)
        new_enemy = Enemy(self, x, -8)
        self.enemies.append(new_enemy)
        
    def remove_enemy(self):
      ecran_enemy=[]
      
      

    # =====================================================
    # == DRAW (30FPS)
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre 30 fois par seconde
        pyxel.cls(0)

        for enemy in self.enemies:
          enemy.draw()        
        for tir in self.spaceship.shoots:
          tir.draw()
        self.spaceship.draw()


    def update_shoots(self):
      visible_shoots =[]
      for tir in self.spaceship.shoots:
        if tir.y > 0 : 
          visible_shoots.append(tir)
      self.spaceship.shoots = visible_shoots
      
      
      
      
      
# instanciation de notre classe
Game()