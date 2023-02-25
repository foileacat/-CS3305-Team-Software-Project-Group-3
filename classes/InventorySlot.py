import arcade
from constants import *

class InventorySlot():
    def __init__(self,id=0,
                selected=False,
                item=None,
                occupied=False):
        self.id=id
        self.selected=selected
        self.item=item
        self.occupied=occupied
        self.width=20
        self.height=20
        self.center_x=0
        self.center_y=0

    def insert_item(self,item):
        if self.occupied:
            print("occupied!")
            return
        self.item=item
        self.occupied=True
        self.item.center_x = self.center_x
        self.item.center_y = self.center_y
        self.item.width=self.width
        self.item.height=self.height
    
    def position_item(self):
        self.item.center_x = self.center_x
        self.item.center_y = self.center_y
        self.item.width=self.width
        self.item.height=self.height
        
    def remove_item(self):
        self.occupied = False
        self.item = None