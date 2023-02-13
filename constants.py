import arcade

FONT_PATH = "assets/assetpacks/ninja/HUD/Font/NormalFont.ttf"
SPRITE_SCALING = 4 
CHARACTER_SCALING = 4
SPRITE_NATIVE_SIZE = 16
CHARACTER_NATIVE_SIZE = 32
ACCESSORIES_NATIVE_SIZE = 32
ACCESSORIES_OFFSET = 32*8
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
VIEWPORT_MARGIN = 200
CAMERA_SPEED = 0.2
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Fake Zelda"
AMBIENT_COLOR = (200,200,200)
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
FORWARD_FACING = 0
BACKWARD_FACING = 1
RIGHT_FACING = 2
LEFT_FACING = 3