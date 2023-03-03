
import json_functions

conversation_1 = json_functions.get_one_conversation("npc_dialogue/main_room.json","first_convo")
conversation_2 = json_functions.get_one_conversation("npc_dialogue/main_room.json","second_convo")
convensation_3 = json_functions.get_one_conversation("npc_dialogue/npc_dojo.json","first_convo")

conversation_dict = {"main_room": [conversation_1,conversation_2]}