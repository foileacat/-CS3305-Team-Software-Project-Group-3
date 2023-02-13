import arcade
import arcade.gui
from arcade.experimental.lights import Light, LightLayer
import os
import character_lists
from classes.PlayerCharacter import PlayerCharacter
from maps import *
from constants import *


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.current_room_index = 0
        self.rooms = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera_sprites = arcade.Camera(
            SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(
            SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize variables. """
        self.character_creator_open = False
        # imports game font. name of font is "NinjaAdventure"
        arcade.load_font(FONT_PATH)
        self.player_sprite = PlayerCharacter()
        self.player_sprite.set_hit_box(self.player_sprite.points)
        self.player_accessory_list = self.player_sprite.accessory_list

        self.setup_inspect_gui()
        self.setup_character_creator_gui()
        self.rooms = []
        # Create the rooms
        #room = setup_starting_room(self.player_sprite,self.player_accessory_list)
        self.rooms.append(starting_room.setup(
            self.player_sprite, self.player_accessory_list))

        room = main_room.setup(self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = cave_outside.setup(
            self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = cave_inside.setup(
            self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = dojo_outside.setup(
            self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = dojo.setup(self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = blacksmith.setup(self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = living_room.setup(
            self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = bedroom.setup(self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = kitchen.setup(self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = forest.setup(self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        room = enemy_house.setup(
            self.player_sprite, self.player_accessory_list)
        self.rooms.append(room)

        self.current_room_index = 1
        self.current_room = self.rooms[self.current_room_index]
        self.scene = self.current_room.scene

        # used for the scrolling camera
        self.view_left = 0
        self.view_bottom = 0
        # #create physics engine - adds collision
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, walls=self.current_room.wall_list)

        """Preliminary Lighting Code - For later"""
        # self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        # light = Light(736, 400, 100, (120,30,0), "soft")
        # light2 = Light(95*4, 650, 400, (80,80,100), "soft")
        # self.light_layer.add(light)
        # self.light_layer.add(light2)

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

        text = "Poo Poo Pee Pee"
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

    def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()
        # this camera is used for everything except the gui
        self.camera_sprites.use()
        """More lighting Code"""
        # with self.light_layer:
        self.scene.draw(pixelated=True)
        #self.current_room.npc.draw_hit_box()
        # self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        # returns interactable objects the player is touching - if we have any, the item has an arrow/text hint
        interactableObjects = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["interactables"])
    
        # renders inspecting popup/interactable hint if applicable
        if self.player_sprite.currently_inspecting:
            self.camera_gui.use()
            self.inspect_message_UI.text = self.inspect_text
            self.gui_inspect_manager.draw()
        elif self.character_creator_open == True:
            self.camera_gui.use()
            self.gui_character_creator_manager.draw()
        elif interactableObjects:
            interactable = interactableObjects[0]

            """
            Alternative hint is text based - currently unused but may be readded:

            self.inspect_item_hint_UI = arcade.Text(
                    "Enter to Inspect", self.player_sprite.center_x, self.player_sprite.center_y, (255, 255, 255), 15, font_name="NinjaAdventure")
            self.inspect_item_hint_UI.draw()
            """
            self.inspect_item_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                        center_x=interactable.center_x, center_y=interactable.center_y+(interactable.height//2)+20)
            if interactable.properties["on_interact"] == "room_transition":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIANRED
            elif interactable.properties["on_interact"] == "character_creator":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIGO
            self.inspect_item_symbol_UI.draw(pixelated=True)
        elif self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(
                self.player_sprite, self.scene["NPC"])
            if npcs:
                npc = npcs[0]
                self.inspect_npc_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                            center_x=npc.center_x, center_y=(npc.center_y+(npc.height//2)-20))
                self.inspect_npc_symbol_UI.color = arcade.csscolor.SEA_GREEN
                self.inspect_npc_symbol_UI.draw(pixelated=True)
            
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.player_sprite.currently_inspecting == False and self.character_creator_open == False:
            if key == UP_KEY:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == DOWN_KEY:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == LEFT_KEY:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == RIGHT_KEY:
                self.player_sprite.change_x = MOVEMENT_SPEED
        if key == INTERACT_KEY:
            self.handle_interact()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == UP_KEY or key == DOWN_KEY:
            self.player_sprite.change_y = 0
        elif key == LEFT_KEY or key == RIGHT_KEY:
            self.player_sprite.change_x = 0

    def handle_interact(self):
        """
        Runs when a player presses the interact key next to an interactable object. 
        It will run the function named in the interactable objects on_interact attribute, from the tmx file
        """
        if self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(
                self.player_sprite, self.scene["NPC"])
            for npc in npcs:
                self.handle_npc_interaction(npc)
        interactables = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["interactables"])
        for interactable in interactables:
            getattr(self, interactable.properties['on_interact'])(interactable)
        return

    def character_creator(self, interactable):
        if self.character_creator_open == True:
            self.character_creator_open = False
            return
        else:
            self.player_sprite.character_face_direction = FORWARD_FACING
            self.character_creator_open = True

    def room_transition(self, interactable):
        """
        Currently unfinished. Runs when player interacts with a transitional interactable object .
        Transitions player from one room to the next.

        """

        entrance = interactable.properties["transition_id"]
        entrance_coordinates = self.current_room.entrances[entrance]
        self.player_sprite.center_x = entrance_coordinates[0]
        self.player_sprite.center_y = entrance_coordinates[1]
        self.current_room_index = int(
            interactable.properties["destination_room"])
        self.current_room = self.rooms[self.current_room_index]

        self.scene = self.current_room.scene

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.current_room.wall_list)
        self.player_sprite.character_face_direction = int(
            interactable.properties["transition_direction"])

    def show_message(self, interactable):
        if self.player_sprite.currently_inspecting:
            self.player_sprite.currently_inspecting = False
            return
        else:
            self.player_sprite.currently_inspecting = True
            self.inspect_text = interactable.properties["inspect_text"]

    def handle_npc_interaction(self, npc):
        x_diff = self.player_sprite.center_x - npc.center_x
        y_diff = self.player_sprite.center_y - npc.center_y
        
        if x_diff < 0 and abs(x_diff) > abs(y_diff):
            self.player_sprite.character_face_direction = RIGHT_FACING
            npc.character_face_direction = LEFT_FACING
        elif x_diff > 0 and abs(x_diff) > abs(y_diff):
            self.player_sprite.character_face_direction = LEFT_FACING
            npc.character_face_direction = RIGHT_FACING
        elif y_diff > 0 and abs(x_diff) < abs(y_diff):
            self.player_sprite.character_face_direction = FORWARD_FACING
            npc.character_face_direction = BACKWARD_FACING
        elif y_diff < 0 and abs(x_diff) < abs(y_diff):
            self.player_sprite.character_face_direction = BACKWARD_FACING
            npc.character_face_direction = FORWARD_FACING       
        # if self.player_sprite.character_face_direction == 0 or self.player_sprite.character_face_direction == 2:
        #     npc.character_face_direction = self.player_sprite.character_face_direction + 1
        # else:
        #     npc.character_face_direction = self.player_sprite.character_face_direction - 1
        return

    def on_update(self, delta_time):
        """ Movement and game logic. Runs constantly when anything changes."""

        self.physics_engine.update()
        self.scene.on_update(delta_time=1/60)
        # self.player_accessory_list.update_animation(self.player_sprite)
        if self.current_room.has_npcs:
            self.scene.update_animation(delta_time, ["NPC"])
        self.scene.update_animation(delta_time, ["Animation", "Player"])
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Manages scrolling camera. Runs constantly from the on_update function
        """
        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left

        # Scroll right
        right_boundary = self.view_left + self.width - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera_sprites.move_to(position, CAMERA_SPEED)


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
