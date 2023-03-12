from quests.SubQuest import Subquest
import items


class DojoQuest():
    def __init__(self):
        self.active = False
        self.steps = {"talk_to_apprentice": Subquest("talk_to_apprentice",description="Talk to the sensei's apprentice outside."),
                       "talk_to_sensei": Subquest("talk_to_sensei",description="Ask the sensei about her challenges."),
                         "challenge_of_wisdom": Subquest("challenge_of_wisdom",description="Complete the challenge of wisdom."),
                           "challenge_of_strength": Subquest("challenge_of_strength",description="Talk to the sensei after swinging the watering can 25 times."),
                             "challenge_of_courage": Subquest("challenge_of_courage",description="Return to the sensei after completing the maze.")}
        self.watering_can_given = False
        self.maze_complete = False
        self.wisdom_challenge_complete = False
        self.strength_challenge_complete = False
        self.complete = False

    def update_subquests(self, game):
        if self.steps["challenge_of_strength"].is_active():
            if game.player_sprite.watering_can_count >= 25:
                self.strength_challenge_complete = True

    def give_required_items(self, game):
        if self.steps["challenge_of_strength"].is_active() and self.watering_can_given == False:
            game.player_sprite.add_to_inventory(items.holey_watering_can)
            self.watering_can_given = True

    def start(self):
        if self.complete == False:
            self.active = True
            self.steps["talk_to_apprentice"].activate()
