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
        self.hide = False
        # Load textures for idle standing

    def __str__(self):
        return f"Type is {self.asset_list}, style is {self.asset_index} and color is {self.color_offset}"
    
    def load_textures(self):
        self.idle_texture_list = load_texture_list(
            self.file_path, 0, 0, self.color_offset)
        self.idle_carry_texture_list = load_texture_list(
            self.file_path, 12, 0, self.color_offset)
        
        self.dying_textures = load_horizontal_texture_pair(self.file_path, 28, 0, self.color_offset)
        # Load textures for walking
        self.walk_textures = []
        # loads each frame
        for frame in range(8):
            texture = load_texture_list(
                self.file_path, 0, frame, self.color_offset)
            self.walk_textures.append(texture)
        self.carry_textures = []
        for frame in range(8):
            texture = load_texture_list(
                self.file_path, 12, frame, self.color_offset)
            self.carry_textures.append(texture)
        self.sword_textures = []
        for frame in range(4):
            texture = load_texture_list(
                self.file_path, 16, frame, self.color_offset)
            self.sword_textures.append(texture)
        self.pickaxe_textures = []
        for frame in range(5):
            texture = load_texture_list(
                self.file_path, 29, frame, self.color_offset)
            self.pickaxe_textures.append(texture)

        self.watering_textures = []
        for frame in range(2):
            texture = load_texture_list(self.file_path, 37, frame, self.color_offset)
            self.watering_textures.append(texture)

        self.damage_textures = []
        for frame in range(3):
            texture = load_texture_list(self.file_path, 24, 0, self.color_offset)
            self.damage_textures.append(texture)

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
        print("color",self.color_offset)

    def change_style(self):
        if self.alpha == 0:
            self.alpha = 255
            self.file_path = self.asset_list[self.asset_index]
            self.load_textures()
            return
        else:
            self.asset_index+=1
            if self.asset_index >= len(self.asset_list):
                self.alpha = 0
                self.asset_index = 0
                if self.asset_list == full_body:
                    self.color_offset = 0
            self.file_path = self.asset_list[self.asset_index]
            self.load_textures()
            print("style",self.asset_index)
    def update_animation(self, player_sprite, delta_time: float = 1 / 60):
        self.face_direction = player_sprite.character_face_direction
        self.center_x = player_sprite.center_x
        self.center_y = player_sprite.center_y
        self.cur_texture = player_sprite.cur_texture
        if player_sprite.dead:
            return
        # Walking animation
        if player_sprite.dying:
            self.update_dying_frames(2,self.dying_textures,40)
            return
        if player_sprite.taking_damage:
            self.update_damage_frames(3,self.damage_textures,10)
            return
        if player_sprite.using_tool==True:
            use_speed = player_sprite.current_item().use_speed
            if player_sprite.current_item().type == "Pickaxe":
                self.update_tool_frames(5,self.pickaxe_textures,use_speed)
                return
            if player_sprite.current_item().type == "Sword":
                self.update_tool_frames(4, self.sword_textures,use_speed)
                return
            if player_sprite.current_item().type == "Watering Can":
                self.update_tool_frames(2, self.watering_textures,use_speed)
                return
            return
        else:
            if player_sprite.is_holding_item():
                if player_sprite.current_item().is_tool == False:
                    if player_sprite.change_x == 0 and player_sprite.change_y == 0:
                        self.texture = self.idle_carry_texture_list[self.face_direction]
                        return
                    self.cur_texture += 1
                    if self.cur_texture > 7 * UPDATES_PER_FRAME:
                        self.cur_texture = 0
                        self.attacking = False
                    frame = self.cur_texture // UPDATES_PER_FRAME
                    direction = self.face_direction
                    self.texture = self.carry_textures[frame][direction]
                    return
            
            if player_sprite.change_x == 0 and player_sprite.change_y == 0:
                self.texture = self.idle_texture_list[self.face_direction]
                return
            
            self.cur_texture += 1
            if self.cur_texture > 7 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            frame = self.cur_texture // UPDATES_PER_FRAME
            direction = self.face_direction
            self.texture = self.walk_textures[frame][direction]
        
    def update_tool_frames(self, max_frames, texture_dict,use_speed):
        self.cur_texture += 1
        if self.cur_texture > max_frames * use_speed:
            self.cur_texture = 0
            self.using_tool = False
        frame = self.cur_texture // use_speed
        direction = self.face_direction
        if frame == max_frames:
            frame=max_frames-1
        self.texture = texture_dict[frame][direction]
        return
    
    def update_damage_frames(self, max_frames, texture_dict,use_speed):
        self.cur_texture += 1
        if self.cur_texture > max_frames * use_speed:
            self.cur_texture = 0
            self.taking_damage = False
        frame = self.cur_texture // use_speed
        direction = self.face_direction
        if frame == max_frames:
            frame=max_frames-1
        self.texture = texture_dict[frame][direction]
        return
    
    def update_dying_frames(self, max_frames, texture_dict,use_speed):
            self.cur_texture += 1
            if self.cur_texture > max_frames * use_speed:
                return
            frame = self.cur_texture // use_speed
            if frame == max_frames:
                frame=max_frames-1
            self.texture = texture_dict[frame]
            return
    
def load_texture_list(filename, row, frame, offset):
    """
    Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
    Only loads a single frame.
    Offset is used where multiple colors are in the same sheet - for clothes etc.
    """
    offset = offset*ACCESSORIES_OFFSET
    return [
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                            row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm=HIT_BOX_ALGORITHM),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+1), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm=HIT_BOX_ALGORITHM),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+2), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm=HIT_BOX_ALGORITHM),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+3), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm=HIT_BOX_ALGORITHM)
    ]

def load_horizontal_texture_pair(filename, row, frame, color_offset):
        color_offset = color_offset*ACCESSORIES_OFFSET
        return [
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                                row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+CHARACTER_NATIVE_SIZE*(frame+1), y=CHARACTER_NATIVE_SIZE*(
                row), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE,hit_box_algorithm="Simple"),
        ]
