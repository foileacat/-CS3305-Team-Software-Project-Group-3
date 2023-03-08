import arcade
from classes.InventorySlot import InventorySlot
from classes.Item import Item
from classes.Tool import Tool
from classes.Consumable import Consumable
from constants import *
import items

class LonelyManQuest():
    def __init__(self):
        self.active = False
        self.steps = {"clear_flowers":"inactive","hangup_washing":"inactive","fill_cart":"inactive","shelve_books":"inactive","plant_plants":"inactive","sort_food":"inactive"}
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
        self.steps[quest_to_check] = "complete"

    def update_subquests(self):
        if self.steps["clear_flowers"] == "complete":
            self.steps["hangup_washing"] = "active"
            self.steps["clear_flowers"] = "done"
        if self.steps["hangup_washing"] == "complete":
            self.steps["fill_cart"] = "active"
            self.steps["hangup_washing"] = "done"
        if self.steps["fill_cart"] == "complete":
            self.steps["shelve_books"] = "active"
            self.steps["fill_cart"] = "done"
        if self.steps["shelve_books"] == "complete":
            self.steps["plant_plants"] = "active"
            self.steps["shelve_books"] = "done"
        if self.steps["plant_plants"] == "complete":
            self.steps["sort_food"] = "active"
            self.steps["plant_plants"] = "done"
        if self.steps["sort_food"] == "complete":
            self.steps["sort_food"] = "done"
            self.complete = True

    def give_needed_items(self,game):
        if self.steps["shelve_books"] == "active":
            if self.book_given == False:
                game.player_sprite.add_to_inventory(items.book,if_doesnt_have=True)
                self.book_given = True
        if self.steps["clear_flowers"] == "active":
            if self.flowers_given == False:
                game.player_sprite.add_to_inventory(items.flowers,if_doesnt_have=True)
                self.flowers_given = True
        if self.steps["hangup_washing"] == "active":
            if self.shirt_given == False:
                game.player_sprite.add_to_inventory(items.shirt,if_doesnt_have=True)
                self.shirt_given = True
        if self.steps["fill_cart"] == "active":
            if self.sacks_given == False:
                game.player_sprite.add_to_inventory(items.sack,if_doesnt_have=True)
                self.sacks_given = True
        if self.steps["sort_food"] == "active":
            if self.food_given == False:
                game.player_sprite.add_to_inventory(items.berries,if_doesnt_have=True)
                game.player_sprite.add_to_inventory(items.fish,if_doesnt_have=True)
                self.food_given = True
        if self.steps["plant_plants"] == "active":
            if self.plants_given == False:
                game.player_sprite.add_to_inventory(items.plants,if_doesnt_have=True)
                self.plants_given = True
                
        else:
            return