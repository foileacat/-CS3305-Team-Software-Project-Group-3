import items 
def load_npc_dialogue(game,npc):
    if npc.id == "lonely_man":
        load_lonely_man_dialogue(game,npc)
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
    
   
    