from classes.Rooms import Room
from constants import *


def setup(player_sprite, player_accessory_list):
    room = Room()
    room.multiple_entrances = True
    room.entrances = {"starting_room" : [SPRITE_SIZE * 11.5,SPRITE_SIZE * 2.5], "cave_outside" : [200,600], "dojo_outside": [100,100],"forest": [SPRITE_SIZE*12.5,SPRITE_SIZE*2]}
    room.starting_x = SPRITE_SIZE * 2.5
    room.starting_y = SPRITE_SIZE * 7
    room.map_file = "assets/maps/main_room.tmx"
    room.wall_list = arcade.SpriteList()
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "solids": {
            "use_spatial_hash": True,
        },
    }
    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    room.scene.add_sprite("Player", player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = player_accessory_list)
    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    room.wall_list = []
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["solids"])
    room.scene.update_animation
    return room