import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from classes.Tool import Tool
from classes.Consumable import Consumable
from constants import *
import items
class Inventory():
    def __init__(self):
        self.slots=[
            InventorySlot(id=0,selected=True),
            InventorySlot(id=1),
            InventorySlot(id=2),
            InventorySlot(id=3),
            InventorySlot(id=4),
            InventorySlot(id=6),
            InventorySlot(id=7),
            InventorySlot(id=8),
            InventorySlot(id=9),
            InventorySlot(id=10),
            InventorySlot(id=11),
            InventorySlot(id=12),
            InventorySlot(id=13),
            InventorySlot(id=14),
            InventorySlot(id=15)
        ]
        
        #self.slots[0].insert_item(items.old_pickaxe)
        
        self.slots[1].insert_item(items.rusty_sword)
        
        self.slots[2].insert_item(items.holey_watering_can)
        
        self.slots[3].insert_item(items.noodles)
        self.selected_slot=0
    def move_cursor(self,direction):
        if direction=="right":
            movement=1
        elif direction=="left":
            movement=-1
        elif direction=="up":
            movement=-5
        else:
            movement=5
        for slot in self.slots:
            slot.selected=False
        
        if direction == "up" or direction == "down":
            self.selected_slot+=movement
            if self.selected_slot<0:
                self.selected_slot= 15 + self.selected_slot
            if self.selected_slot>14:
                self.selected_slot= self.selected_slot - 15

        else:
            self.selected_slot+=movement
            if self.selected_slot<0:
                self.selected_slot=14
            if self.selected_slot>14:
                self.selected_slot=0
        self.slots[self.selected_slot].selected = True
        
    def add_to_inventory(self,item):
        if self.in_inventory(item.name):
            self.in_inventory(item.name).item.quantity+=1
            return
        inserted = False
        for slot in self.slots:
            if inserted == False:
                if slot.occupied == False:
                    slot.insert_item(item)
                    inserted = True
                    return
                
    def in_inventory(self,name):
        for slot in self.slots:
            if slot.occupied:
                    if slot.item.name == name:
                        return slot
        return False