import arcade
from constants import *
from character_lists import full_body
class PlayerAccessory(arcade.Sprite):

    """
    Creates Accesory for character - clothes,hair,eyes etc. 
    These are added to the players accesory sprite list 
    """

    def __init__(self, asset_list,asset_index,color_offset):
        super().__init__()
        self.asset_list = asset_list
        self.asset_index = asset_index
        self.file_path = self.asset_list[self.asset_index]
        self.face_direction = RIGHT_FACING
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        self.points = [[6, -16], [6, 4], [6, 4], [6, -16]]  # creates hitbox
        self.color_offset = color_offset  # the offset to choose the color of the accesory
        self.load_textures()
        # Load textures for idle standing

    def __str__(self):
        return f"Type is {self.asset_list}, style is {self.asset_index} and color is {self.color_offset}"
    
    def load_textures(self):
        self.idle_texture_list = load_texture_list(
            self.file_path, 0, 0, self.color_offset)
        # Load textures for walking
        self.walk_textures = []
        # loads each frame
        for frame in range(8):
            texture = load_texture_list(
                self.file_path, 0, frame, self.color_offset)
            self.walk_textures.append(texture)

    def change_color(self):
        if self.asset_list == full_body:
            if self.asset_index <= 1:
                overflow = 0
            elif self.asset_index <=3:
                overflow = 1
            else:
                overflow = 7
        else:
            overflow = 7
        self.color_offset+=1
        if self.color_offset > overflow:
            self.color_offset = 0
        self.load_textures()

    def change_style(self):
        if self.alpha == 0:
            self.alpha = 255
            self.file_path = self.asset_list[self.asset_index]
            self.load_textures()
            print(self.asset_index)
            return
        else:
            self.asset_index+=1
            if self.asset_index >= len(self.asset_list):
                self.alpha = 0
                self.asset_index = 0
                if self.asset_list == full_body:
                    self.color_offset = 0
            print(self.asset_index)
            self.file_path = self.asset_list[self.asset_index]
            self.load_textures()

    def update_animation(self, player_sprite, delta_time: float = 1 / 60):
        self.face_direction = player_sprite.character_face_direction
        self.center_x = player_sprite.center_x
        self.center_y = player_sprite.center_y
        # Walking animation
        if player_sprite.change_x == 0 and player_sprite.change_y == 0:
            self.texture = self.idle_texture_list[self.face_direction]
            return
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.face_direction
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
