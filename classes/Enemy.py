import arcade
from constants import *
import math
import random
import character_lists
from classes.Character import Character
from classes.PlayerAccessory import PlayerAccessory
ENEMY_FORWARD_FACING = 0
ENEMY_BACKWARD_FACING = 1
ENEMY_RIGHT_FACING = 3
ENEMY_LEFT_FACING = 2
class Enemy(arcade.Sprite):
    def __init__(self,x,y,name,id):
        super().__init__()
        self.start_x = x
        self.start_y = y
        self.character_face_direction = ENEMY_FORWARD_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = 5
        # creates hitbox
        self.filename="assets/assetpacks/ninja/Actor/Monsters/Spirit2/SpriteSheet.png"
        self.center_x = x
        self.center_y = y
        self.name = name
        self.id = id
        self.load_textures()
        self.speed = 2
        self.damage = 3
        self.following = False
        self.cooldown = 101
        self.knockback = 4
        self.taking_damage = False
        self.max_health = 10
        self.health = self.max_health
        self.dying = False
        self.dead = False

    def on_update(self, delta_time: float = 1 / 60):
        return super().on_update(delta_time)
    
    def update(self):
        if self.dead:
            self.die()
        elif self.health < 0:
            self.dying = True
            #self.color = arcade.color.BLACK
            return
        else:
            if self.following:
                if self.cooldown > 20:
                    self.follow_sprite(self.target)
                self.cooldown += 1
            else:
                self.change_x = 0
                self.change_y = 0
            return

    def reset_cooldown(self):
        self.cooldown = 0
    
    def take_damage(self,enemy):
        x_diff = self.center_x - enemy.center_x
        y_diff = self.center_y - enemy.center_y-16
        
        if x_diff <= 0 and abs(x_diff) > abs(y_diff):
            self.character_face_direction=RIGHT_FACING
            self.center_x -= enemy.knockback*10

        if x_diff >= 0 and abs(x_diff) > abs(y_diff):
            self.character_face_direction=LEFT_FACING
            self.center_x += enemy.knockback*10
            
        if y_diff >= 0 and abs(x_diff) < abs(y_diff):
            self.character_face_direction=FORWARD_FACING
            self.center_y += enemy.knockback*10

        if y_diff <= 0 and abs(x_diff) < abs(y_diff):
            self.character_face_direction=BACKWARD_FACING
            self.center_y -= enemy.knockback*10
        self.taking_damage = True
        self.health -= enemy.damage
        return

    def follow_sprite(self, player_sprite):
        if self.center_y < player_sprite.center_y:
            self.change_y =  min(self.speed, player_sprite.center_y - self.center_y)
            self.change_x = 0
            self.center_y += self.change_y
    
        elif self.center_y > player_sprite.center_y:
            self.change_y = -min(self.speed, self.center_y - player_sprite.center_y)
            self.change_x = 0
            self.center_y += self.change_y
     
        elif self.center_x < player_sprite.center_x:
            self.change_x = min(self.speed, player_sprite.center_x - self.center_x)
            self.change_y = 0
            self.center_x += self.change_x
         
        elif self.center_x > player_sprite.center_x:
            self.change_x = -min(self.speed, self.center_x - player_sprite.center_x)
            self.change_y = 0
            self.center_x += self.change_x
           
    def update_animation(self, delta_time: float = 1 / 60): 
        if self.change_x < 0 and self.change_y == 0:
            self.character_face_direction = ENEMY_LEFT_FACING
        elif self.change_x > 0 and self.change_y == 0:
            self.character_face_direction = ENEMY_RIGHT_FACING
        elif self.change_y < 0 and self.change_x == 0:
            self.character_face_direction = ENEMY_FORWARD_FACING
        elif self.change_y > 0 and self.change_x == 0:
            self.character_face_direction = ENEMY_BACKWARD_FACING
        else:
            self.character_face_direction = ENEMY_FORWARD_FACING

        if self.dying:
            self.update_death_frames(6,self.death_textures,5)
            return
        
        if self.taking_damage:
            self.update_damage_frames(4,self.damage_textures,5)
            return
        
        if self.change_x == 0 and self.change_y == 0:
            self.cur_texture += 1
            if self.cur_texture > 3 * (UPDATES_PER_FRAME+3):
                self.cur_texture = 0
            frame = self.cur_texture // (UPDATES_PER_FRAME+3)
            direction = self.character_face_direction
            self.texture = self.texture_list[frame][direction]
        else:
        # Walking animation
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            frame = self.cur_texture // UPDATES_PER_FRAME
            direction = self.character_face_direction
            self.texture = self.texture_list[frame][direction]
            
            
    def load_textures(self):
            self.filename="assets/assetpacks/ninja/Actor/Monsters/Spirit2/SpriteSheet.png"
            self.death_filename = "assets/assetpacks/ninja/FX/Smoke/Smoke/SpriteSheet.png"
            self.idle_texture_list = self.load_texture_list_vertical(self.filename, 0, 0, 0)
            self.texture_list = []
            for frame in range(4):
                texture = self.load_texture_list_vertical(self.filename, 0, frame, 0)
                self.texture_list.append(texture)
            self.damage_textures = []
            for frame in range(4):
                texture = self.load_texture_list(self.filename, 0, frame, 0)
                self.damage_textures.append(texture)

            self.death_textures = self.load_death_textures(self.death_filename, 0, 0, 0)

    def load_texture_list_vertical(self,filename, row, frame, color_offset):
        """
        Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
        Only loads a single frame.
        Offset is used where multiple colors are in the same sheet - for clothes etc.
        """
        FLAME_NATIVE_SIZE = 16
        #color_offset = color_offset*FLAME_NATIVE_SIZE
        color_offset=0
        return [
            arcade.load_texture(filename, y=color_offset+FLAME_NATIVE_SIZE*frame, x=FLAME_NATIVE_SIZE *
                                row, width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE),
            arcade.load_texture(filename, y=color_offset+FLAME_NATIVE_SIZE*frame, x=FLAME_NATIVE_SIZE*(
                row+1), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE),
            arcade.load_texture(filename, y=color_offset+FLAME_NATIVE_SIZE*frame, x=FLAME_NATIVE_SIZE*(
                row+2), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE),
            arcade.load_texture(filename, y=color_offset+FLAME_NATIVE_SIZE*frame, x=FLAME_NATIVE_SIZE*(
                row+3), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE)
        ]
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
                                row, width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+FLAME_NATIVE_SIZE*frame, y=FLAME_NATIVE_SIZE*(
                row+1), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+FLAME_NATIVE_SIZE*frame, y=FLAME_NATIVE_SIZE*(
                row+2), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+FLAME_NATIVE_SIZE*frame, y=FLAME_NATIVE_SIZE*(
                row+3), width=FLAME_NATIVE_SIZE, height=FLAME_NATIVE_SIZE,hit_box_algorithm="Simple")
        ]
    
    def update_damage_frames(self, max_frames, texture_dict,use_speed):
            self.cur_texture += 1
            if self.cur_texture > max_frames * use_speed:
                self.cur_texture = 0
                self.taking_damage = False
            frame = self.cur_texture // use_speed
            direction = self.character_face_direction
            if frame == max_frames:
                frame=max_frames-1
            self.texture = texture_dict[frame][direction]
            return
    
    def update_death_frames(self, max_frames, texture_dict,use_speed):
            self.cur_texture += 1
            if self.cur_texture > max_frames * use_speed:
                self.cur_texture = 0
                self.dying = False
                self.dead = True
            frame = self.cur_texture // use_speed
            direction = self.character_face_direction
            if frame == max_frames:
                frame=max_frames-1
            self.texture = texture_dict[frame]
            return
    
    def load_death_textures(self,filename, row, frame, color_offset):
        SMOKE_NATIVE_SIZE = 32
        color_offset = color_offset*ACCESSORIES_OFFSET
        return [
            arcade.load_texture(filename, x=color_offset+SMOKE_NATIVE_SIZE*frame, y=SMOKE_NATIVE_SIZE *
                                row, width=SMOKE_NATIVE_SIZE, height=SMOKE_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+SMOKE_NATIVE_SIZE*(frame+1), y=SMOKE_NATIVE_SIZE*(
                row), width=SMOKE_NATIVE_SIZE, height=SMOKE_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+SMOKE_NATIVE_SIZE*(frame+2), y=SMOKE_NATIVE_SIZE*(
                row), width=SMOKE_NATIVE_SIZE, height=SMOKE_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+SMOKE_NATIVE_SIZE*(frame+3), y=SMOKE_NATIVE_SIZE*(
                row), width=SMOKE_NATIVE_SIZE, height=SMOKE_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+SMOKE_NATIVE_SIZE*(frame+4), y=SMOKE_NATIVE_SIZE*(
                row), width=SMOKE_NATIVE_SIZE, height=SMOKE_NATIVE_SIZE,hit_box_algorithm="Simple"),
            arcade.load_texture(filename, x=color_offset+SMOKE_NATIVE_SIZE*(frame+5), y=SMOKE_NATIVE_SIZE*(
                row), width=SMOKE_NATIVE_SIZE, height=SMOKE_NATIVE_SIZE,hit_box_algorithm="Simple"),
        ]
    
    def die(self):
        self.kill()
    def reload(self):
        self.health = self.max_health
        self.center_x = self.start_x
        self.center_y = self.start_y