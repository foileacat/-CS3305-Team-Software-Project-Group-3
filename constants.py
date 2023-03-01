import arcade
#in progress
# def update_constants(screen):
#     SCREEN_WIDTH = screen.width
#     SCREEN_HEIGHT = screen.height

"Screen"
VIEWPORT_MARGIN = 200
CAMERA_SPEED = 0.2
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Fake Zelda"

"Sprite Sizing"
SPRITE_SCALING = 4 
CHARACTER_SCALING = 4
SPRITE_NATIVE_SIZE = 16
CHARACTER_NATIVE_SIZE = 32
ACCESSORIES_NATIVE_SIZE = 32
ACCESSORIES_OFFSET = 32*8
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)


"Graph"
GRAPH_WIDTH = 200
GRAPH_HEIGHT = 120
GRAPH_MARGIN = 5

"Inventory Bar"
# INVENTORY_BAR_SIZE = 8
# INVENTORY_BAR_WIDTH = 504
# INVENTORY_BAR_HEIGHT = 56
# INVENTORY_BAR_HORIZONTAL_PADDING = 20
# INVENTORY_BAR_X = 500
# INVENTORY_BAR_Y = 100
# INVENTORY_SLOT_SIZE = (INVENTORY_BAR_WIDTH - INVENTORY_BAR_HORIZONTAL_PADDING ) // INVENTORY_BAR_SIZE
# INVENTORY_SLOT_SPRITE_SIZE = 35
# INVENTORY_BAR_CURSOR_SIZE = INVENTORY_SLOT_SIZE
# INVENTORY_BAR_SPRITE_SCALING = 4
INVENTORY_BAR_SLOT_A = arcade.key.KEY_1
INVENTORY_BAR_SLOT_B = arcade.key.KEY_2
INVENTORY_BAR_SLOT_C = arcade.key.KEY_3
INVENTORY_BAR_SLOT_D = arcade.key.KEY_4
INVENTORY_BAR_SLOT_E = arcade.key.KEY_5
INVENTORY_BAR_SLOT_F = arcade.key.KEY_6
INVENTORY_BAR_SLOT_G = arcade.key.KEY_7
INVENTORY_BAR_SLOT_H = arcade.key.KEY_8

"Lighting"
AMBIENT_COLOR = (200,200,200)

"Controls"
UP_KEY = arcade.key.W
DOWN_KEY = arcade.key.S
LEFT_KEY = arcade.key.A
RIGHT_KEY = arcade.key.D
INTERACT_KEY = arcade.key.ENTER

# How fast to move, and how fast to run the animation
"Animation"
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5
HIT_BOX_ALGORITHM = "Simple"
#Number correlates to 
WALK = [0,7]
CARRY = [12,7]
PICKAXE = {"sprite_location":29, "frames":5 }
SWORD = {"sprite_location":16, "frames":4 }
# Constants used to track if the player is facing left or right
FORWARD_FACING = 0
BACKWARD_FACING = 1
RIGHT_FACING = 2
LEFT_FACING = 3
INVENTORY_BAR_CURSOR_RIGHT = arcade.key.RIGHT
INVENTORY_BAR_CURSOR_LEFT = arcade.key.LEFT

FONT_PATH = "assets/assetpacks/ninja/HUD/Font/NormalFont.ttf"
EXAMPLE_EGG_SPRITE_LINK = "assets/guiassets/AssetPacks/Free Pack/Free Pixel Paper/Png/Sprites/1 items Pack/1.png"
INVENTORY_BAR_CURSOR_ASSET = "assets/guiassets/CustomAssets/InventoryCursor.png"
INVENTORY_BAR_ASSET = "assets/guiassets/CustomAssets/InventoryBar.png"