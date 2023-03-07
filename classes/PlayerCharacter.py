import arcade
from constants import *
import character_lists
from classes.PlayerAccessory import PlayerAccessory
from classes.Character import Character
from classes.Inventory import Inventory
from classes.InventoryBar import InventoryBar
from classes.Item import Item
import items
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
        # self.sword = PlayerAccessory(["assets/characterassets/Character v.2/separate/sword/tool/sword.png"],0,0)
        self.full_body.alpha = 0
        self.health = 10
        self.knockback = 3
        self.populate_accessory_list()
        self.currently_inspecting = False
        self.currently_npc_interacting = False
        self.taking_damage = False
        self.dead = False
        self.mining = False
        
        
    def load_textures(self):
        self.idle_texture_list = self.load_texture_list(self.skintone_file, 0, 0, 0)
        self.idle_carry_texture_list = self.load_texture_list(self.skintone_file, 12, 0, 0)
        
        self.dying_textures = self.load_horizontal_texture_pair(self.skintone_file, 28, 0, 0)

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

        self.damage_textures = []
        for frame in range(3):
            texture = self.load_texture_list(self.skintone_file, 24, 0, 0)
            self.damage_textures.append(texture)
        
        

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
        if self.dead:
            return
        if self.dying:
            self.update_dying_frames(2,self.dying_textures,40)
            return
        
        if self.taking_damage:
            self.update_damage_frames(3,self.damage_textures,10)
            return
        
        if self.using_tool==True:
            use_speed = self.current_item().use_speed
            if self.current_item().type == "Pickaxe":
                self.update_tool_frames(5,self.pickaxe_textures,use_speed)
                return
            if self.current_item().type == "Sword":
                self.update_tool_frames(4, self.sword_textures,use_speed)
                return
            if self.current_item().type == "Watering Can":
                self.update_tool_frames(2, self.watering_textures,use_speed)
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
    
    def take_damage(self,enemy):
        if self.dying or self.dead or enemy.dying:
            return
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
      
        self.cur_texture = 0
        self.taking_damage=True
        self.health -= enemy.damage
        if self.health < 0:
            self.health = 0
            self.dying = True
            self.cur_texture = 0
        return
    
    def use_tool(self):
        if self.using_tool == True:
            return
        else:
            self.cur_texture = 0
            if self.current_item().is_tool == False:
                return
            self.using_tool = True
            self.calculate_tool_stats()

    def use_consumable(self):
        self.inventory_bar.remove_item()
    
    def calculate_tool_stats(self):
        if self.current_item().is_tool == False:
                return
        else:
            self.knockback = self.current_item().knockback
            self.damage =  self.current_item().damage


    def update_tool_frames(self, max_frames, texture_dict,use_speed):
            self.cur_texture += 1
            if self.cur_texture > max_frames * use_speed:
                self.cur_texture = 0
                self.using_tool = False
                self.mining = False
                self.set_hit_box(self.points)
                return
            frame = self.cur_texture // use_speed
            direction = self.character_face_direction
            if frame == max_frames:
                frame=max_frames-1
            self.texture = texture_dict[frame][direction]
            self.set_hit_box(self.texture.hit_box_points)
            return
    
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
    
    def update_dying_frames(self, max_frames, texture_dict,use_speed):
            self.cur_texture += 1
            if self.cur_texture > max_frames * use_speed:
                self.dying = False
                self.die()
            frame = self.cur_texture // use_speed
            if frame == max_frames:
                frame=max_frames-1
            self.texture = texture_dict[frame]
            return
    
    def die(self):
        print("ok")
        self.dying = False
        self.dead = True

    def mine(self,pickaxe_interactable):
        if self.mining:
            return
        else:
            if self.current_item().type == "Pickaxe":
                self.mining = True
                pickaxe_interactable.properties["pickaxe_condition"] -= 1 
                print(pickaxe_interactable.properties["pickaxe_condition"])
                asset="assets/customassets/"+pickaxe_interactable.properties['item_id']+".png"
                ore =Item(id=1,name=pickaxe_interactable.properties["name"],filename=asset,image_width=16,image_height=16)
                ore.description = "This is the emerald ore the blacksmith needs! I should bring this to him ASAP"
                self.add_to_inventory(ore)
            else:
                return

    def has_item(self,item):
        if self.inventory.in_inventory(item):
            return True
        else:
            return False
        
    def add_to_inventory(self,item):
        self.inventory.add_to_inventory(item)
        self.inventory_bar.update_on_add()

    def respawn(self,game):
        self.health = 10
        self.dying = False
        self.dead = False
        self.cur_texture = 0
        self.center_x = game.current_room.respawn_x
        self.center_y = game.current_room.respawn_y
        