from classes.Rooms import Room
from constants import *

def setup(self):
    room = Room()
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
    room.map_file = "assets/maps/forest_hideout.tmx"
    room.entrances = {"dungeon" : [SPRITE_SIZE*33,SPRITE_SIZE*10],"lonely_house" : [SPRITE_SIZE*7,SPRITE_SIZE*3]}
    room.wall_list = arcade.SpriteList(visible=False)
   
    # all layers that are spatially hashed are "solid" - aka we can give them collision
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "renovation2": {
            "use_spatial_hash": True,
        },
        "trees": {
            "use_spatial_hash": True,
        },
        "trees2": {
            "use_spatial_hash": True,
        },
        "trees 3": {
            "use_spatial_hash": True,
        }
        
    }

    # create tilemap, and then a scene from that tilemap. the scene is what we use.

    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options, hit_box_algorithm=None)
    
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)
    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    # the rooms wall list is used for player collision.
    room.wall_list = []
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["trees"])
    room.wall_list.append(room.scene["trees2"])
    room.wall_list.append(room.scene["trees 3"])
    room.wall_list.append(room.scene["renovation2"])
    room.scene["renovation1"].visible=False
    room.scene["renovation2"].visible=False
    room.scene["renovation3"].visible=False
    room.scene["renovation4"].visible=False
    room.scene["renovation5"].visible=False
    room.scene["renovation6"].visible=False
    room.scene["renovation7"].visible=False
    room.scene["renovation8"].visible=False
    room.scene["renovation9"].visible=False
    return room