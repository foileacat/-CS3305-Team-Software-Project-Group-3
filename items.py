import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from classes.Tool import Tool
from classes.Consumable import Consumable
from constants import *

egg = Item(id=1,name="Egg",filename=EXAMPLE_EGG_SPRITE_LINK)
book =Item(id=1,name="Book",filename="assets/guiassets/AssetPacks/Free Pack/Free Pixel Paper/Png/Sprites/1 items Pack/5.png")
white_flower_quest = Item(id="white_flower_quest",name="White Flower",filename="assets/customassets/white_flower.png")
red_flower_quest = Item(id="red_flower_quest",name="Red Flower",filename="assets/customassets/red_flower.png")
yellow_flower_quest = Item(id="yellow_flower_quest",name="Yellow Flower",filename="assets/customassets/yellow_flower.png")
old_pickaxe = Tool(name="Old Pickaxe",
                                       type="Pickaxe",
                                       id=1,
                                       knockback=5,
                                       filename="assets/characterassets/Character v.2/separate/pickaxe/tool/pickaxe_full.png",
                                       image_width=16,image_height=16)
old_pickaxe.description = "This pickaxe is heavy, I think it used to belong to one of the old miners."
rusty_sword=Tool(name="Rusty Sword",
                                       type="Sword",
                                       id=1,
                                       filename="assets/characterassets/Character v.2/separate/sword/tool/sword.png",
                                       image_x=0,image_y=112,image_width=16,image_height=16,use_speed=6)
rusty_sword.description = "This thing may be rusty but it's definitely still sharp!"
holey_watering_can=Tool(name="Holey Watering Can",
                        type="Watering Can",
                        id=1,
                        filename="assets/characterassets/Character v.2/separate/water/tool/wateringcan_full_green.png",
                        image_x=64,image_y=0,image_width=16,image_height=16,use_speed=10)
holey_watering_can.description = "I think this watering can has seen better days... at least it still holds water."

noodles = Consumable(name="Tasty Noods", id=1, filename="assets/assetpacks/ninja/Items/Food/Noodle.png")
noodles.description = "These smell so good... and surprisingly healthy!"

items = [egg,book,white_flower_quest,red_flower_quest,yellow_flower_quest,old_pickaxe,rusty_sword,holey_watering_can,noodles]

def get_item(name):
    for item in items:
        if name == item.id:
            return item
    return False