"""
Julissa Paramo
11 / 9 / 23

Uses RoboFriend class to create 3 objects
"""

from ClassFile import * # imports everything from ClassFile ( contains RoboFriend class )

friend1 = RoboFriend('Aang', 12) # first object 

friend2 = RoboFriend('Sokka', 15) # second object

friend3 = RoboFriend ('Katara', 14) # third object

print(friend1.stageName()) # calls stageName method 

print(friend1.stageAge()) # calls stageAge method

print(friend2.stageName())

print(friend2.stageAge())

print(friend3.stageName())

print(friend3.stageAge())
