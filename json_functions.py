import json

def deserialise_data(file_name):
    npc_file = open(file_name, "r")
    npc_object = json.load(npc_file)
    npc_file.close()
    return npc_object

def get_one_conversation(file_name, conversation_name):
    npc_object = deserialise_data(file_name)
    conversations = npc_object.values()
    
    for conversation in conversations:
        for key in conversation.keys():
            if key == conversation_name:
                return conversation[key]
