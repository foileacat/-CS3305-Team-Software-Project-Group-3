from quests.LonelyManQuest import LonelyManQuest
from quests.BlacksmithQuest import BlackSmithQuest
from quests.WitchQuest import WitchQuest
from quests.DojoQuest import DojoQuest
def setup_quests(game):
    game.lonely_man_quest = LonelyManQuest()
    game.blacksmith_quest = BlackSmithQuest()
    game.witch_quest = WitchQuest()
    game.dojo_quest = DojoQuest()
    game.quests = [game.dojo_quest,game.witch_quest,game.blacksmith_quest,game.lonely_man_quest]