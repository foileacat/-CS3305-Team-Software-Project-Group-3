from classes.Rooms import Room
from constants import *
from classes.Npc import Npc
from classes.Enemy import Enemy
def setup(self):
    room = Room()
    room.has_npcs = True
    room.has_enemies = True
    room.respawn_x = 100
    room.respawn_y = 200
    room.multiple_entrances = True
    room.entrances = {"starting_room" : [SPRITE_SIZE * 11.5,SPRITE_SIZE * 2.5], "cave_outside" : [200,600], "dojo_outside": [100,100],"forest": [SPRITE_SIZE*12.5,SPRITE_SIZE*2], "dungeon": [SPRITE_SIZE*5,SPRITE_SIZE*9]}
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
        "NPC": {
            "use_spatial_hash": True,
        },
        "ENEMY": {
            "use_spatial_hash": True,
        }
    }
    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

   #
    
    room.npc_list = arcade.SpriteList()
    room.npc = Npc(500,500,"boberta",12, "npc_dialogue/main_room.json")
    room.npc_list.append(room.npc)
    room.scene.add_sprite_list("NPC", sprite_list=room.npc_list)
    room.scene.add_sprite_list("NPC Stuff", sprite_list = room.npc.accessory_list)
    room.enemy = Enemy(500,300,"bobesrta",12)
    room.enemies = []
    room.enemies.append(room.enemy)
    room.enemy_list = arcade.SpriteList()
    room.enemy_list.append(room.enemy)
    room.wall_sprite_list = arcade.SpriteList(use_spatial_hash=True)

    room.wall_sprite_list.extend(room.scene["walls"])
    room.wall_sprite_list.extend(room.scene["solids"])

    room.scene.add_sprite_list("Enemy", sprite_list=room.enemy_list)
   
    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)
    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    room.wall_list = []

    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["solids"])
    return room