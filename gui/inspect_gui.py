import arcade
from constants import *

def setup_inspect_gui(self):

        self.gui_inspect_manager = arcade.gui.UIManager()
        self.gui_inspect_manager.enable()

        # setup GUI for inspecting objects

        inspect_background_UI_sprite = arcade.gui.UISpriteWidget(x=0, y=0, width=500, height=100, sprite=arcade.Sprite(
            filename="assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png", scale=SPRITE_SCALING))

        self.inspect_background_UI_anchor = arcade.gui.UIAnchorWidget(
            child=inspect_background_UI_sprite, align_x=-50, align_y=-250)

        self.inspect_message_UI = arcade.gui.UITextArea(
            x=350, y=130, text_color=(0, 0, 0), text="", font_name="NinjaAdventure")

        self.gui_inspect_manager.add(self.inspect_background_UI_anchor)
        self.gui_inspect_manager.add(self.inspect_message_UI)

        self.inspect_item_hint_UI = arcade.Text(
            "E to Inspect", 0, 0, (255, 255, 255), 15, font_name="NinjaAdventure")

        self.inspect_item_symbol_UI = arcade.Sprite(
            filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3, center_x=200, center_y=200)