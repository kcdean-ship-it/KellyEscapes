# print("Welcome to my Escape Game!")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Item:
    def __init__(self, name, description, is_moveable):
        self.name = name
        self.description = description
        self.is_moveable = is_moveable
        self.searched = False
        self.contains = None

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
        self.notes = []

# create rooms
entry = Room("Entry", "You are in the front entry of the house. To the north is the locked front door, and there are three doors leading off the entry: one to the west, one to the south, and one to the east. On either side of the door leading south, there is a potted plant.")
living = Room("Living Room", "You are now in the living room. There is a big pillow on the couch, a mug on the coffee table, and a painting hanging on the wall. There are two doors: one to the south and one to the east.")
kitchen = Room("Kitchen", "Welcome to the Kitchen! It's a bit messy in here! There's a dirty pot in the sink, a used napkin on the counter, and a note on the fridge. To the north is a door and to the east is another door.")
office = Room("Home Office", "Congratulations, you've unlocked the office! In front of you is a desk with a book on it, and behind that desk is a bookshelf that looks like it contains a safe. The door leading out of the office and back to the entry in on the west wall.")
dining = Room("Dining Room", "You've entered the dining room. In the middle of the room is a dining table. There is a vase with flowers and two candles flanking it in the middle of the table. There are four doors, one in each direction.")
bath = Room("Bathroom", "You are in the bathroom. In the bath tub is a yellow rubber duck, and on the floor is a bathmat. On the sink is a toothbrush holder and a bar of soap. The door you walked through is on the north wall of the bathroom.")
bed = Room("Bedroom", "Welcome to the bedroom! There is a big king bed against the south wall of the room and on either side of the bed is a nightstand. On the left nightstand is a lamp, and on the right nightstand is a jewelry box. The bedroom door is on the west wall of the room.")

# create items
# entry items
plant_left = Item("Left plant", "This plant looks small and lightweight.", True)
plant_right = Item("Right plant", "This plant is big and looks very heavy.", False)

# living room items
pillow = Item("Couch pillow", "The pillow is in the middle of the couch. It appears to be more decorative than practical.", True)
mug = Item("Mug", "The mug is empty and looks like it's been sitting there a while.", True)
painting = Item("Wall painting", "This is a painting of the beach at sunset. It looks kind of crooked on the wall.", True)

# kitchen items
pot = Item("Dirty pot", "The pot is full of soapy water, someone must have left it to soak.", False)
napkin = Item("Dirty napkin", "The napkin has been used to clean up some jam.", True)
note = Item("Note", "The note says 'Birthday: 4/1/03'.", True)

# office items
book = Item("Book", "The book is the Bible.", True)
safe = Item("Safe", "The safe is locked and needs a 4 digit code, perhaps a birthday?", False)

# dining room items
candle_1 = Item("Candle", "This candle is old and almost all used up.", True)
candle_2 = Item("Candle", "This candle has never been used and looks as though it is brand new.", True)
vase = Item("Flower vase", "The vase has a beautiful bouquet of roses in it and there is a lot of water in the base of the vase.", False)

# bathroom items
duck = Item("Rubber duck", "The rubber duck is lying on it's side in the middle of the tub.", True)
bathmat = Item("Bathmat", "The bathmat is in front of the toilet and it's wrinkled and crooked, like it's been moved.", True)
holder = Item("Toothbrush holder", "The toothbrush holder is on the left side of the sink and there is one toothbrush in it.", True)
soap = Item("Bar of soap", "The bar of soap is on the right side of the sink. It looks old.", False)

# bedroom items
lamp = Item("Lamp", "The lamp is fancy and looks expesive, and it appears to be very delicate and fragile.", False)
jewelry_box = Item("Jewelry box", "The jewelry box is small and wooden. I wonder if there is something inside?", True)

# create exits
entry.exits = {"north": pass, "west": living, "south": dining}
living.exits = {"south": kitchen, "east": entry}
kitchen.exits = {"north": living, "east": dining}
office.exits = {"west": entry}
dining.exits = {"north": entry, "west": kitchen, "east": bed, "south": bath}
bath.exits = {"north": dining}
bed.exits = {"west": dining}

entry.exits["east"] = office # locked

# connect rooms and items
entry.items = [plant_left, plant_right]
living.items = [pillow, mug, painting]
kitchen.items = [pot, napkin, note]
office.items = [book, safe]
dining.items = [candle_1, candle_2, vase]
bath.items = [duck, bathmat, holder, soap]
bed.items = [lamp, jewelry_box]

# create player
player = Player("The Player", entry)

# clues
# key
jewelry_box.contains = "office_key"

# numbers for final code
plant_left.contains = "green 3"
painting.contains = "red 9"
candle_2.contains = "orange 1"
bathmat.contains = "blue 8"

# order of numbers clue
safe.contains = "order clue"

# game play
print("Welcome to Kelly's Escape Game!")
print("\nYour friend Kelly wants to see how smart you are so she locked you inside her house to see if you could escape.")
print("\nYou are in the entry room of the house and need a 4 digit code to unlock the front door.")

