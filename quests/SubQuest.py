from constants import *


class Subquest():
    def __init__(self,name,description="Nothing here!"):
        self.name = name
        self.description = ""
        self.state = "inactive"
        self.complete = False

    def activate(self):
        self.state = "active"

    def complete(self):
        self.state = "complete"
        self.complete = True
    
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