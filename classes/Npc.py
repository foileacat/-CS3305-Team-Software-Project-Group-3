import arcade
from constants import *
import math
import random
import character_lists
from classes.Character import Character
from classes.PlayerAccessory import PlayerAccessory
import json 
import json_functions

class Npc(Character):

    """Creates our Character"""

    def __init__(self,x,y,name,id,conversation_list,):
        super().__init__()
        #initialise starting position
        #be able to pace
        self.points = [[9, -18], [9, 6], [-9, 6], [-9, -18]]
        self.set_hit_box(self.points)
        self.wanders = True
        self.home = True
        self.home_x = x
        self.home_y = y
        self.x_range = 300
        self.y_range = 200
        self.wandering = False
        self.hair = PlayerAccessory(character_lists.hairstyles,5,3)
        self.shirt = PlayerAccessory(character_lists.tops,1,3)
        self.bottoms = PlayerAccessory(character_lists.bottoms,2,6)
        self.full_body = PlayerAccessory(character_lists.full_body,4,6)
        self.shoes = PlayerAccessory(character_lists.shoes,0,1)
        self.full_body.alpha = 0
        self.populate_accessory_list()
        self.center_x = x
        self.center_y = y
        self.room = 0
        self.name = name
        self.id = id
        self.speed = 3.0
        self.interacting = False
        self.conversation_list = conversation_list 

    def wander(self):
        if self.wandering == False:
            if random.randint(0,500) == 1:
                if self.home == True:
                    if random.randint(0,1) == 1:
                        self.dest_x = self.home_x + random.randint(-self.x_range,self.x_range)
                        self.dest_y = self.home_y
                    else:
                        self.dest_x = self.home_x 
                        self.dest_y = self.home_y + random.randint(-self.y_range,self.y_range)
                else:
                    self.dest_x = self.home_x
                    self.dest_y = self.home_y
                self.wandering = True
        else:
            self.move_to(self.dest_x,self.dest_y)
        return
    
    def think(self):
        return
    
    def on_update(self, delta_time: float = 1 / 60):
        if self.wanders and self.interacting==False:
            self.wander()
        self.think()
        return super().on_update(delta_time)
    
    def move_to(self,dest_x,dest_y):
            start_x = self.center_x
            start_y = self.center_y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            if x_diff > 0:
                self.change_x = self.speed
                self.change_y = 0
            elif x_diff < 0:
                self.change_x = -self.speed
                self.change_y = 0
            if y_diff > 0:
                self.change_y = self.speed
                self.change_x = 0
            elif y_diff < 0:
                self.change_y = -self.speed
                self.change_x = 0

            self.center_x += self.change_x
            self.center_y += self.change_y

            # How far are we?
            distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

            # If we are there, head to the next point.
            if distance <= self.speed:
                self.center_x = self.dest_x
                self.center_y = self.dest_y
                self.change_x = 0
                self.change_y = 0
                if self.home == True:
                    self.home = False
                else:
                    self.home = True
                self.wandering = False
    
    def get_conversation(self, conversation_key):
        return json_functions.get_one_conversation(self.conversation_list, conversation_key)

                

