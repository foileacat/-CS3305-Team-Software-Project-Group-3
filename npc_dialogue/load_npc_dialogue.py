import items 
def load_npc_dialogue(game,npc):
    if npc.id == "lonely_man":
        load_lonely_man_dialogue(game,npc)
    if npc.id == "blacksmith":
        load_blacksmith_dialogue(game,npc)
    if npc.id == "blacksmith_wife":
        load_blacksmith_wife_dialogue(game,npc)
    if npc.id == "witch":
        load_witch_dialogue(game,npc)
    if npc.id == "sensei":
        load_sensei_dialogue(game,npc)
    if npc.id == "sensei_apprentice":
        load_apprentice_dialogue(game,npc)
    return

def load_lonely_man_dialogue(game,lonely_man):
    game.lonely_man_quest.update_subquests()
    game.lonely_man_quest.give_needed_items(game)
    if game.lonely_man_quest.steps["talk_to_old_man"] == "active":
        game.lonely_man_quest.steps["talk_to_old_man"] = "complete"
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_before.json")
        game.lonely_man_quest.steps["clear_flowers"] = "active"
    if game.lonely_man_quest.steps["hangup_washing"] == "active":
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_washing.json")
    if game.lonely_man_quest.steps["fill_cart"] == "active":
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_cart.json")
    if game.lonely_man_quest.steps["shelve_books"] == "active":
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_books.json")
    if game.lonely_man_quest.steps["plant_plants"] == "active":
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_plants.json")
    if game.lonely_man_quest.steps["sort_food"] == "active":
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_food.json")
    if game.lonely_man_quest.complete:
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_after.json")
    
   
def load_blacksmith_dialogue(game,blacksmith):
    if game.blacksmith_quest.active == False:
        game.blacksmith_quest.active = True
    game.blacksmith_quest.update_subquests(game)
    game.blacksmith_quest.give_needed_items(game)
    if game.blacksmith_quest.steps["speak_to_blacksmith"] == "active":
        game.blacksmith_quest.steps["speak_to_blacksmith"] = "complete"
        game.blacksmith_quest.steps["speak_to_wife"] = "active"
        blacksmith.update_conversation_list("npc_dialogue/blacksmith/blacksmith_before.json")

    if game.blacksmith_quest.steps["speak_to_wife"] == "complete":
        blacksmith.update_conversation_list("npc_dialogue/blacksmith/blacksmith_before.json")
        game.blacksmith_quest.steps["speak_to_wife"] = "done"

    if game.blacksmith_quest.steps["read_diary"] == "complete":
        game.blacksmith_quest.steps["read_diary"] = "done"
        game.blacksmith_quest.steps["tell_blacksmith"] = "done"
        game.blacksmith_quest.steps["collect_flowers"] = "active"
        blacksmith.update_conversation_list("npc_dialogue/blacksmith/blacksmith_read_diary.json")

    if game.blacksmith_quest.steps["collect_flowers"] == "active":
        if game.blacksmith_quest.right_flower:
            game.blacksmith_quest.steps["collect_flowers"] = "complete"
            game.blacksmith_quest.steps["collect_ores"] = "active"
            blacksmith.update_conversation_list("npc_dialogue/blacksmith/blacksmith_flower.json")
        if game.blacksmith_quest.wrong_flower:
            blacksmith.update_conversation_list("npc_dialogue/blacksmith/blacksmith_wrong_flower.json")

    if game.blacksmith_quest.steps["collect_ores"] == "complete":
        game.blacksmith_quest.steps["collect_ores"] = "done"
        blacksmith.update_conversation_list("npc_dialogue/blacksmith/blacksmith_after.json")
        game.blacksmith_quest.steps["get_gem"] = "active"
   
def load_blacksmith_wife_dialogue(game,blacksmith_wife):
    if game.blacksmith_quest.steps["speak_to_wife"] == "active":
        game.blacksmith_quest.steps["speak_to_wife"] = "complete"
        game.blacksmith_quest.steps["read_diary"] = "active"
        blacksmith_wife.update_conversation_list("npc_dialogue/blacksmith_wife/blacksmith_wife_before.json")
    if game.blacksmith_quest.steps["collect_flowers"] == "complete":
        blacksmith_wife.update_conversation_list("npc_dialogue/blacksmith_wife/blacksmith_wife_flowers.json")
    if game.blacksmith_quest.steps["collect_ores"] == "complete":
        blacksmith_wife.update_conversation_list("npc_dialogue/blacksmith_wife/blacksmith_wife_after.json")

def load_witch_dialogue(game,witch):
    quest = game.witch_quest
    subquests = quest.steps
    quest.update_subquests(game)
    quest.give_required_items(game)
    if subquests["talk_to_witch"].is_active():
        subquests["talk_to_witch"].make_complete()
        witch.update_conversation_list("npc_dialogue/witch/witch_before.json")
        subquests["fight_monsters"].activate()
    if subquests["fight_monsters"].is_active():
        if quest.monsters_defeated:
            subquests["fight_monsters"].make_complete()
            subquests["return_to_witch"].activate()
    if subquests["return_to_witch"].is_active():
        witch.update_conversation_list("npc_dialogue/witch/witch_after.json")
        subquests["return_to_witch"].make_complete()
        quest.complete = True
    
def load_sensei_dialogue(game,sensei):
    quest = game.dojo_quest
    subquests = quest.steps
    quest.update_subquests(game)
    quest.give_required_items(game)
    if subquests["talk_to_sensei"].is_active():
        sensei.update_conversation_list("npc_dialogue/sensei/sensei_before.json")
        subquests["talk_to_sensei"].make_complete()
        subquests["challenge_of_wisdom"].activate()
    if subquests["challenge_of_wisdom"].is_active():
        if quest.wisdom_challenge_complete:
            subquests["challenge_of_wisdom"].make_complete()
            sensei.update_conversation_list("npc_dialogue/sensei/sensei_strength.json")
            subquests["challenge_of_strength"].activate()
    if subquests["challenge_of_strength"].is_active():
        if quest.strength_challenge_complete:
            subquests["challenge_of_strength"].make_complete()
            sensei.update_conversation_list("npc_dialogue/sensei/sensei_courage.json")
            subquests["challenge_of_courage"].activate()
    if subquests["challenge_of_courage"].is_active():
        if quest.maze_complete:
            subquests["challenge_of_courage"].make_complete()
            sensei.update_conversation_list("npc_dialogue/sensei/sensei_after.json")
            quest.complete = True
    return

def load_apprentice_dialogue(game,apprentice):
    quest = game.dojo_quest
    subquests = quest.steps
    if subquests["talk_to_apprentice"].is_active():
        subquests["talk_to_apprentice"].make_complete()
        subquests["talk_to_sensei"].activate()
        apprentice.update_conversation_list("npc_dialogue/sensei_apprentice/sensei_apprentice_before.json")
    if subquests["challenge_of_strength"].is_active():
        apprentice.update_conversation_list("npc_dialogue/sensei_apprentice/sensei_apprentice_can.json")
    if quest.complete:
        apprentice.update_conversation_list("npc_dialogue/sensei_apprentice/sensei_apprentice_after.json")
    return