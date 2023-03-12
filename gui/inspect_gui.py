import arcade
import arcade.gui
from constants import *
from gui.TypewriterText import TypewriterTextWidget

def setup_inspect_gui(self):

        self.gui_inspect_manager = arcade.gui.UIManager()
        self.gui_inspect_manager.enable()

        self.inspect_message_UI = TypewriterTextWidget(
            x=0, y=0,width= 400, height = 50, font_name="NinjaAdventure")
        

        self.inspect_message_UI_background = self.inspect_message_UI.with_background(texture = arcade.load_texture(
            "assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png"),top=20,left=20,right=20,bottom=20)
        
    
        self.inspect_background_UI_anchor = arcade.gui.UIAnchorWidget(
            child=self.inspect_message_UI_background, align_x=-50, align_y=-250)

        self.gui_inspect_manager.add(self.inspect_background_UI_anchor)
        
       