from constants import *
from quests.SubQuest import Subquest
import items


class BlackSmithQuest():
    def __init__(self):
        self.active = False
        self.steps = {"speak_to_blacksmith": Subquest("speak_to_blacksmith",description="Talk to the Blacksmith in his house"),
                       "speak_to_wife": Subquest("speak_to_wife",description="Talk to the blacksmith's wife."),
                         "read_diary": Subquest("read_diary",description="Find a clue in the house to figure out her favorite flower."),
                           "tell_blacksmith": Subquest("tell_blacksmith",description="Tell the blacksmith about her favorite flower."),
                             "collect_flowers": Subquest("collect_flowers",description="Bring the blacksmith his wife's favorite flower."),
                               "collect_ores": Subquest("collect_ores",description="Use the pickaxe to collect the ores, and bring them to the blacksmith"),
                                 "get_gem": Subquest("get_gem",description="Use the key to collect the gem from the mine.")}
        self.complete = False
        self.diary_read = False
        self.pickaxe_key_given = False
        self.gem_key_given = False
        self.wrong_flower = False
        self.right_flower = False

    def update_subquests(self, game):
        if self.steps["collect_flowers"].is_active():
            if game.player_sprite.is_holding_item():
                if game.player_sprite.current_item().name == "Red Flower":
                    self.right_flower = True
                    self.wrong_flower = False
                    game.player_sprite.remove_from_inventory("Red Flower")
                    game.player_sprite.remove_from_inventory("Yellow Flower")
                    game.player_sprite.remove_from_inventory("White Flower")
                elif game.player_sprite.current_item().name == "White Flower" or game.player_sprite.current_item().name == "Yellow Flower":
                    self.wrong_flower = True
                    self.right_flower = False
                else:
                    self.wrong_flower = False
                    self.right_flower = False

        elif self.steps["collect_ores"].is_active():
            if game.player_sprite.has_amount_of_items("Amethyst Ore", 10):
                if game.player_sprite.has_amount_of_items("Emerald Ore", 9):
                    if game.player_sprite.has_amount_of_items("Sapphire Ore", 3):
                        if game.player_sprite.has_amount_of_items("Amber Ore", 5):
                            self.steps["collect_ores"].make_done()
                            game.player_sprite.remove_from_inventory(
                                "Amethyst Ore")
                            game.player_sprite.remove_from_inventory(
                                "Emerald Ore")
                            game.player_sprite.remove_from_inventory(
                                "Sapphire Ore")
                            game.player_sprite.remove_from_inventory(
                                "Amber Ore")
            return

    def give_needed_items(self, game):
        if self.steps["collect_ores"].is_active():
            if self.pickaxe_key_given == False:
                game.player_sprite.add_to_inventory(
                    items.pickaxe_key, if_doesnt_have=True)
                self.pickaxe_key_given = True
        if self.steps["get_gem"].is_active():
            if self.gem_key_given == False:
                game.player_sprite.add_to_inventory(
                    items.gem_key, if_doesnt_have=True)
                self.gem_key_given = True
        

    def start(self):
        if self.complete == False:
            self.active = True
            self.steps["speak_to_blacksmith"].activate()
            
