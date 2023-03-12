import arcade
from constants import *

def draw_inventory(self):
        screen_center_x = self.width // 2
        screen_center_y = self.height // 2
        self.book = arcade.Sprite(filename="assets/guiassets/CustomAssets/Larger-Book-Test-2.png",
                                  scale=5, center_x=screen_center_x, center_y=screen_center_y)
        self.book.draw(pixelated=True)
        inventory_start_x = screen_center_x + 100
        inventory_start_y = screen_center_y + 120
        inventory_text_start_x = screen_center_x + 150
        inventory_text_start_y = screen_center_y + 180
        slot_sprite_list = arcade.SpriteList()
        increase_x = 0
        for index in range(5):
            slot_background = arcade.Sprite(filename="assets/guiassets/CustomAssets/InventorySlotBackground8.png",
                                            scale=4, center_x=inventory_start_x+increase_x, center_y=inventory_start_y)
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
            slot_background = arcade.Sprite(filename="assets/guiassets/CustomAssets/InventorySlotBackground8.png",
                                            scale=4, center_x=inventory_start_x+increase_x, center_y=inventory_start_y-70)
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
            slot_background = arcade.Sprite(filename="assets/guiassets/CustomAssets/InventorySlotBackground8.png",
                                            scale=4, center_x=inventory_start_x+increase_x, center_y=inventory_start_y-140)
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
                self.inventory_cursor = arcade.Sprite(
                    filename=INVENTORY_BAR_CURSOR_ASSET, scale=4, center_x=x, center_y=y)

        self.inventory_text = arcade.Text(text="Inventory", start_x=inventory_text_start_x,
                                          start_y=inventory_text_start_y, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=26)
        self.inventory_text.draw()
        if self.selected_item:
            self.inventory_display_name = arcade.Text(text=self.selected_item.name, start_x=inventory_start_x-20,
                                                      start_y=inventory_start_y-210, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=19)
            if self.selected_item.is_tool:
                self.selected_item.generate_stats()
                self.inventory_display_stat1 = arcade.Text(text=self.selected_item.statistic_one, start_x=inventory_start_x-20,
                                                           start_y=inventory_start_y-230, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
                self.inventory_display_stat2 = arcade.Text(text=self.selected_item.statistic_two, start_x=inventory_start_x-20,
                                                           start_y=inventory_start_y-250, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
                self.inventory_display_stat3 = arcade.Text(text=self.selected_item.statistic_three, start_x=inventory_start_x-20,
                                                           start_y=inventory_start_y-270, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
                self.inventory_display_description = arcade.Text(text=self.selected_item.description, start_x=inventory_start_x-20,
                                                                 start_y=inventory_start_y-310, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12, multiline=True, width=350)
                self.inventory_display_stat1.draw()
                self.inventory_display_stat2.draw()
                self.inventory_display_stat3.draw()
                self.inventory_display_description.draw()
            elif self.selected_item.is_consumable:
                self.selected_item.generate_stats()
                self.inventory_display_stat1 = arcade.Text(text=self.selected_item.statistic_one, start_x=inventory_start_x-20,
                                                           start_y=inventory_start_y-250, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
                self.inventory_display_description = arcade.Text(text=self.selected_item.description, start_x=inventory_start_x-20,
                                                                 start_y=inventory_start_y-280, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12, multiline=True, width=350)
                self.inventory_display_stat1.draw()
                self.inventory_display_description.draw()
            else:
                self.inventory_display_description = arcade.Text(text=self.selected_item.description, start_x=inventory_start_x-20,
                                                                 start_y=inventory_start_y-240, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12, multiline=True, width=350)
                self.inventory_display_description.draw()

            self.inventory_display_name.draw()
        self.gem_list = arcade.SpriteList()
        self.gem1 = arcade.Sprite(filename="assets/customassets/gem_1.png", scale=SPRITE_SCALING,
                                  center_x=screen_center_x - 390, center_y=screen_center_y+140)
        self.gem2 = arcade.Sprite(filename="assets/customassets/gem_2.png", scale=SPRITE_SCALING,
                                  center_x=screen_center_x - 290, center_y=screen_center_y+140)
        self.gem3 = arcade.Sprite(filename="assets/customassets/gem_3.png", scale=SPRITE_SCALING,
                                  center_x=screen_center_x - 190, center_y=screen_center_y+140)
        self.gem4 = arcade.Sprite(filename="assets/customassets/gem_4.png", scale=SPRITE_SCALING,
                                  center_x=screen_center_x - 90, center_y=screen_center_y+140)
        self.gem_text = arcade.Text(text="Gems", start_x=screen_center_x-290,
                                    start_y=screen_center_y + 180, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=26)
        if self.player_sprite.gem_1 == False:
            self.gem1.color = arcade.color.BLACK
        if self.player_sprite.gem_2 == False:
            self.gem2.color = arcade.color.BLACK
        if self.player_sprite.gem_3 == False:
            self.gem3.color = arcade.color.BLACK
        if self.player_sprite.gem_4 == False:
            self.gem4.color = arcade.color.BLACK
        self.gem_list.append(self.gem1)
        self.gem_list.append(self.gem2)
        self.gem_list.append(self.gem3)
        self.gem_list.append(self.gem4)
        slot_sprite_list.draw(pixelated=True)
        self.gem_list.draw(pixelated=True)
        self.gem_text.draw()
        for slot in self.inventory.slots:
            if slot.number_text:
                slot.number_text.draw()
        self.inventory_cursor.draw(pixelated=True)
        descriptions = []
        self.controls_text = arcade.Text(text="Controls", start_x=screen_center_x-320,
                                         start_y=screen_center_y + 60, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=26)
        self.controls1 = arcade.Text(text="Move: WASD", start_x=screen_center_x-410,
                                          start_y=screen_center_y + 30, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
        self.controls2 = arcade.Text(text="Move in Inventory: Up, Down, Left, Right", start_x=screen_center_x-410,
                                          start_y=screen_center_y + 0, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
        self.controls3 = arcade.Text(text="Select from Inventory Bar: 1-8", start_x=screen_center_x-410,
                                          start_y=screen_center_y - 30, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
        self.controls4 = arcade.Text(text="Interact: Enter", start_x=screen_center_x-410,
                                          start_y=screen_center_y - 60, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
        self.controls5 = arcade.Text(text="Use Item: C", start_x=screen_center_x-410,
                                          start_y=screen_center_y - 90, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12)
        self.controls_text.draw()
        self.controls1.draw()
        self.controls2.draw()
        self.controls3.draw()
        self.controls4.draw()
        self.controls5.draw()
        for quest in self.quests:
            if quest.active:
                for subquest in quest.steps:
                    if quest.steps[subquest].is_active() or quest.steps[subquest].is_done():
                        descriptions.append(quest.steps[subquest].description)
        self.quest_text = arcade.Text(text="Quests", start_x=screen_center_x-310,
                                      start_y=screen_center_y - 140, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=26)
        self.quest_text.draw()
        self.q_text1 = arcade.Text(text=descriptions[0], start_x=screen_center_x-410,
                                   start_y=screen_center_y - 170, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12, multiline=True, width=350)
        self.q_text1.draw()

        if len(descriptions) > 1:
            self.q_text2 = arcade.Text(text=descriptions[1], start_x=screen_center_x-410,
                                       start_y=screen_center_y - 215, color=arcade.color.BLACK, font_name="NinjaAdventure", font_size=12, multiline=True, width=350)
            self.q_text2.draw()