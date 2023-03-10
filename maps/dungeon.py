from classes.Rooms import Room
from constants import *
from classes.Enemy import Enemy
def setup(self):

    room = Room()
    room.entrances = {"main_room" : [SPRITE_SIZE*19,SPRITE_SIZE*22],"forest_hideout" : [SPRITE_SIZE*5,SPRITE_SIZE*9]}
    room.starting_x = SPRITE_SIZE * 11.5
    room.starting_y = SPRITE_SIZE * 2.5
    room.respawn_x = SPRITE_SIZE*5
    room.respawn_y = SPRITE_SIZE*9
    room.has_enemies = True
    room.map_file = "assets/maps/dungeon.tmx"

    room.wall_list = arcade.SpriteList()
    # all layers that are spatially hashed are "solid" - aka we can give them collision
    layer_options = {
        "walls": {
            "use_spatial_hash": True,
        },
        "trees": {
            "use_spatial_hash": True,
        },
        "trees2": {
            "use_spatial_hash": True,
        },
        "trees3": {
            "use_spatial_hash": True,
        },
        "Enemy": {
            "use_spatial_hash": True,
        }
    } 
    room.enemy = Enemy(SPRITE_SIZE*30,SPRITE_SIZE*13,"bobesrta",12)
    room.enemy2 = Enemy(SPRITE_SIZE*30,SPRITE_SIZE*5,"bobesrta",12)
    room.enemy3 = Enemy(SPRITE_SIZE*22,SPRITE_SIZE*13,"bobesrta",12)
    room.enemy4 = Enemy(SPRITE_SIZE*17,SPRITE_SIZE*9,"bobesrta",12)
    room.enemy5 = Enemy(SPRITE_SIZE*30,SPRITE_SIZE*9,"bobesrta",12)
    room.enemy6 = Enemy(SPRITE_SIZE*22,SPRITE_SIZE*6,"bobesrta",12)
    room.enemies = [room.enemy,room.enemy2,room.enemy3,room.enemy4,room.enemy5,room.enemy6]
    room.enemy_list = arcade.SpriteList()
    room.enemy_list.extend(room.enemies)
        
    

    # create tilemap, and then a scene from that tilemap. the scene is what we use.

    room.tile_map = arcade.load_tilemap(
        room.map_file, SPRITE_SCALING, layer_options=layer_options, hit_box_algorithm=None)
    
    room.scene = arcade.Scene.from_tilemap(room.tile_map)

    room.scene.add_sprite("Player", self.player_sprite)
    room.scene.add_sprite_list("Player Stuff", sprite_list = self.player_accessory_list)
    room.scene.add_sprite_list("Enemy", sprite_list=room.enemy_list)
    room.wall_sprite_list = arcade.SpriteList(use_spatial_hash=True)

    room.wall_sprite_list.extend(room.scene["walls"])
    
    room.wall_list = []
    # the rooms wall list is used for player collision.

    room.wall_list = []
    room.wall_list.append(room.scene["walls"])
    room.wall_list.append(room.scene["trees"])
    room.wall_list.append(room.scene["trees2"])
    room.wall_list.append(room.scene["trees3"])
    return room
