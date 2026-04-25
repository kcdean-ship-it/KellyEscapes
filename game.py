# print("Welcome to my Escape Game!")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Item:
    def __init__(self, name, description, is_moveable):
        self.name = name
        self.description = description
        self.is_moveable = is_moveable

