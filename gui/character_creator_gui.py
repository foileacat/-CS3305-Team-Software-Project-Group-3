import arcade
from constants import *

def setup_character_creator_gui(self):
        """
        Future Code for the possible character Creator
        """
        self.gui_character_creator_manager = arcade.gui.UIManager()
        self.gui_character_creator_manager.enable()
        texture = arcade.load_texture(
            "assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png")
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Character Customiser",
                                              text_color=arcade.csscolor.WHITE,
                                              width=450,
                                              height=40,
                                              font_size=20,
                                              font_name="NinjaAdventure")
        self.background = arcade.gui.UITexturePane(
            child=ui_text_label, tex=texture)
        self.v_box.add(ui_text_label.with_space_around(bottom=20))

        text = "Balh"
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=450,
                                              height=60,
                                              font_size=12,
                                              font_name="Arial",
                                              text_color=arcade.csscolor.BLACK)
        blah = arcade.gui.UIWidget(children=[ui_text_label])
        blah.with_background(texture=texture)

        horse = ui_text_label.with_background(
            texture=texture, bottom=20, top=20, left=20, right=20)
        self.v_box.add(horse.with_space_around(bottom=0))
        # HAIR#####################
        # Create a UIFlatButton
        ui_flatbutton_hair = arcade.gui.UIFlatButton(text="Hair", width=200)
        self.v_box.add(ui_flatbutton_hair.with_space_around(bottom=20))

        # Handle Clicks
        @ui_flatbutton_hair.event("on_click")
        def on_click_flatbutton(event):
            self.player_sprite.hair.change_style()
        # Create a UITextureButton

        texture = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button_hair = arcade.gui.UITextureButton(texture=texture)
        self.v_box.add(ui_texture_button_hair.with_space_around(bottom=20))
        # Handle Clicks

        @ui_texture_button_hair.event("on_click")
        def on_click_texture_button(event):
            self.player_sprite.hair.change_color()

        # shirt#######################

        ui_flatbutton_clothes = arcade.gui.UIFlatButton(text="Top", width=200)
        self.v_box.add(ui_flatbutton_clothes.with_space_around(bottom=20))

        # Handle Clicks
        @ui_flatbutton_clothes.event("on_click")
        def on_click_flatbutton(event):
            self.player_sprite.shirt.change_style()
        # Create a UITextureButton

        texture = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button_clothes = arcade.gui.UITextureButton(texture=texture)
        self.v_box.add(ui_texture_button_clothes.with_space_around(bottom=20))
        # Handle Clicks

        @ui_texture_button_clothes.event("on_click")
        def on_click_texture_button(event):
            self.player_sprite.shirt.change_color()

        # TBOTTOM######################

        ui_flatbutton_bottoms = arcade.gui.UIFlatButton(
            text="Bottoms", width=200)
        self.v_box.add(ui_flatbutton_bottoms.with_space_around(bottom=20))

        # Handle Clicks
        @ui_flatbutton_bottoms.event("on_click")
        def on_click_flatbutton(event):
            self.player_sprite.bottoms.change_style()
        # Create a UITextureButton

        texture = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button_bottoms = arcade.gui.UITextureButton(texture=texture)
        self.v_box.add(ui_texture_button_bottoms.with_space_around(bottom=20))
        # Handle Clicks

        @ui_texture_button_bottoms.event("on_click")
        def on_click_texture_button(event):
            self.player_sprite.bottoms.change_color()

        # TFULL######################

        ui_flatbutton_fullbody = arcade.gui.UIFlatButton(
            text="Full Body", width=200)
        self.v_box.add(ui_flatbutton_fullbody.with_space_around(bottom=20))

        # Handle Clicks
        @ui_flatbutton_fullbody.event("on_click")
        def on_click_flatbutton(event):
            self.player_sprite.full_body.change_style()
        # Create a UITextureButton

        texture = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button_fullbody = arcade.gui.UITextureButton(
            texture=texture)
        self.v_box.add(ui_texture_button_fullbody.with_space_around(bottom=20))
        # Handle Clicks

        @ui_texture_button_fullbody.event("on_click")
        def on_click_texture_button(event):
            self.player_sprite.full_body.change_color()

        texture = arcade.load_texture(
            ":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button_shoes = arcade.gui.UITextureButton(texture=texture)
        self.v_box.add(ui_texture_button_shoes.with_space_around(bottom=20))
        # Handle Clicks

        @ui_texture_button_shoes.event("on_click")
        def on_click_texture_button(event):
            self.player_sprite.shoes.change_color()

        texture = arcade.load_texture(
            "assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png")
        # Create a widget to hold the v_box widget, that will center the buttons
        self.gui_character_creator_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box.with_background(texture=texture, bottom=20, top=20, left=20, right=20))
        )