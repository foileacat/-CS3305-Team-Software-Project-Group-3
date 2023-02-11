import arcade
from constants import *
import character_lists
from classes.PlayerAccessory import PlayerAccessory

class PlayerCharacter(arcade.Sprite):

    """Creates our player"""

    def __init__(self):
        super().__init__()
        #initialise starting position
        self.center_x = 200
        self.center_y = 500
        self.character_face_direction = RIGHT_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        # creates hitbox
        self.points = [[7, -16], [7, -8], [-7, -8], [-7, -16]]

        # Select the desired asset file from our character_lists file
        skintone_file = character_lists.skintones[2]
        hairstyle_file = character_lists.hairstyles[7]
        clothing_file = character_lists.clothing[3]
        # initialise accessory list and add PlayerAccesories to it
        self.accessory_list = arcade.SpriteList()
        self.hair = PlayerAccessory(character_lists.hairstyles,7,2)
        self.clothes = PlayerAccessory(character_lists.clothing,7,3)
        #self.bottoms
        #self.shoes
        #self.fullbody
        self.accessory_list.append(self.clothes)
        self.accessory_list.append(self.hair)
        # load textures for standing still and for walking animation
        self.idle_texture_list = load_texture_list(skintone_file, 0, 0, 0)

        self.walk_textures = []
        for frame in range(8):
            texture = load_texture_list(skintone_file, 0, frame, 0)
            self.walk_textures.append(texture)

        self.currently_inspecting = False
    # runs constantly, animates character moving

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.change_y == 0:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.change_y == 0:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.change_x == 0:
            self.character_face_direction = UP_FACING
        elif self.change_y > 0 and self.change_x == 0:
            self.character_face_direction = DOWN_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_list[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]


def load_texture_list(filename, row, frame, offset):
    """
    Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
    Only loads a single frame.
    Offset is used where multiple colors are in the same sheet - for clothes etc.
    """
    offset = offset*ACCESSORIES_OFFSET
    return [
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                            row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+1), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+2), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+3), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE)
    ]
