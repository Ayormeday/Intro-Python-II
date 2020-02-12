# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    #constructor
    def __init__(self, name, information = []):
        #attribute(name, room)
        self.name = name
        self.information = information