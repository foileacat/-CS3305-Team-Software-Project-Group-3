import arcade
from constants import *

class Room:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self):
        # You may want many lists. 
       #Lists for coins, monsters, etc.
        self.entrances = []
        self.multiple_entrances = False
        self.has_npcs = False
        self.has_enemies = False
        self.map_file = ""
        self.wall_list = None
        self.wall_list = None
        self.layer_options = {}
        self.background = None


class RoomA:
    """
    This class holds all the information about the
    different rooms.
    """

    def __init__(self, map_file, player_sprite, player_accessory_list):
        # You may want many lists. 
       #Lists for coins, monsters, etc.
        self.entrances = {}
        self.multiple_entrances = False
        self.has_npcs = False
        self.has_enemies = False
        self.map_file = map_file
        self.background = None
        self.wall_list = arcade.SpriteList()
        self.wall_list = []
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
        
        self.tile_map = arcade.load_tilemap(
        self.map_file, SPRITE_SCALING, layer_options=layer_options)
            
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene.add_sprite("Player", player_sprite)
        self.scene.add_sprite_list("Player Stuff", sprite_list = player_accessory_list)
        self.scene.move_sprite_list_after("over layer", "Player Stuff")
        # the rooms wall list is used for player collision.
        

        
        self.wall_list.append(self.scene["walls"])
        self.wall_list.append(self.scene["furniture"])

        