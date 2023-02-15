import arcade
from constants import *
import character_lists
from classes.PlayerAccessory import PlayerAccessory
from classes.Character import Character

class PlayerCharacter(Character):

    """Creates our player"""

    def __init__(self):
        super().__init__()
        #initialise starting position
        self.center_x = 200
        self.center_y = 500
        # Select the desired asset file from our character_lists file
        skintone_file = character_lists.skintones[4]
        
        # initialise accessory list and add PlayerAccesories to it
        self.hair = PlayerAccessory(character_lists.hairstyles,7,2)
        self.shirt = PlayerAccessory(character_lists.tops,7,3)
        self.bottoms = PlayerAccessory(character_lists.bottoms,2,6)
        self.full_body = PlayerAccessory(character_lists.full_body,4,6)
        self.shoes = PlayerAccessory(character_lists.shoes,0,1)
        self.full_body.alpha = 0
        self.populate_accessory_list()
        self.currently_inspecting = False
        self.currently_npc_interacting = False
   
    