import arcade
import arcade.gui
import os
import character_lists

FONT_PATH = "assets/assetpacks/ninja/HUD/Font/NormalFont.ttf"
SPRITE_SCALING = 4 
CHARACTER_SCALING = 4
SPRITE_NATIVE_SIZE = 16
CHARACTER_NATIVE_SIZE = 32
ACCESSORIES_NATIVE_SIZE = 32
ACCESSORIES_OFFSET = 32*8
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
VIEWPORT_MARGIN = 200
CAMERA_SPEED = 0.1
DEFAULT_SCREEN_WIDTH = 1200
DEFAULT_SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Fake Zelda"

# setting arrow key controls
UP_KEY = arcade.key.W
DOWN_KEY = arcade.key.S
LEFT_KEY = arcade.key.A
RIGHT_KEY = arcade.key.D
INTERACT_KEY = arcade.key.ENTER
# How fast to move, and how fast to run the animation
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5

# Constants used to track if the player is facing left or right
RIGHT_FACING = 2
LEFT_FACING = 3
UP_FACING = 0
DOWN_FACING = 1


class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.width = SPRITE_SIZE * 10
        self.height = SPRITE_SIZE * 10
        self.background = None


def load_texture_list(filename, row, frame, offset):
    """
    Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
    Only loads a single frame.
    Offset is used where multiple colors are in the same sheet - for clothes etc.
    """
    offset = offset*ACCESSORIES_OFFSET
    return [
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                            row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+1), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+2), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+3), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE)
    ]


class PlayerAccessory(arcade.Sprite):
    """
    Creates Accesory for character - clothes,hair,eyes etc. 
    These are added to the players accesory sprite list 
    """

    def __init__(self, path, color_offset):
        super().__init__()
        self.file_path = path
        self.face_direction = RIGHT_FACING
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        self.points = [[6, -16], [6, 4], [6, 4], [6, -16]]  # creates hitbox
        self.color_offset = color_offset  # the offset to choose the color of the accesory

        # Load textures for idle standing
        self.idle_texture_list = load_texture_list(
            self.file_path, 0, 0, self.color_offset)
        # Load textures for walking
        self.walk_textures = []
        # loads each frame
        for frame in range(8):
            texture = load_texture_list(
                self.file_path, 0, frame, self.color_offset)
            self.walk_textures.append(texture)

    def update_animation(self, player_sprite, delta_time: float = 1 / 60):
        self.face_direction = player_sprite.character_face_direction
        self.center_x = player_sprite.center_x
        self.center_y = player_sprite.center_y
        # Walking animation
        if player_sprite.change_x == 0 and player_sprite.change_y == 0:
            self.texture = self.idle_texture_list[self.face_direction]
            return
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.face_direction
        self.texture = self.walk_textures[frame][direction]


class PlayerCharacter(arcade.Sprite):

    """Creates our player"""

    def __init__(self):
        super().__init__()
        #initialise starting position
        self.center_x = 200
        self.center_y = 200
        self.character_face_direction = RIGHT_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        # creates hitbox
        self.points = [[8, -16], [8, -8], [-8, -8], [-8, -16]]

        # Select the desired asset file from our character_lists file
        skintone_file = character_lists.skintones[2]
        hairstyle_file = character_lists.hairstyles[7]
        clothing_file = character_lists.clothing[3]
        # initialise accessory list and add PlayerAccesories to it
        self.accessory_list = arcade.SpriteList()
        self.hair = PlayerAccessory(hairstyle_file, 4)
        self.clothes = PlayerAccessory(clothing_file, 2)
        self.accessory_list.append(self.clothes)
        self.accessory_list.append(self.hair)
        # load textures for standing still and for walking animation
        self.idle_texture_list = load_texture_list(skintone_file, 0, 0, 0)

        self.walk_textures = []
        for frame in range(8):
            texture = load_texture_list(skintone_file, 0, frame, 0)
            self.walk_textures.append(texture)

        self.currently_inspecting = False
    # runs constantly, animates character moving

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.change_y == 0:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.change_y == 0:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.change_x == 0:
            self.character_face_direction = UP_FACING
        elif self.change_y > 0 and self.change_x == 0:
            self.character_face_direction = DOWN_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_list[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]


def setup_room_1():
    room = Room()
    room.map_file = "assets/maps/dojo.tmx"
    room.wall_list = arcade.SpriteList()
    # all layers that are spatially hashed are "solid" - aka we can give them collision
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "furniture": {
            "use_spatial_hash": True,
        },
        "furniture 2": {
            "use_spatial_hash": True,
        },
    }

    # create tilemap, and then a scene from that tilemap. the scene is what we use.

    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    # the rooms wall list is used for player collision.
    room.wall_list = []
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["furniture"])
    room.wall_list.append(room.scene["furniture 2"])

    return room


def setup_room_2():
    room = Room()
    room.map_file = "assets/maps/main_room.tmx"
    room.wall_list = arcade.SpriteList()
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
    }
    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    room.wall_list = []
    room.wall_list.append(room.scene["walls"])

    return room


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

        self.current_room = 0
        self.rooms = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera_sprites = arcade.Camera(
            DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(
            DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize variables. """

        arcade.load_font(FONT_PATH) #imports game font. name of font is "Ninja Adventure"

        self.player_sprite = PlayerCharacter()
        self.player_sprite.set_hit_box(self.player_sprite.points)
        self.player_accessory_list = self.player_sprite.accessory_list
        self.gui_inspect_manager = arcade.gui.UIManager()
        self.gui_inspect_manager.enable()
        #setup GUI for inspecting objects

        inspect_background_UI_sprite = arcade.gui.UISpriteWidget(x=0, y=0, width=500, height=100, sprite=arcade.Sprite(
            filename="assets/assetpacks/ninja/HUD/Dialog/DialogueBoxSimple.png", scale=SPRITE_SCALING))

        self.inspect_background_UI_anchor = arcade.gui.UIAnchorWidget(
            child=inspect_background_UI_sprite, align_x=-50, align_y=-250)

        self.inspect_message_UI = arcade.gui.UITextArea(
            x=350, y=120, text_color=(0, 0, 0), text="")

        self.gui_inspect_manager.add(self.inspect_background_UI_anchor)
        self.gui_inspect_manager.add(self.inspect_message_UI)

        self.inspect_item_hint_UI = arcade.Text(
            "E to Inspect", 0, 0, (255, 255, 255), 15, font_name="NinjaAdventure")

        self.inspect_item_symbol_UI = arcade.Sprite(
            filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3, center_x=200, center_y=200)

        # Our list of roomssdd
        self.rooms = []
        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        self.current_room = 0
        #used for the scrolling camera
        self.view_left = 0
        self.view_bottom = 0
        #create physics engine - adds collision
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, walls=self.rooms[self.current_room].wall_list)

    def on_draw(self):

        # This command has to happen before we start drawing
        self.clear()
        #this camera is used for everything except the gui
        self.camera_sprites.use()

        self.rooms[self.current_room].scene.draw(pixelated=True)
        self.player_sprite.draw(pixelated=True)
        self.player_accessory_list.draw(pixelated=True)

        #returns interactable objects the player is touching - if we have any, the item has an arrow/text hint
        interactableObjects = arcade.check_for_collision_with_list(
            self.player_sprite, self.rooms[self.current_room].scene["interactables"])

        #renders inspecting popup/interactable hint if applicable
        if self.player_sprite.currently_inspecting:
            self.camera_gui.use()
            self.inspect_message_UI.text = self.inspect_text
            self.gui_inspect_manager.draw()
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
            self.inspect_item_symbol_UI.draw(pixelated=True)
            

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == UP_KEY:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == DOWN_KEY:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == LEFT_KEY:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == RIGHT_KEY:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == INTERACT_KEY:
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
        interactables = arcade.check_for_collision_with_list(
            self.player_sprite, self.rooms[self.current_room].scene["interactables"])
        for interactable in interactables:
            getattr(self, interactable.properties['on_interact'])(interactable)
        return

    def room_transition(self,interactable):
        """
        Currently unfinished. Runs when player interacts with a transitional interactable object .
        Transitions player from one room to the next.

        """
        self.current_room = int(interactable.properties["destination_room"])
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                            self.rooms[self.current_room].wall_list)
        if interactable.properties["transition_type"] == "right":
            self.player_sprite.center_x = 0
        elif interactable.properties["transition_type"] == "left":
            self.player_sprite.center_x = self.rooms[self.current_room].width
        elif interactable.properties["transition_type"] == "up":
            self.player_sprite.center_y = 0
        elif interactable.properties["transition_type"] == "down":
            self.player_sprite.center_y = self.rooms[self.current_room].height

    def show_message(self, interactable):
        if self.player_sprite.currently_inspecting:
            self.player_sprite.currently_inspecting = False
            return
        else:
            self.player_sprite.currently_inspecting = True
            self.inspect_text = interactable.properties["item_id"]

    def on_update(self, delta_time):
        """ Movement and game logic. Runs constantly when anything changes."""

        self.physics_engine.update()
        self.player_sprite.update_animation()
        self.player_accessory_list.update_animation(self.player_sprite)

        """
        Used for room changes ---- NEEDS REPLACING WITH INTERACTABLE OBJECTS (in progress)
        Only really works for two rooms

        """

        # if self.player_sprite.center_x > self.rooms[self.current_room].width and self.current_room == 0:
        #     self.current_room = 1
        #     #adds current rooms walls to the physics engine
        #     self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
        #                                                      self.rooms[self.current_room].wall_list)
        #     self.player_sprite.center_x = 0
        # elif self.player_sprite.center_x < 0 and self.current_room == 1:
        #     self.current_room = 0
        #     self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
        #                                                      self.rooms[self.current_room].wall_list)
        #     self.player_sprite.center_x = self.rooms[self.current_room].width

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
