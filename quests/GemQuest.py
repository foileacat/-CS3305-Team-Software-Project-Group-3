from quests.SubQuest import Subquest
import items


class GemQuest():
    def __init__(self):
        self.active = True
        self.steps = {"customise": Subquest("customise",state="active"), "talk_to_mom": Subquest("talk_to_mom"), "witch": Subquest(
            "witch"), "blacksmith": Subquest("blacksmith"), "lonely": Subquest("lonely"),"dojo": Subquest("dojo")}
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
            