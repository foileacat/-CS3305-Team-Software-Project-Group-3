from constants import *


class Subquest():
    def __init__(self,name,description="Nothing here!",state="inactive"):
        self.name = name
        self.description =description
        self.state = state
        self.completed = False

    def activate(self):
        self.state = "active"

    def make_complete(self):
        self.state = "complete"
        self.completed = True
    
    def make_done(self):
        self.state = "done"

    def is_active(self):
        if self.state == "active":
            return True
        else:
            return False
        
    def is_completed(self):
        if self.state == "complete":
            return True
        else:
            return False
    
    def is_done(self):
        if self.state == "done":
            return True
        else:
            return False
        