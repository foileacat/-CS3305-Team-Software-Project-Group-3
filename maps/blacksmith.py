from classes.Rooms import Room
from constants import *
from classes.Npc import Npc

def setup(self):
    room = Room()
    room.multiple_entrances = True
    room.entrances = { "cave_outside" : [5*SPRITE_SIZE,12*SPRITE_SIZE],}
    room.map_file = "assets/maps/blacksmith.tmx"
    room.has_npcs = True
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
    room.npc_list = arcade.SpriteList()
    room.npc = Npc(290,300,"Blacksmith",12, "npc_dialogue/generic_npc.json") 
    room.npc_list.append(room.npc)
    
    
    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    
    room.scene.add_sprite_list("NPC", sprite_list=room.npc_list)
    room.scene.add_sprite_list("NPC Stuff", sprite_list = room.npc.accessory_list)
    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)
    
    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    # the rooms wall list is used for player collision.

    room.wall_list = []
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["furniture"])

    return room
