import arcade
from constants import *

class Item(arcade.Sprite):
    def __init__(self,*,
                id=None, 
                name="Unamed-Item01",
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
        super().__init__(filename=filename, scale=scale, image_x=image_x,
                        image_y=image_y, image_width=image_width, image_height=image_height, 
                        center_x=center_x, center_y=center_y, flipped_horizontally=flipped_horizontally, 
                        flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, 
                        hit_box_algorithm=hit_box_algorithm, texture=texture, angle=angle)
        self.id = id
        self.name = name
        self.filename = filename
        self.is_tool=False
        self.is_consumable=False
        self.quantity = 1
        self.statistic_one = "Loren Ipsum Blah"
        self.statistic_two = "Loren Ipsum Blah"
        self.statistic_three = "Loren Ipsum Blah"
        self.description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text"