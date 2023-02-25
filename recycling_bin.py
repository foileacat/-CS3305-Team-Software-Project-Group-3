# code that might be used later, is half written, or might be used for reference
#text based hint
import arcade

""" self.inspect_item_hint_UI = arcade.Text(
                    "Enter to Inspect", self.player_sprite.center_x, self.player_sprite.center_y, (255, 255, 255), 15, font_name="NinjaAdventure")
            self.inspect_item_hint_UI.draw()"""

def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()
        # this camera is used for everything except the gui
        self.camera_sprites.use()

        """More lighting Code"""
        # with self.light_layer:
        self.scene.draw(pixelated=True)
        # self.current_room.npc.draw_hit_box()
        # self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        # returns interactable objects the player is touching - if we have any, the item has an arrow/text hint
        interactableObjects = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["interactables"])
        #arcade.gui.UITextArea.w
        # renders inspecting popup/interactable hint if applicable

        if self.player_sprite.currently_inspecting:
            self.camera_gui.use()
            "text formatting"
            #self.inspect_message_UI.text=self.inspect_text
            #self.inspect_message_UI.fit_content()
            self.inspect_message_UI.display_text(self.inspect_text)
            self.gui_inspect_manager.draw()

        elif self.player_sprite.currently_npc_interacting:
            self.camera_gui.use()
            "text formatting"
            #self.inspect_message_UI.text=self.inspect_text
            #self.inspect_message_UI.fit_content()
            self.inspect_message_UI.display_text(self.conversation_list[self.count])
            self.gui_inspect_manager.draw()

        elif self.character_creator_open == True:
            self.camera_gui.use()
            self.gui_character_creator_manager.draw()

        elif interactableObjects:
            interactable = interactableObjects[0]
            self.inspect_item_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                        center_x=interactable.center_x, center_y=interactable.center_y+(interactable.height//2)+20)
            if interactable.properties["on_interact"] == "room_transition":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIANRED
            elif interactable.properties["on_interact"] == "character_creator":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIGO
            self.inspect_item_symbol_UI.draw(pixelated=True)
            self.camera_gui.use()
            self.inventory_bar.draw()

        elif self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(
                self.player_sprite, self.scene["NPC"])
            
            if npcs:
                npc = npcs[0]
                self.inspect_npc_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                           center_x=npc.center_x, center_y=(npc.center_y+(npc.height//2)-20))
                self.inspect_npc_symbol_UI.color = arcade.csscolor.SEA_GREEN
                self.inspect_npc_symbol_UI.draw(pixelated=True)
            self.camera_gui.use()
            self.inventory_bar.draw()

        else:
            self.camera_gui.use()
            self.inventory_bar.draw()

        if self.draw_performance:
            self.draw_performance_graph()