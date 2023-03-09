from quests.LonelyManQuest import LonelyManQuest
from quests.BlacksmithQuest import BlackSmithQuest
from quests.WitchQuest import WitchQuest
def setup_quests(game):
    game.lonely_man_quest = LonelyManQuest()
    game.blacksmith_quest = BlackSmithQuest()
    game.witch_quest = WitchQuest()
