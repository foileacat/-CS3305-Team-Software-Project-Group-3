import arcade
import arcade.gui
from constants import *
from gui.TypewriterText import TypewriterTextWidget

def setup_npc_gui(self):

        self.gui_npc_manager = arcade.gui.UIManager()
        self.gui_npc_manager.enable()
        
        self.npc_message_UI = TypewriterTextWidget(
            x=0, y=0,width= 400, height = 100, font_name="NinjaAdventure")
        

        self.npc_message_UI_background = self.npc_message_UI.with_background(texture = arcade.load_texture(
            "assets/guiassets/CustomAssets/DialogBoxFaceset.png"),top=40,left=120,right=40,bottom=20)
        
        
        self.npc_background_UI_anchor = arcade.gui.UIAnchorWidget(
            child=self.npc_message_UI_background, align_x=-50, align_y=-250)

        self.gui_npc_manager.add(self.npc_background_UI_anchor)
        
