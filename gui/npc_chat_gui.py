import arcade
import arcade.gui
from constants import *
from gui.TypewriterText import TypewriterTextWidget

def setup_npc_gui(self):

        self.gui_npc_manager = arcade.gui.UIManager()
        self.gui_npc_manager.enable()

        # setup GUI for npcing objects

        # npc_background_UI_sprite = arcade.gui.UISpriteWidget(x=0, y=0, width=500, height=100, sprite=arcade.Sprite(
        #     filename="assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png", scale=SPRITE_SCALING))
        
        self.npc_message_UI = TypewriterTextWidget(
            x=0, y=0,width= 400, height = 100, font_name="NinjaAdventure")
        

        self.npc_message_UI_background = self.npc_message_UI.with_background(texture = arcade.load_texture(
            "assets/guiassets/CustomAssets/DialogBoxFaceset.png"),top=40,left=120,right=40,bottom=20)
        
        
        self.npc_background_UI_anchor = arcade.gui.UIAnchorWidget(
            child=self.npc_message_UI_background, align_x=-50, align_y=-250)

        self.gui_npc_manager.add(self.npc_background_UI_anchor)
        
        # self.npc_background_UI_anchor = self.npc_background_UI_anchor.with_background(texture = arcade.load_texture(
        
        # self.npc_background_UI_anchor = arcade.gui.UIAnchorWidget(
        #     child=self.npc_message_UI, align_x=-50, align_y=-250)

        # self.npc_background_UI_anchor = self.npc_background_UI_anchor.with_background(texture = arcade.load_texture(
        #     "assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png"))

        # self.npc_background_UI_anchor = arcade.gui.UIAnchorWidget(
        #     child=npc_background_UI_sprite, align_x=-50, align_y=-250)

        # self.npc_message_UI = TypewriterTextWidget(
        #     x=0, y=0,width=400, height =80, font_name="NinjaAdventure")
        
        #self.gui_npc_manager.add(self.npc_message_UI)

        # self.npc_item_hint_UI = arcade.Text(
        #     "E to npc", 0, 0, (255, 255, 255), 15, font_name="NinjaAdventure")

        # self.npc_item_symbol_UI = arcade.Sprite(
        #     filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3, center_x=200, center_y=200)