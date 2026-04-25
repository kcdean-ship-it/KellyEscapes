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

# create rooms
entry = Room("Entry", "You are in the front entry of the house. To the north is the locked front door, and there are three doors leading off the entry: one to the west, one to the south, and one to the east. On either side of the door leading south, there is a potted plant.")
living = Room("Living Room", "You are now in the living room. There is a big pillow on the couch, an empty mug on the coffee table, and a painting hanging on the wall. There is also a door to the south leading to another room.")
kitchen = Room("Kitchen", "Welcome to the Kitchen! It's a bit messy in here! There's a dirty pot in the sink, a used napkin on the counter, and a note on the fridge. And to the west is another door.")
office = Room("Home Office", "Congratulations, you've unlocked the office! In front of you is a desk with a book on it, and behind that desk is a bookshelf that looks like it contains a safe.")
dining = Room("Dining Room", "You've entered the dining room. In the middle of the room is a dining table. There is a vase with flowers and two candles flanking it in the middle of the table. There are three more doors leading to the west, south and east.")
bath = Room("Bathroom", "You are in the bathroom. In the bath tub is a yellow rubber duck, and on the floor is a blue bathmat. On the sink is a toothbrush holder and some soap.")
bed = Room("Bedroom", "Welcome to the bedroom! There is a big king bed against the south wall of the room and on either side of the bed is a nightstand. On the left nightstand is lamp, and on the right nightstand is a jewelry box.")

