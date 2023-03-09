import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from classes.Tool import Tool
from classes.Consumable import Consumable
from constants import *

egg = Item(id=1,name="Egg",filename=EXAMPLE_EGG_SPRITE_LINK)
book =Item(id=1,name="Books",filename="assets/guiassets/AssetPacks/Free Pack/Free Pixel Paper/Png/Sprites/1 items Pack/5.png")
book.quantity = 25
book.description = "Jeez, these are not getting any lighter the longer I carry them"

plants =Item(id=1,name="Seeds",filename="assets/assetpacks/ninja/Items/Food/SeedLargeWhite.png")
plants.quantity = 2
plants.description = "I can't believe these are going to grow to a whole plant. From something so tiny!!"

sack =Item(id=1,name="Sacks",filename="assets/customassets/sack.png" )
sack.quantity = 2
sack.description = "What is in these? They weigh as much as me!"

shirt =Item(id=1,name="Wet Shirt",filename="assets/guiassets/AssetPacks/Free Pack/Free Pixel Paper/Png/Sprites/2 Equipments Pack/33.png")
shirt.description = "This is really wet. I wish tumble driers existed in this universe."

berries =Item(id=1,name="Berries",filename="assets/assetpacks/ninja/Items/Food/SeedBig3.png" )
berries.description = "These look so good, maybe he won't notice if I sneak a few.."
berries.quantity = 5

fish =Item(id=1,name="Fish",filename="assets/assetpacks/ninja/Items/Food/Fish.png" )
fish.description = "These smell... like fish. I think that's bad?"
fish.quantity = 2

flowers =Item(id=1,name="Flowers",filename="assets/customassets/white_flower.png" )
flowers.quantity = 7
flowers.description = "These are so pretty! I feel like a real gardener."

pickaxe_key =Item(id=1,name="Pickaxe Key",filename="assets/assetpacks/ninja/Items/Treasure/SilverKey.png" )
pickaxe_key.description = "Fancy Key! I should open that chest outside with it"

gem_key =Item(id=1,name="Gem Key",filename="assets/assetpacks/ninja/Items/Treasure/GoldKey.png" )
gem_key.description = "Shiny! I can finally collect the gem!"

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
        if name == item.name:
            return item
    return False