from classes.Rooms import Room
from constants import *

def setup(self):
    room = Room()
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
    room.map_file = "assets/maps/forest.tmx"
    room.entrances = {"main_room" : [SPRITE_SIZE*9,SPRITE_SIZE*2],"enemy_house" : [SPRITE_SIZE*9,SPRITE_SIZE*7.5]}
    #room.wall_list = arcade.SpriteList()
    # all layers that are spatially hashed are "solid" - aka we can give them collision
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "building": {
            "use_spatial_hash": True,
        }
    }

    # create tilemap, and then a scene from that tilemap. the scene is what we use.

    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)
    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    # the rooms wall list is used for player collision.
    room.wall_list = []
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["building"])
    return room