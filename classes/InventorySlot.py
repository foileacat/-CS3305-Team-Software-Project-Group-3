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
        self.width=45
        self.height=45
        self.center_x=0
        self.center_y=0
        self.number_text = False

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
        if self.occupied:
            self.item.center_x = self.center_x
            self.item.center_y = self.center_y
            self.item.width=self.width
            self.item.height=self.height
            if self.item.quantity > 1:
                self.number_text =arcade.Text(text=str(self.item.quantity),
                                     start_x=self.center_x-15,
                                     start_y=self.center_y-15,
                                     color=(255, 255, 255), 
                                     font_size=25,
                                     font_name="NinjaAdventure")
            else:
                self.number_text = False
        return
            
    def remove_item(self):
        self.occupied = False
        self.item.kill()
        self.item = None
        self.number_text = False