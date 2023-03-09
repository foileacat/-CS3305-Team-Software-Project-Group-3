from quests.SubQuest import Subquest
import items


class GemQuest():
    def __init__(self):
        self.active = True
        self.steps = {"leave_house": Subquest("leave_house",state="active"), "talk_to_mom": Subquest("talk_to_mom"), "witch": Subquest(
            "witch"), "blacksmith": Subquest("blacksmith"), "lonely": Subquest("lonely"),"dojo": Subquest("dojo")}
        self.char_created = False
        self.complete = False