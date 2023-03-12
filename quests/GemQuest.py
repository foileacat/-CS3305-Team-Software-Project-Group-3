from quests.SubQuest import Subquest
import items


class GemQuest():
    def __init__(self):
        self.active = True
        self.steps = {"customise": Subquest("customise",state="active",description="Get dressed at the dresser in your house."),
                       "talk_to_mom": Subquest("talk_to_mom",description="Talk to mom in the forest outside."),
                         "witch": Subquest("witch",description="Talk to mom once you find the gem in the witches forest."),
                           "blacksmith": Subquest("blacksmith",description="Talk to mom once you get the gem from the blacksmith."),
                             "lonely": Subquest("lonely",description="Talk to mom after find the gem from the family in the woods"),
                             "dojo": Subquest("dojo",description="Tell mom after you find the final gem in the dojo."),
                             "finished":Subquest("finished",description="Congratulations! You found all the gems, the village is safe again!")}
        self.char_created = False
        self.complete = False
        self.witch = False
        self.blacksmith = False
        self.lonely = False
        self.dojo = False

    def update_subquests(self, game):
        if game.witch_quest.complete and self.witch == False:
            self.steps["witch"].make_done()
            self.witch = True
        if game.blacksmith_quest.complete and self.blacksmith == False:
            self.steps["blacksmith"].make_done()
            self.blacksmith = True
        if game.lonely_man_quest.complete and self.lonely == False:
            self.steps["lonely"].make_done()
            self.lonely = True
        if game.dojo_quest.complete and self.dojo == False:
            self.steps["dojo"].make_done()
            self.dojo = True
            self.steps["finished"].activate()
            