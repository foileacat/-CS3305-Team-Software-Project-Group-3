from classes.Rooms import Room
from constants import *
from classes.Npc import Npc

def setup(self):
    room = Room()
    room.has_npcs = True
    room.multiple_entrances = True
    room.entrances = {"dojo_outside" : [1300,610], "maze" : [SPRITE_SIZE*2,SPRITE_SIZE*3]}
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
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
        "over layer": {
            "use_spatial_hash": True,
        }
        
        
        
    }

    # create tilemap, and then a scene from that tilemap. the scene is what we use.

    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    room.npc_list = arcade.SpriteList()
    room.npc =  Npc(500,500,"None","sensei", "npc_dialogue/generic_npc.json")
    room.npc.change_appearance([11,0],[8,3],False,[4,0],[0,0])
    room.npc_list.append(room.npc)
    room.scene.add_sprite_list("NPC", sprite_list=room.npc_list)
    room.scene.add_sprite_list("NPC Stuff", sprite_list = room.npc.accessory_list)
    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)

    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    room.scene.move_sprite_list_after("Animation", "Player Stuff")
    # the rooms wall list is used for player collision.

    room.wall_list = []
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["furniture"])

    return room