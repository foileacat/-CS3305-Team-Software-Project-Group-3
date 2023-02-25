import arcade
import arcade.gui
from constants import *
from gui.TypewriterText import TypewriterTextWidget

def setup_inspect_gui(self):

        self.gui_inspect_manager = arcade.gui.UIManager()
        self.gui_inspect_manager.enable()

        # setup GUI for inspecting objects

        # inspect_background_UI_sprite = arcade.gui.UISpriteWidget(x=0, y=0, width=500, height=100, sprite=arcade.Sprite(
        #     filename="assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png", scale=SPRITE_SCALING))
        
        self.inspect_message_UI = TypewriterTextWidget(
            x=0, y=0,width= 350, height = 70, font_name="NinjaAdventure")
        

        self.inspect_message_UI_background = self.inspect_message_UI.with_background(texture = arcade.load_texture(
            "assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png"),top=20,left=20,right=20,bottom=20)
        
    
        self.inspect_background_UI_anchor = arcade.gui.UIAnchorWidget(
            child=self.inspect_message_UI_background, align_x=-50, align_y=-250)

        self.gui_inspect_manager.add(self.inspect_background_UI_anchor)
        
        # self.inspect_background_UI_anchor = self.inspect_background_UI_anchor.with_background(texture = arcade.load_texture(
        
        # self.inspect_background_UI_anchor = arcade.gui.UIAnchorWidget(
        #     child=self.inspect_message_UI, align_x=-50, align_y=-250)

        # self.inspect_background_UI_anchor = self.inspect_background_UI_anchor.with_background(texture = arcade.load_texture(
        #     "assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png"))

        # self.inspect_background_UI_anchor = arcade.gui.UIAnchorWidget(
        #     child=inspect_background_UI_sprite, align_x=-50, align_y=-250)

        # self.inspect_message_UI = TypewriterTextWidget(
        #     x=0, y=0,width=400, height =80, font_name="NinjaAdventure")
        
        #self.gui_inspect_manager.add(self.inspect_message_UI)

        # self.inspect_item_hint_UI = arcade.Text(
        #     "E to Inspect", 0, 0, (255, 255, 255), 15, font_name="NinjaAdventure")

        # self.inspect_item_symbol_UI = arcade.Sprite(
        #     filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3, center_x=200, center_y=200)