import arcade
import os
import character_lists
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
    Load a texture pair, with the second being a mirror image.
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
    def __init__(self, path, color_offset):
        super().__init__()
        self.file_path = path
        self.face_direction = RIGHT_FACING
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        self.points = [[6, -16], [6, 4], [6, 4], [6, -16]]
        self.color_offset = color_offset
        # main_path = ":resources:images/animated_characters/male_person/malePerson"
        # main_path = ":resources:images/animated_characters/male_adventurer/maleAdventurer"
        # main_path = ":resources:images/animated_characters/zombie/zombie"
        # main_path = ":resources:images/animated_characters/robot/robot"

        # Load textures for idle standing
        self.idle_texture_list = load_texture_list(
            self.file_path, 0, 0, self.color_offset)
        # Load textures for walking
        self.walk_textures = []
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
    def __init__(self):

        # Set up parent class
        super().__init__()
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0

        self.scale = CHARACTER_SCALING
        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[8, -16], [8, -8], [-8, -8], [-8, -16]]

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3
        skintone = character_lists.skintones[2]
        hairstyle = character_lists.hairstyles[7]
        clothing = character_lists.clothing[3]

        self.accessory_list = arcade.SpriteList()
        self.hair = PlayerAccessory(hairstyle, 4)
        self.clothes = PlayerAccessory(clothing, 2)
        self.accessory_list.append(self.clothes)
        self.accessory_list.append(self.hair)
        

        self.idle_texture_list = load_texture_list(skintone, 0, 0, 0)

        self.walk_textures = []
        for frame in range(8):
            texture = load_texture_list(skintone, 0, frame, 0)
            self.walk_textures.append(texture)

        # Load textures for idle standing
        # Load textures for walking
        #self.right_walk_textures = []
        # for i in range(8):
        #     arcade.load_texture(filename)

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
    room.map_name = "assets\starting_room\starting_room.tmx"
    room.wall_list = arcade.SpriteList()
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
    room.tile_map = arcade.load_tilemap(
        room.map_name, SPRITE_SCALING, layer_options=layer_options)
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    for y in (0, room.width - SPRITE_SIZE):
        for x in range(0, room.width, SPRITE_SIZE):
            wall = arcade.Sprite("assets\worldassets\Backgrounds\Tilesets\TilesetLogic.png",
                                 image_width=16, image_height=16, image_x=16, image_y=0, scale=SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, room.width - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, room.height - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("assets\worldassets\Backgrounds\Tilesets\TilesetLogic.png",
                                     image_width=16, image_height=16, center_x=0, center_y=0, scale=SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    room.background = arcade.load_texture(
        "assets\worldassets\Backgrounds\Tilesets\TilesetLogic.png")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()
    room.width = SPRITE_SIZE * 20
    room.height = SPRITE_SIZE * 20
    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, room.height - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, room.width, SPRITE_SIZE):
            wall = arcade.Sprite("assets\worldassets\Backgrounds\Tilesets\TilesetLogic.png",
                                 image_width=16, image_height=16, center_x=0, center_y=0, scale=SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, room.width - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, room.height - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("assets\worldassets\Backgrounds\Tilesets\TilesetLogic.png",
                                     image_width=16, image_height=16, center_x=0, center_y=0, scale=SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("assets\worldassets\Backgrounds\Tilesets\TilesetLogic.png",
                         image_width=16, image_height=16, center_x=0, center_y=0, scale=SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture(
        "assets\worldassets\Backgrounds\Tilesets\TilesetLogic.png")

    return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.camera_sprites = arcade.Camera(
            DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(
            DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player_sprite = PlayerCharacter()
        self.player_sprite.set_hit_box(self.player_sprite.points)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.player_list = arcade.SpriteList()
        self.player_accessory_list = self.player_sprite.accessory_list
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0
        self.view_left = 0
        self.view_bottom = 0
        # Create a physics engine for this room
        walls_list = []
        walls_list.append(self.rooms[self.current_room].scene["walls"])
        walls_list.append(self.rooms[self.current_room].scene["furniture"])
        walls_list.append(self.rooms[self.current_room].scene["furniture 2"])
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, walls=walls_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        self.camera_sprites.use()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            self.rooms[self.current_room].width, self.rooms[self.current_room].height,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].scene.draw(pixelated=True)

        # If you have coins or monsters, then copy and modify the line
        # above for each list.
        self.player_list.draw(pixelated=True)
        self.player_accessory_list.draw(pixelated=True)
        # self.player_sprite.hair_sprite.draw(pixelated=True)

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

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == UP_KEY or key == DOWN_KEY:
            self.player_sprite.change_y = 0
        elif key == LEFT_KEY or key == RIGHT_KEY:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.player_list.update_animation()
        self.player_accessory_list.update_animation(self.player_sprite)
        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > self.rooms[self.current_room].width and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = self.rooms[self.current_room].width

        self.scroll_to_player()

    def scroll_to_player(self):
        # --- Manage Scrolling ---

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
