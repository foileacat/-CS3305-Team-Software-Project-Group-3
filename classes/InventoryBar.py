import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from constants import *

INVENTORY_BAR_SIZE = 8
INVENTORY_BAR_WIDTH = 504
INVENTORY_BAR_HEIGHT = 56
INVENTORY_BAR_HORIZONTAL_PADDING = 20
INVENTORY_BAR_X = 500
INVENTORY_BAR_Y = 100
INVENTORY_SLOT_SIZE = (INVENTORY_BAR_WIDTH - INVENTORY_BAR_HORIZONTAL_PADDING ) // INVENTORY_BAR_SIZE
INVENTORY_SLOT_SPRITE_SIZE = 35
INVENTORY_BAR_CURSOR_SIZE = INVENTORY_SLOT_SIZE * 5/6
INVENTORY_BAR_SPRITE_SCALING = 4

class InventoryBar():
    def __init__(self):
        self.sprite = arcade.Sprite(filename=INVENTORY_BAR_ASSET,
                        scale=SPRITE_SCALING,
                        center_x=INVENTORY_BAR_X,
                        center_y=INVENTORY_BAR_Y)
        self.width = INVENTORY_BAR_WIDTH
        self.height = INVENTORY_BAR_HEIGHT
        self.sprite.width = self.width
        self.sprite.height = self.height
        self.slot0 = InventorySlot(selected=True)
        self.slot1 = InventorySlot()
        self.slot2 = InventorySlot()
        self.slot3 = InventorySlot()
        self.slot4 = InventorySlot()
        self.slot5 = InventorySlot()
        self.slot6 = InventorySlot()
        self.slot7 = InventorySlot()

        self.selected_slot=0
        self.slots = [self.slot0,self.slot1,self.slot2,self.slot3,self.slot4,self.slot5,self.slot6,self.slot7]
        self.slot_list = arcade.SpriteList()
        
        self.cursor = arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=INVENTORY_BAR_SPRITE_SCALING)
        self.cursor.width= INVENTORY_BAR_CURSOR_SIZE
        self.cursor.height= INVENTORY_BAR_CURSOR_SIZE
        self.initialise_slots()
        self.update_cursor()
        self.slot_list.append(self.cursor)

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
            slot.center_x = INVENTORY_BAR_X - inventory_bar_center + slot_center + slot_position
            slot.center_y = INVENTORY_BAR_Y
            slot.width = INVENTORY_SLOT_SPRITE_SIZE
            slot.height = INVENTORY_SLOT_SPRITE_SIZE
            slot.insert_item(Item(id=1,filename=EXAMPLE_EGG_SPRITE_LINK))
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
    
    def draw(self, pixelated=True):
        self.sprite.draw(pixelated=pixelated)
        self.slot_list.draw(pixelated=pixelated)
        self.cursor.draw(pixelated=pixelated)