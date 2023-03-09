import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from classes.Tool import Tool
from classes.Consumable import Consumable
from constants import *
from quests.SubQuest import Subquest
import items

class LonelyManQuest():
    def __init__(self):
        self.active = False
       # self.steps = {"talk_to_old_man":"inactive","clear_flowers":"inactive","hangup_washing":"inactive","fill_cart":"inactive","shelve_books":"inactive","plant_plants":"inactive","sort_food":"inactive"}
        self.steps = {"talk_to_old_man":Subquest("talk_to_old_man"),"clear_flowers":Subquest("clear_flowers"),"hangup_washing":Subquest("hangup_washing"),"fill_cart":Subquest("fill_cart"),"shelve_books":Subquest("shelve_books"),"plant_plants":Subquest("plant_plants"),"sort_food":Subquest("sort_food")}
        self.complete = False
        self.book_given = False##
        self.sacks_given = False
        self.food_given = False
        self.flowers_given = False##
        self.shirt_given = False ##
        self.plants_given = False

    def check_subquest(self,game,interactable):
        quest_to_check = interactable.properties["quest"]
        interactables = game.scene["interactables"]
        for item in interactables:
            if item.properties["on_interact"] == "renovate":
                if item.properties["quest"] == quest_to_check:
                    if item.properties["complete"]:
                        pass
                    else:
                        return False
        self.steps[quest_to_check].make_complete()

    def update_subquests(self):
        if self.steps["clear_flowers"].is_completed():
            self.steps["hangup_washing"].activate()
            self.steps["clear_flowers"].make_done()
        if self.steps["hangup_washing"].is_completed():
            self.steps["fill_cart"].activate()
            self.steps["hangup_washing"].make_done()
        if self.steps["fill_cart"].is_completed():
            self.steps["shelve_books"].activate()
            self.steps["fill_cart"].make_done()
        if self.steps["shelve_books"].is_completed():
            self.steps["plant_plants"].activate()
            self.steps["shelve_books"].make_done()
        if self.steps["plant_plants"].is_completed():
            self.steps["sort_food"].activate()
            self.steps["plant_plants"].make_done()
        if self.steps["sort_food"].is_completed():
            self.steps["sort_food"].make_done()
            self.complete = True

    def give_needed_items(self,game):
        if self.steps["shelve_books"].is_active():
            if self.book_given == False:
                game.player_sprite.add_to_inventory(items.book,if_doesnt_have=True)
                self.book_given = True
        if self.steps["clear_flowers"].is_active():
            if self.flowers_given == False:
                game.player_sprite.add_to_inventory(items.flowers,if_doesnt_have=True)
                self.flowers_given = True
        if self.steps["hangup_washing"].is_active():
            if self.shirt_given == False:
                game.player_sprite.add_to_inventory(items.shirt,if_doesnt_have=True)
                self.shirt_given = True
        if self.steps["fill_cart"].is_active():
            if self.sacks_given == False:
                game.player_sprite.add_to_inventory(items.sack,if_doesnt_have=True)
                self.sacks_given = True
        if self.steps["sort_food"].is_active():
            if self.food_given == False:
                game.player_sprite.add_to_inventory(items.berries,if_doesnt_have=True)
                game.player_sprite.add_to_inventory(items.fish,if_doesnt_have=True)
                self.food_given = True
        if self.steps["plant_plants"].is_active():
            if self.plants_given == False:
                game.player_sprite.add_to_inventory(items.plants,if_doesnt_have=True)
                self.plants_given = True
                
        else:
            return
        
    def start(self):
        if self.complete == False:
            self.active = True
            self.steps["talk_to_old_man"].activate()