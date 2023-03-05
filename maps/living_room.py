from classes.Rooms import Room
from constants import *

def setup(self):
    room = Room()
    room.multiple_entrances = True
    room.entrances = {"cave_outside" : [19.5*SPRITE_SIZE,4*SPRITE_SIZE], "kitchen" : [14*SPRITE_SIZE,5*SPRITE_SIZE], "bedroom" : [3*SPRITE_SIZE,12*SPRITE_SIZE]}
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
    room.map_file = "assets/maps/living room.tmx"

    room.wall_list = arcade.SpriteList()
    # all layers that are spatially hashed are "solid" - aka we can give them collision
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "furniture": {
            "use_spatial_hash": True,
        },
        "over layer": {
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
    room.wall_list.append(room.scene["furniture"])

    return room
