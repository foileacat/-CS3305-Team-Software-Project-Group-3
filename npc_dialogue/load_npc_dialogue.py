import items 
def load_npc_dialogue(game,npc):
    if npc.id == "lonely_man":
        load_lonely_man_dialogue(game,npc)
    if npc.id == "blacksmith":
        load_blacksmith_dialogue(game,npc)
    if npc.id == "blacksmith_wife":
        load_blacksmith_wife_dialogue(game,npc)
    return

def load_lonely_man_dialogue(game,lonely_man):
    if game.lonely_man_quest.active == False:
        game.lonely_man_quest.active = True
        game.lonely_man_quest.steps["clear_flowers"] = "active"
    game.lonely_man_quest.update_subquests()
    game.lonely_man_quest.give_needed_items(game)
    if game.lonely_man_quest.steps["clear_flowers"] == "active":
        lonely_man.update_conversation_list("npc_dialogue/lonely_man/lonely_man_before.json")
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
