import arcade
from constants import *

class InventorySlot():
    def __init__(self,
                selected=False,
                item=None,
                occupied=False):
        self.selected=selected
        self.item=item
        self.occupied=occupied
        self.width=0
        self.height=0
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