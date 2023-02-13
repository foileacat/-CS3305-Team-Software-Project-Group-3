from classes.Rooms import RoomA
from constants import *
from classes.Npc import Npc
def setup( player_sprite, player_accessory_list):

    room = RoomA("assets/maps/starting_room.tmx",player_sprite,player_accessory_list)
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
    room.entrances = {"main_room" : [2.5*SPRITE_SIZE,7*SPRITE_SIZE]}
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
    return room