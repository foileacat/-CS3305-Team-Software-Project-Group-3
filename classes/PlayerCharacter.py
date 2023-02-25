import arcade
from constants import *
import character_lists
from classes.PlayerAccessory import PlayerAccessory
from classes.Character import Character
from classes.Inventory import Inventory
from classes.InventoryBar import InventoryBar
class PlayerCharacter(Character):

    """Creates our player"""

    def __init__(self):
        super().__init__()
        #initialise starting position
        self.center_x = 200
        self.center_y = 500
        # Select the desired asset file from our character_lists file
        skintone_file = character_lists.skintones[4]

        self.inventory=Inventory()
        self.inventory_bar=InventoryBar(self.inventory)
        self.using_tool=False
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

        self.watering_textures = []
        for frame in range(2):
            texture = self.load_texture_list(self.skintone_file, 37, frame, 0)
            self.watering_textures.append(texture)

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

        if self.using_tool==True:
            use_speed = self.current_item().use_speed
            if self.current_item().type == "Pickaxe":
                self.update_frames(5,self.pickaxe_textures,use_speed)
                return
            if self.current_item().type == "Sword":
                self.update_frames(4, self.sword_textures,use_speed)
                return
            if self.current_item().type == "Watering Can":
                self.update_frames(2, self.watering_textures,use_speed)
                return
            return
        else:
            if self.is_holding_item() and self.current_item().is_tool == False:
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
    
    def current_item(self):
        return self.inventory_bar.current_slot().item

    def is_holding_item(self):
        if self.inventory_bar.current_slot().occupied:
            return True
        return False
    
    def use_tool(self):
        if self.using_tool == True:
            return
        else:
            self.cur_texture = 0
            if self.current_item().is_tool == False:
                return
            self.using_tool = True

    def use_consumable(self):
        self.inventory_bar.remove_item()
        

    def update_frames(self, max_frames, texture_dict,use_speed):
            self.cur_texture += 1
            if self.cur_texture > max_frames * use_speed:
                self.cur_texture = 0
                self.using_tool = False
            frame = self.cur_texture // use_speed
            direction = self.character_face_direction
            if frame == max_frames:
                frame=max_frames-1
            self.texture = texture_dict[frame][direction]
            return
        