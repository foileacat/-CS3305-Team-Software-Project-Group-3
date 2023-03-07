from classes.Rooms import Room
from constants import *
from classes.Npc import Npc
def setup(self):
    room = Room()
    room.has_npcs = True
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
    room.map_file = "assets/maps/lonely_house.tmx"
    room.entrances = {"forest_hideout" : [SPRITE_SIZE*12,SPRITE_SIZE*7]}
    room.wall_list = arcade.SpriteList()
    # all layers that are spatially hashed are "solid" - aka we can give them collision
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "over layer": {
            "use_spatial_hash": True,
        },
        "furniture": {
            "use_spatial_hash": True,
        }      
    }

    # create tilemap, and then a scene from that tilemap. the scene is what we use.

    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    room.npc_list = arcade.SpriteList()
    room.npc =  Npc(300,350,"None",12, "npc_dialogue/generic_npc.json") 
    room.npc_list.append(room.npc)
    room.scene.add_sprite_list("NPC", sprite_list=room.npc_list)
    room.scene.add_sprite_list("NPC Stuff", sprite_list = room.npc.accessory_list)

    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)
    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    room.scene.move_sprite_list_after("renovation1", "Player Stuff")
    room.scene.move_sprite_list_after("renovation2", "Player Stuff")
    # the rooms wall list is used for player collision.
    room.wall_list = []
    
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["furniture"])
    room.scene["renovation1"].visible=False
    room.scene["renovation2"].visible=False
    room.scene["renovation3"].visible=False
    room.scene["renovation4"].visible=False
    room.scene["renovation5"].visible=False
    room.scene["renovation6"].visible=False
    #room.wall_list.append(room.scene["Trees 1"])
    #room.wall_list.append(room.scene["Trees 2"])
    #room.wall_list.append(room.scene["House"])
    return room