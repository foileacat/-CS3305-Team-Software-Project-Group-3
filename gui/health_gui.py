import arcade
import arcade.gui
from constants import *
MAX_HEALTH_BAR_WIDTH = 200
def setup_health_gui(game):
    height = game.height
    width = game.width
    health_bar_length = MAX_HEALTH_BAR_WIDTH
    game.health_bar = arcade.SpriteSolidColor(width=health_bar_length, height=20, color=arcade.color.RED)
    game.health_bar.center_x=width-width/5
    game.health_bar.center_y=height-100

def update_health_bar(game):
    if game.player_sprite.health < 0:
        game.player_sprite.health = 0
    width = game.width
    start_x = width-width/5 - MAX_HEALTH_BAR_WIDTH
   
    health_bar_length = 20 * game.player_sprite.health + 1

    game.health_bar.width = health_bar_length

    game.health_bar.center_x = start_x + game.health_bar.width/2

def reposition_health_bar(game):
    height = game.height
    width = game.width
    game.health_bar.center_x=width-width/5
    game.health_bar.center_y=height-height/8