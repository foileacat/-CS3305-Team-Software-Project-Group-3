from quests.LonelyManQuest import LonelyManQuest
from quests.BlacksmithQuest import BlackSmithQuest
def setup_quests(game):
    game.lonely_man_quest = LonelyManQuest()
    game.blacksmith_quest = BlackSmithQuest()
