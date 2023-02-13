import arcade
from constants import *
import character_lists
from classes.PlayerAccessory import PlayerAccessory

class Character(arcade.Sprite):

    """Creates our Character"""

    def __init__(self):
        super().__init__()
        #initialise starting position
        self.attacking = False
        self.pickaxing = False
        self.center_x = 0
        self.center_y = 0
        self.character_face_direction = FORWARD_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        # creates hitbox
        self.points = [[7, -16], [7, -8], [-7, -8], [-7, -16]]
        
        # Select the desired asset file from our character_lists file
        skintone_file = character_lists.skintones[0]
        self.accessory_list = arcade.SpriteList()
        self.idle_texture_list = self.load_texture_list(skintone_file, 0, 0, 0)

        self.walk_textures = []
        for frame in range(8):
            texture = self.load_texture_list(skintone_file, 0, frame, 0)
            self.walk_textures.append(texture)
        self.carry_textures = []
        for frame in range(8):
            texture = self.load_texture_list(skintone_file, 12, frame, 0)
            self.carry_textures.append(texture)
        self.sword_textures = []
        for frame in range(4):
            texture = self.load_texture_list(skintone_file, 16, frame, 0)
            self.sword_textures.append(texture)
        self.pickaxe_textures = []
        for frame in range(5):
            texture = self.load_texture_list(skintone_file, 29, frame, 0)
            self.pickaxe_textures.append(texture)
    
    # runs constantly, animates character moving
    def populate_accessory_list(self):
        self.accessory_list.append(self.shirt)
        self.accessory_list.append(self.bottoms)
        self.accessory_list.append(self.hair)
        self.accessory_list.append(self.shoes)
        self.accessory_list.append(self.full_body)

    def update_animation(self, delta_time: float = 1 / 60):
        for accessory in self.accessory_list:
            accessory.update_animation(self)
        if self.change_x < 0 and self.change_y == 0:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.change_y == 0:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.change_x == 0:
            self.character_face_direction = FORWARD_FACING
        elif self.change_y > 0 and self.change_x == 0:
            self.character_face_direction = BACKWARD_FACING

        if self.pickaxing == True:
            self.cur_texture += 1
            if self.cur_texture > 4 * UPDATES_PER_FRAME:
                self.cur_texture = 0
                self.pickaxing = False
            frame = self.cur_texture // UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.pickaxe_textures[frame][direction]
            return
        
        if self.attacking == True:
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
                self.attacking = False
            frame = self.cur_texture // UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.sword_textures[frame][direction]
            return
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

        if self.attacking == True:
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
                self.attacking = False
            frame = self.cur_texture // UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.sword_textures[frame][direction]

    def load_texture_list(self,filename, row, frame, color_offset):
        """
        Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
        Only loads a single frame.
        Offset is used where multiple colors are in the same sheet - for clothes etc.
        """
        color_offset = color_offset*ACCESSORIES_OFFSET
        return [
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                                row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
                row+1), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
                row+2), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
                row+3), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE)
        ]
