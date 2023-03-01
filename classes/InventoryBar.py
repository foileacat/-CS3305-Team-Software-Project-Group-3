import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from classes.Tool import Tool
from constants import *

INVENTORY_BAR_SIZE = 8
INVENTORY_BAR_SPRITE_SCALING = 5
INVENTORY_BAR_WIDTH = 126 * INVENTORY_BAR_SPRITE_SCALING
INVENTORY_BAR_HEIGHT = 14 * INVENTORY_BAR_SPRITE_SCALING
INVENTORY_BAR_HORIZONTAL_PADDING = 20
INVENTORY_BAR_X = 500
INVENTORY_BAR_Y = 100
INVENTORY_SLOT_SIZE = (INVENTORY_BAR_WIDTH - INVENTORY_BAR_HORIZONTAL_PADDING ) // INVENTORY_BAR_SIZE
INVENTORY_SLOT_SPRITE_SIZE = 9 * INVENTORY_BAR_SPRITE_SCALING
INVENTORY_BAR_CURSOR_SIZE = INVENTORY_SLOT_SIZE * 5/6


class InventoryBar():
    def __init__(self, inventory):
        self.inventory = inventory
        self.sprite = arcade.Sprite(
                        filename=INVENTORY_BAR_ASSET,
                        scale=SPRITE_SCALING,
                        center_x=INVENTORY_BAR_X,
                        center_y=INVENTORY_BAR_Y)
        self.x = INVENTORY_BAR_X
        self.y = INVENTORY_BAR_Y
        self.width = INVENTORY_BAR_WIDTH
        self.height = INVENTORY_BAR_HEIGHT
        self.sprite.width = self.width
        self.sprite.height = self.height
        self.selected_slot=0
        self.slots = inventory.slots[:INVENTORY_BAR_SIZE]
        self.slot_list = arcade.SpriteList()
        
        self.cursor = arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=INVENTORY_BAR_SPRITE_SCALING)
        self.cursor.width= INVENTORY_BAR_CURSOR_SIZE
        self.cursor.height= INVENTORY_BAR_CURSOR_SIZE
        self.initialise_slots()
        self.update_cursor()
        self.slot_list.append(self.cursor)
        self.name_text =arcade.Text( text="",
                                     start_x=200,
                                     start_y=200,
                                     color=(255, 255, 255), 
                                     font_size=12,
                                     font_name="NinjaAdventure")
        self.time_since_last_change=1000

    def update_cursor(self):
        for slot in self.slots:
            if slot.selected:
                self.cursor.center_x=slot.center_x
                self.cursor.center_y=slot.center_y
           
    def initialise_slots(self): 
        slot_counter = 0
        inventory_bar_center = ((INVENTORY_BAR_WIDTH - INVENTORY_BAR_HORIZONTAL_PADDING )// 2 )
        slot_center = (INVENTORY_SLOT_SIZE // 2)
        for slot in self.slots:
            slot_position = slot_counter * INVENTORY_SLOT_SIZE
            slot.center_x = self.x - inventory_bar_center + slot_center + slot_position
            slot.center_y = self.y
            slot.width = INVENTORY_SLOT_SPRITE_SIZE
            slot.height = INVENTORY_SLOT_SPRITE_SIZE
            if slot.occupied:
                slot.position_item()
                self.slot_list.append(sprite=slot.item)
            slot_counter+=1
       
    def move_cursor(self,direction):
        if direction=="right":
            movement=1
        else:
            movement=-1
        for slot in self.slots:
            slot.selected=False
        self.selected_slot+=movement
        if self.selected_slot<0:
            self.selected_slot=7
        if self.selected_slot>7:
            self.selected_slot=0

        self.slots[self.selected_slot].selected = True
        self.update_cursor()
        self.time_since_last_change=0

    def select_slot(self,key):
        key-=49 # converting key to list index - arcade keys are numbers, 0 is 48, 1 is 49 etc.
        for slot in self.slots:
            slot.selected=False
        self.selected_slot=key
        self.slots[self.selected_slot].selected = True
        self.update_cursor()
        self.time_since_last_change=0
    
    def draw(self, pixelated=True):
        self.time_since_last_change+=1
        self.sprite.draw(pixelated=pixelated)
        self.slot_list.draw(pixelated=pixelated)
        self.cursor.draw(pixelated=pixelated)

        if self.time_since_last_change <=100 and self.current_slot().occupied:
            if self.current_slot().item.is_consumable:
                self.name_text.color=arcade.color.RADICAL_RED
            elif self.current_slot().item.is_tool:
                self.name_text.color=arcade.color.AERO_BLUE
            else:
                self.name_text.color=arcade.color.WHITE
            self.name_text.value=self.current_slot().item.name
            self.name_text.y=self.current_slot().center_y+40
            self.name_text.x=self.current_slot().center_x-(INVENTORY_SLOT_SIZE//2 +5)
            self.name_text.draw()

    def current_slot(self):
        return self.slots[self.selected_slot]
    
    def resize(self,screen):
        self.slot_list.clear()
        self.x=screen.width//2
        self.y= screen.height//8
        self.sprite.center_x=screen.width//2
        self.sprite.center_y=screen.height//8
        self.initialise_slots()
        self.update_cursor()

    def remove_item(self):
        self.current_slot().occupied=False
        self.current_slot().item.kill()
        self.current_slot().item = None