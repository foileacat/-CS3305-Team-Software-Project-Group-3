from classes.Rooms import Room
from classes.Enemy import Enemy
from constants import *

def setup(self):
    room = Room()
    room.id = "enemy_house"
    room.entrances = {"forest" : [SPRITE_SIZE*14.5,SPRITE_SIZE*14]}
    room.respawn_x = 100
    room.respawn_y = 200
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
    room.map_file = "assets/maps/enemy_house.tmx"
    room.has_enemies = True
    room.wall_list = arcade.SpriteList()
    # all layers that are spatially hashed are "solid" - aka we can give them collision
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "ENEMY": {
            "use_spatial_hash": True,
        }
        
       
    }

    # create tilemap, and then a scene from that tilemap. the scene is what we use.

    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options)
    
    room.scene = arcade.Scene.from_tilemap(room.tile_map)
    room.enemy = Enemy(SPRITE_SIZE*5,SPRITE_SIZE*2,"bobesrta",12)
    room.enemy2 = Enemy(SPRITE_SIZE*12,SPRITE_SIZE*2,"bobesrta",12)
    room.enemy3 = Enemy(SPRITE_SIZE*16,SPRITE_SIZE*5,"bobesrta",12)
    room.enemy4 = Enemy(SPRITE_SIZE*1,SPRITE_SIZE*5,"bobesrta",12)
    room.enemy5 = Enemy(SPRITE_SIZE*2,SPRITE_SIZE*12,"bobesrta",12)
    room.enemy6 = Enemy(SPRITE_SIZE*15,SPRITE_SIZE*12,"bobesrta",12)
    room.enemies = [room.enemy,room.enemy2,room.enemy3,room.enemy4,room.enemy5,room.enemy6]
    room.enemy_list = arcade.SpriteList()
    room.enemy_list.extend(room.enemies)
    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)
    room.scene.add_sprite_list("Enemy", sprite_list=room.enemy_list)
    room.scene.move_sprite_list_after("over layer", "Player Stuff")
    # the rooms wall list is used for player collision.
    room.wall_sprite_list = arcade.SpriteList(use_spatial_hash=True)

    room.wall_sprite_list.extend(room.scene["walls"])
    room.wall_list = []
    
    room.wall_list.append(room.scene["walls"])
    return room

