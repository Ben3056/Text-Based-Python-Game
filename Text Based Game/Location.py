x = 0
y = 0

def leave():
    move = input("Do you want to go 'N'orth, 'S'outh, 'E'ast or 'W'est? ")
    if move == "N":
        goNorth()
    elif move == "S":
        goSouth()
    elif move == "E":
        goEast()
    elif move == "W":
        goWest()
    else:
        print("Please select N, S, E or W")

def home():
    print("You're at your home! (0,0)")
    leave()

def town():
    print("You're at the town! (1,0)")
    choice = input("Do you want to buy a 'W'eapon, 'S'hield or just 'L'eave?")
    if choice == "W":
        print("This will work soon and access the player's inventory!")
    elif choice == "S":
        print("This will work soon and access the player's inventory!")
    else:
        leave()

def hole():
    print("You're at a hole! (2,0)")
    leave()

def location(x, y):
    if x == 0 and y == 0:
        home()
    elif x == 1 and y == 0:
        town()
    elif x == 2 and y == 0:
        hole()
    else:
        print("Place not defined yet! (" + str(x) + ",", str(y) +")")
        leave()

def goNorth():
    global x
    global y
    if y != 0:
        y -= 1
        location(x, y)
    else:
        print("You can't go any further North!")
        location(x, y)

def goSouth():
    global x
    global y
    if y != 2:
        y += 1
        location(x, y)
    else:
        print("You can't go any further South!")
        location(x, y)

def goEast():
    global x
    global y
    if x != 2:
        x += 1
        location(x, y)
    else:
        print("You can't go any further East!")
        location(x, y)

def goWest():
    global x
    global y
    if x != 0:
        x -= 1
        location(x, y)
    else:
        print("You can't go any further West!")
        location(x, y)

location(x, y)