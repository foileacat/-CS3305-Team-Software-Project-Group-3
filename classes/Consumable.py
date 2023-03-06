import arcade
from classes.Item import Item
from constants import *

class Consumable(Item):
    def __init__(self,*,
                id=None, 
                name="None",
                filename=None, 
                scale=SPRITE_SCALING, 
                image_x=0, 
                image_y=0, 
                image_width=0, 
                image_height=0, 
                center_x=0, 
                center_y=0,
                flipped_horizontally=False, 
                flipped_vertically=False, 
                flipped_diagonally=False,
                hit_box_algorithm='Simple',
                texture=None, 
                angle=0,
                **kwargs):
        super().__init__(id=id,filename=filename, name=name,scale=scale, image_x=image_x,
                        image_y=image_y, image_width=image_width, image_height=image_height, 
                        center_x=center_x, center_y=center_y, flipped_horizontally=flipped_horizontally, 
                        flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, 
                        hit_box_algorithm=hit_box_algorithm, texture=texture, angle=angle)
        
        self.is_consumable=True
        self.health = 10

    def be_consumed(self):
        #play sound?
        #change stats
        return
    def generate_stats(self):
        self.statistic_one = "Health: +" + str(self.health)
