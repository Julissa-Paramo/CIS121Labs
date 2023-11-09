"""
Julissa Paramo
11 / 9 / 23

This implements the RoboFriend class.
"""

class RoboFriend: # creates class named RoboFriend

    def __init__(self, _name, _age): # initializing variables for the object 

        self.name = _name

        self.age = _age

    def get_name(self): # getters

        return self.name
    
    def get_age(self):

        return self.age
    
    def set_name(self,new_name): # setters

        self.name = new_name

    def set_age(self,new_age):

        self.age = new_age

    def stageName(self): # method for name statement

        return f'Hello. My name is {self.get_name()}'

    def stageAge(self): # method for age statement

        return f"I'm {self.get_age()} years old"
