from quests.SubQuest import Subquest
import items
class WitchQuest():
    def __init__(self):
        self.active = False
        self.steps = {"talk_to_witch": Subquest("talk_to_witch"),"fight_monsters" : Subquest("fight_monsters"),"return_to_witch":Subquest("return_to_witch")}
        self.sword_given = False
        self.noodles_given = False
        self.monsters_defeated = False
        self.complete = False
        
    def update_subquests(self,game):
        if self.steps["fight_monsters"].is_active():
            enemy_room = game.rooms[11]
            if len(enemy_room.enemy_list) == 0:
                self.monsters_defeated = True


    def give_required_items(self,game):
        if self.steps["talk_to_witch"].is_completed() and self.sword_given == False:
            game.player_sprite.add_to_inventory(items.rusty_sword)
            self.sword_given = True
        if self.steps["talk_to_witch"].is_completed() and self.noodles_given == False:
            game.player_sprite.add_to_inventory(items.noodles)
            self.noodles_given = True

    def start(self):
        if self.complete == False:
            self.active = True
            self.steps["talk_to_witch"].activate()