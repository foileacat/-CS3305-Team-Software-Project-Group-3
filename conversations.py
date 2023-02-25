'''
unsure if it should be class, cause npc has a conversation
or should each npc have a list 
im a bit confused cause i feel everything is feeding into each other and ive made a huge mess
maybe i should start again
  :(
'''



'''
import json_functions

class Conversation():
  def __init__(self):
    self.conversation_list = []
    self.length = len(self.conversation_list)
  
  def add_conversation(self):
    pass

  def get_conversation(self):
    pass

    
'''
    



conversation_1 = json_functions.get_one_conversation("npc_dialogue/main_room.json","first_convo")
conversation_2 = json_functions.get_one_conversation("npc_dialogue/main_room.json","second_convo")


conversation_dict = {"main_room": [conversation_1,conversation_2]}