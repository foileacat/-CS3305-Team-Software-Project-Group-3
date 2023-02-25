import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from classes.Tool import Tool
from classes.Consumable import Consumable
from constants import *

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
        self.selected_slot=2

        self.slots[6].insert_item(Item(id=1,name="Egg",filename=EXAMPLE_EGG_SPRITE_LINK))
        self.slots[7].insert_item(Item(id=1,name="Book",
                                       filename="assets/guiassets/AssetPacks/Free Pack/Free Pixel Paper/Png/Sprites/1 items Pack/5.png"))
        
        self.slots[0].insert_item(Tool(name="Old Pickaxe",
                                       type="Pickaxe",
                                       id=1,
                                       filename="assets/characterassets/Character v.2/separate/pickaxe/tool/pickaxe_full.png",
                                       image_width=16,image_height=16))
        
        self.slots[1].insert_item(Tool(name="Rusty Sword",
                                       type="Sword",
                                       id=1,
                                       filename="assets/characterassets/Character v.2/separate/sword/tool/sword.png",
                                       image_x=0,image_y=112,image_width=16,image_height=16,use_speed=6))
        
        self.slots[2].insert_item(Tool(
                                       name="Holey Watering Can",
                                       type="Watering Can",
                                       id=1,
                                       filename="assets/characterassets/Character v.2/separate/water/tool/wateringcan_full_green.png",
                                       image_x=64,image_y=0,image_width=16,image_height=16,use_speed=10))
        
        self.slots[3].insert_item(Consumable(
                                       name="Tasty Noods",
                                       id=1,
                                       filename="assets/assetpacks/ninja/Items/Food/Noodle.png"))