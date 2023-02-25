import arcade
from constants import *
import math
import random
import character_lists
from classes.Character import Character
from classes.PlayerAccessory import PlayerAccessory

class Enemy(arcade.Sprite):
    def __init__(self,x,y,name,id):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.character_face_direction = FORWARD_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        # creates hitbox
        self.points = [[7, -16], [7, -8], [-7, -8], [-7, -16]]
        self.set_hit_box(self.points)
        self.wanders = True
        self.home = True
        self.home_x = x
        self.home_y = y
        self.x_range = 300
        self.y_range = 200
        self.wandering = False
        
        self.filename="assets/assetpacks/ninja/Actor/Monsters/Spirit2/SpriteSheet.png"
        self.center_x = x
        self.center_y = y
        self.room = 0
        self.name = name
        self.id = id
        self.speed = 3.0
        self.interacting = False
        self.load_textures()

    def wander(self):
        if self.wandering == False:
            if random.randint(0,500) == 1:
                if self.home == True:
                    if random.randint(0,1) == 1:
                        self.dest_x = self.home_x + random.randint(-self.x_range,self.x_range)
                        self.dest_y = self.home_y
                    else:
                        self.dest_x = self.home_x 
                        self.dest_y = self.home_y + random.randint(-self.y_range,self.y_range)
                else:
                    self.dest_x = self.home_x
                    self.dest_y = self.home_y
                self.wandering = True
        else:
            self.move_to(self.dest_x,self.dest_y)
        return
    
    def on_update(self, delta_time: float = 1 / 60):
        if self.wanders and self.interacting==False:
            self.wander()
        return super().on_update(delta_time)

    def move_to(self,dest_x,dest_y):
            start_x = self.center_x
            start_y = self.center_y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            if x_diff > 0:
                self.change_x = self.speed
                self.change_y = 0
            elif x_diff < 0:
                self.change_x = -self.speed
                self.change_y = 0
            if y_diff > 0:
                self.change_y = self.speed
                self.change_x = 0
            elif y_diff < 0:
                self.change_y = -self.speed
                self.change_x = 0

            self.center_x += self.change_x
            self.center_y += self.change_y

            # How far are we?
            distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

            # If we are there, head to the next point.
            if distance <= self.speed:
                self.center_x = self.dest_x
                self.center_y = self.dest_y
                self.change_x = 0
                self.change_y = 0
                if self.home == True:
                    self.home = False
                else:
                    self.home = True
                self.wandering = False

    def update_animation(self, delta_time: float = 1 / 60):        
        if self.change_x < 0 and self.change_y == 0:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.change_y == 0:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.change_x == 0:
            self.character_face_direction = FORWARD_FACING
        elif self.change_y > 0 and self.change_x == 0:
            self.character_face_direction = BACKWARD_FACING

        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_list[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 3 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.textures[frame][direction]
            
    def load_textures(self):
            self.filename="assets/assetpacks/ninja/Actor/Monsters/Spirit2/SpriteSheet.png"
            self.idle_texture_list = self.load_texture_list(self.filename, 0, 0, 0)
            self.textures = []
            for frame in range(4):
                texture = self.load_texture_list(self.filename, 0, frame, 0)
                self.textures.append(texture)

    def load_texture_list(self,filename, row, frame, color_offset):
        """
        Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
        Only loads a single frame.
        Offset is used where multiple colors are in the same sheet - for clothes etc.
        """
        FLAME_NATIVE_SIZE = 16
        color_offset = color_offset*ACCESSORIES_OFFSET
        return [
            arcade.load_texture(filename, x=color_offset+FLAME_NATIVE_SIZE*frame, y=FLAME_NATIVE_SIZE *
                                row, width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE),
            arcade.load_texture(filename, x=color_offset+FLAME_NATIVE_SIZE*frame, y=FLAME_NATIVE_SIZE*(
                row+1), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE),
            arcade.load_texture(filename, x=color_offset+FLAME_NATIVE_SIZE*frame, y=FLAME_NATIVE_SIZE*(
                row+2), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE),
            arcade.load_texture(filename, x=color_offset+FLAME_NATIVE_SIZE*frame, y=FLAME_NATIVE_SIZE*(
                row+3), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE)
        ]
            
    