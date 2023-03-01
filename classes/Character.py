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
        self.using_tool = False
        self.carrying = False
        self.dying = False
        self.center_x = 0
        self.center_y = 0
        self.character_face_direction = FORWARD_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        # creates hitbox
        self.points = [[7, -16], [7, -8], [-7, -8], [-7, -16]]
        self.set_hit_box(self.points)
        # Select the desired asset file from our character_lists file
        self.skintone_file = character_lists.skintones[2]
        self.accessory_list = arcade.SpriteList()
        textures = self.load_texture_list(self.skintone_file, 0, 0, 0)
        self.texture = textures[0]
        self.load_textures()
        
    def load_textures(self):
        self.idle_texture_list = self.load_texture_list(self.skintone_file, 0, 0, 0)
        self.idle_carry_texture_list = self.load_texture_list(self.skintone_file, 12, 0, 0)

        self.walk_textures = []
        for frame in range(8):
            texture = self.load_texture_list(self.skintone_file, 0, frame, 0)
            self.walk_textures.append(texture)

        self.carry_textures = []
        for frame in range(8):
            texture = self.load_texture_list(self.skintone_file, 12, frame, 0)
            self.carry_textures.append(texture)

        self.sword_textures = []
        for frame in range(4):
            texture = self.load_texture_list(self.skintone_file, 16, frame, 0)
            self.sword_textures.append(texture)

        self.pickaxe_textures = []
        for frame in range(5):
            texture = self.load_texture_list(self.skintone_file, 29, frame, 0)
            self.pickaxe_textures.append(texture)
    
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
        
        if self.carrying == True:
            if self.change_x == 0 and self.change_y == 0:
                self.texture = self.idle_carry_texture_list[self.character_face_direction]
                return
            self.cur_texture += 1
            if self.cur_texture > 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            frame = self.cur_texture // UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.carry_textures[frame][direction]
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

       
    def load_texture_list(self,filename, row, frame, color_offset):
        """
        Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
        Only loads a single frame.
        Offset is used where multiple colors are in the same sheet - for clothes etc.
        """
        color_offset = color_offset*ACCESSORIES_OFFSET
        return [
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                                row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
                row+1), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
                row+2), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
                row+3), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple")
        ]
    
    def load_horizontal_texture_pair(self,filename, row, frame, color_offset):
        color_offset = color_offset*ACCESSORIES_OFFSET
        return [
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                                row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*(frame+1), y=CHARACTER_NATIVE_SIZE*(
                row), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple"),
        ]
    
    def generate_floating_head(self,x,y):
        scale = 4.5
        list = arcade.SpriteList()
        self.head_sprite = arcade.Sprite(filename=character_lists.skintones[2],scale=scale,image_width=32,image_height=28,center_x=x,center_y=y)
        self.shirt_sprite = arcade.Sprite(filename=self.shirt.file_path,image_x=self.shirt.color_offset*ACCESSORIES_OFFSET,scale=scale,image_width=32,image_height=28,center_x=x,center_y=y)
        self.hair_sprite = arcade.Sprite(filename=self.hair.file_path,image_x=self.hair.color_offset*ACCESSORIES_OFFSET,scale=scale,image_width=32,image_height=28,center_x=x,center_y=y)
        self.full_body_sprite = arcade.Sprite(filename=self.full_body.file_path,image_x=self.full_body.color_offset*ACCESSORIES_OFFSET,scale=scale,image_width=32,image_height=28,center_x=x,center_y=y)
        list.append(self.head_sprite)
        list.append(self.shirt_sprite)
        list.append(self.hair_sprite)
        return list
    
    def is_holding_item(self):
        if self.inventory_bar.current_slot().occupied:
            if self.inventory_bar.current_slot().item.is_tool == False:
                return True
            else:
                return False
        return False
