import arcade
from constants import *

def setup_inventory(self):
        if self.inventory_open:
            screen_center_x = self.width // 2
            screen_center_y = self.height // 2
            self.book = arcade.Sprite(filename="assets/guiassets/CustomAssets/Larger-Book-Test-2.png", scale=5,center_x=screen_center_x,center_y=screen_center_y)
            self.book.draw(pixelated=True)
            inventory_start_x = screen_center_x + 100
            inventory_start_y = screen_center_y + 120
            inventory_text_start_x = screen_center_x + 150
            inventory_text_start_y = screen_center_y + 180
            slot_sprite_list = arcade.SpriteList()
            slot_list = []
            increase_x = 0
            for index in range(5):
                slot_background = arcade.Sprite(filename="assets/guiassets/CustomAssets/InventorySlotBackground8.png",scale=4,center_x=inventory_start_x+increase_x,center_y=inventory_start_y)
               # slot_background.color = arcade.color.CELESTIAL_BLUE
                slot_sprite_list.append(slot_background)
                slot = self.inventory.slots[index]
                slot.center_x = inventory_start_x+increase_x
                slot.center_y = inventory_start_y
                slot.position_item()
                increase_x += 70
                if slot.occupied:
                    slot_sprite_list.append(slot.item)
            increase_x = 0
            for index in range(5):
                slot_background = arcade.Sprite(filename="assets/guiassets/CustomAssets/InventorySlotBackground8.png",scale=4,center_x=inventory_start_x+increase_x,center_y=inventory_start_y-70)
                slot_sprite_list.append(slot_background)
                slot = self.inventory.slots[index+5]
                slot.center_x = inventory_start_x+increase_x
                slot.center_y = inventory_start_y-70
                slot.position_item()
                increase_x += 70
                if slot.occupied:
                    slot_sprite_list.append(slot.item)
            increase_x = 0
            for index in range(5):
                slot_background = arcade.Sprite(filename="assets/guiassets/CustomAssets/InventorySlotBackground8.png",scale=4,center_x=inventory_start_x+increase_x,center_y=inventory_start_y-140)
                slot_sprite_list.append(slot_background)
                slot = self.inventory.slots[index+10]
                slot.center_x = inventory_start_x+increase_x
                slot.center_y = inventory_start_y-140
                slot.position_item()
                increase_x += 70
                if slot.occupied:
                    slot_sprite_list.append(slot.item)
            for slot in self.inventory.slots:
                if slot.selected:
                    x = slot.center_x
                    y = slot.center_y
                    self.selected_item = slot.item
                    self.inventory_cursor=arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=4,center_x=x,center_y=y)

            self.inventory_text=arcade.Text(text="Inventory",start_x=inventory_text_start_x,start_y=inventory_text_start_y,color=arcade.color.BLACK,font_name="NinjaAdventure",font_size=26)
            self.inventory_text.draw()
            self.inventory_display_box = arcade.Sprite(filename="assets/guiassets/CustomAssets/InventorySlotBackground8.png",scale=11,center_x=inventory_start_x+50,center_y=inventory_start_y-270)
            if self.selected_item:
                self.inventory_display_name=arcade.Text(text=self.selected_item.name,start_x=inventory_text_start_x+100,start_y=inventory_text_start_y-275,color=arcade.color.BLACK,font_name="NinjaAdventure",font_size=12)
            #self.inventory_text=arcade.Text(text="Inventory",start_x=inventory_text_start_x,start_y=inventory_text_start_y,color=arcade.color.BLACK,font_name="NinjaAdventure",font_size=26)
            #self.inventory_text=arcade.Text(text="Inventory",start_x=inventory_text_start_x,start_y=inventory_text_start_y,color=arcade.color.BLACK,font_name="NinjaAdventure",font_size=26)
                self.inventory_display_name.draw()
            self.inventory_display_box.draw(pixelated=True)
            slot_sprite_list.draw(pixelated=True)
            self.inventory_cursor.draw(pixelated=True)