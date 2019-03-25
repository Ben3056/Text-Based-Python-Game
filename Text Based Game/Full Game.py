import os
import random

# Global Variables #
playerName = ""
playerHealth = 0
playerWeapon = ""
playerShield = ""
playerGold = 0
attackDamage = 0
defenseValue = 0
x = 0
y = 0
monsterName = ""
monsterHealth = 0
monsterAttack = 0
monsterDefense = 0
monsterGold = 0
weaponPrice = 0

def savePlayer():
    global playerName
    global playerHealth
    global playerWeapon
    global playerShield
    global playerGold
    global x
    global y

    text = "\\gameplay\\playerData.txt"
    path = os.getcwd()+text
    file = open(path,'w')
    playerStats = [playerName.strip(), str(playerHealth).strip(), playerWeapon.strip(), str(playerShield).strip(), str(playerGold).strip(), str(x).strip(), str(y).strip()]

    for line in playerStats:
        file.write(line)
        file.write("\n")
    file.close()
    print("Saved game!")

def createPlayer():
    global playerName
    global playerHealth
    global playerWeapon
    global playerShield
    global playerGold

    playerName = input("Enter your player name: ")
    print("Your name is", playerName)
    difficulty = input("Please select your difficulty, 'E'asy, 'M'edium, 'H'ard or 'C'ustom: ")
    if difficulty == "E":
        text = "\\gameplay\\Easy.txt"
        path = os.getcwd()+text
        file = open(path,'r')
    elif difficulty == "M":
        text = "\\gameplay\\Medium.txt"
        path = os.getcwd()+text
        file = open(path,'r')
    elif difficulty == "H":
        text = "\\gameplay\\Hard.txt"
        path = os.getcwd()+text
        file = open(path,'r')
    elif difficulty == "C":
        text = "\\gameplay\\Custom Difficulty.txt"
        path = os.getcwd()+text
        file = open(path,'r')

    playerHealth, playerWeapon, playerShield, playerGold = file.readlines()
    file.close()
    savePlayer()

def loadPlayer():
    try:
        text = "\\gameplay\\playerData.txt"
        path = os.getcwd()+text
        file = open(path,'r')
    except:
        createPlayer()

    try:
        global playerName, playerHealth, playerWeapon, playerShield, playerGold, x, y

        playerName, playerHealth, playerWeapon, playerShield, playerGold, x, y = file.readlines()
        x = x.strip()
        x = int(x)
        y = y.strip()
        y = int(y)
        print("Name:", playerName + "Health:", playerHealth + "Weapon:", playerWeapon + "Defense:", playerShield + "Gold:", playerGold + "X: ", str(x) + " " + "Y: ", str(y))
        file.close()
    except:
        input("Missing data for player!")
        file.close()
        createPlayer()
    weaponStats()

def startGame():
    startChoice = input("If you want to play press P if you want to start a new game press N: ")
    if  startChoice == "P":
        loadPlayer()
    elif startChoice == "N":
        createPlayer()
        loadPlayer()

def weaponStats():
    global playerWeapon, playerShield, attackDamage, defenseValue, weaponPrice

    playerWeapon = playerWeapon.strip()
    text = "\\weapons\\{}.txt".format(playerWeapon)
    path = os.getcwd()+text
    file = open(path,'r')
    playerWeapon, attackDamage, weaponPrice = file.readlines()
    file.close()
    playerWeapon = playerWeapon.strip()
    attackDamage = int(attackDamage.strip())
    weaponPrice = int(weaponPrice.strip())
    print(playerWeapon + ":", attackDamage)

    playerShield = playerShield.strip()
    text = "\\shields\\{}.txt".format(playerShield)
    path = os.getcwd()+text
    file = open(path,'r')
    playerShield, defenseValue = file.readlines()
    file.close()
    playerShield = playerShield.strip()
    defenseValue = defenseValue.strip()
    print(playerShield + ":", defenseValue)

startGame()

def randMonster(difficulty):
    global monsterName, monsterHealth, monsterAttack, monsterDefense, monsterGold

    easyMonsters = os.listdir(".\\gameplay\\Easy Monsters")
    mediumMonsters = os.listdir(".\\gameplay\\Medium Monsters")
    hardMonsters = os.listdir(".\\gameplay\\Hard Monsters")
    Bosses = os.listdir(".\\gameplay\\Bosses")
    
    if difficulty == 1:
        text = "\\gameplay\\Easy Monsters\\{}".format(random.choice(easyMonsters))
    if difficulty == 2:
        text = "\\gameplay\\Medium Monsters\\{}".format(random.choice(mediumMonsters))
    if difficulty == 3:
        text = "\\gameplay\\Hard Monsters\\{}".format(random.choice(hardMonsters))
    if difficulty == 4:
        text = "\\gameplay\\Bosses\\{}".format(random.choice(Bosses))
    path = os.getcwd()+text
    file = open(path,'r')
    monsterName, monsterHealth, monsterAttack, monsterDefense, monsterGold = file.readlines()
    file.close()
    return monsterName
    
def playerDied():
    global monsterHealth, attackDamage, monsterAttack, playerHealth, monsterName, monsterGold, playerGold, playerName, x, y
    playerGold = int(playerGold)
    lostGold = playerGold - playerGold * 33 / 100
    lostGold = round(lostGold)
    playerGold -= lostGold
    print("You died, returning you back home and you lose " + str(lostGold) + " gold!")
    savePlayer()
    x = 0
    y = 0
    location(x, y)

def monsterDied():
    global monsterHealth, attackDamage, monsterAttack, playerHealth, monsterName, monsterGold, playerGold, playerName, x, y
    playerGold = int(playerGold)
    monsterGold = int(monsterGold)
    playerGold += monsterGold
    print("The " + monsterName.strip() + " is dead! You gained " + str(monsterGold).strip() + " gold!")

def fight(difficulty):
    savePlayer()
    global monsterHealth, monsterDefense, attackDamage, defenseValue, monsterAttack, playerHealth, monsterName, monsterGold, playerGold, playerName, x, y
    attackDamage = int(attackDamage)
    print("Watch out a " + randMonster(difficulty).strip() + " is approaching!")
    monsterHealth = int(monsterHealth)
    playerHealth = int(playerHealth)
    monsterAttack = int(monsterAttack)
    monsterDefense = int(monsterDefense)
    defenseValue = int(defenseValue)
    while playerHealth > 0 and monsterHealth > 0:
        choice = input("Do you want to 'A'ttack or 'D'efend? ")
        monsterChoice = random.randint(1, 2)
        if choice == "A":
            if monsterChoice == 1:
                monsterHealth -= attackDamage
                if monsterHealth <= 0:
                    monsterDied()
                else:
                    playerHealth -= monsterAttack
                    if playerHealth > 0:
                        print("You attacked the " + monsterName + " and it attacked you!")
                        print(playerName.strip() + "'s health: " + str(playerHealth))
                        print(monsterName.strip() + "'s health: " + str(monsterHealth))
                    else:
                        playerDied()
            elif monsterChoice == 2:
                monsterDefended = monsterHealth + monsterDefense
                monsterDefended -= attackDamage
                if monsterDefended < monsterHealth:
                    monsterHealth = monsterDefended
                    if monsterHealth > 0:
                        print("The " + monsterName.strip() + " defended for " + str(monsterDefense).strip() + " points!")
                        print("You attacked the monster for " + str(attackDamage).strip())
                        print("The " + monsterName.strip() + " has " + str(monsterHealth).strip() + " health left!")
                    else:
                        monsterDied()
                else:
                    print("The " + monsterName.strip() + " blocked your attack!")
        elif choice =="D":
            playerDefended = playerHealth + defenseValue
            playerDefended -= monsterAttack
            if monsterChoice == 1:
                if playerDefended < playerHealth:
                    playerHealth = playerDefended
                    if playerHealth > 0:    
                        print("You  defended for " + str(defenseValue).strip() + " points!")
                        print("The " + monsterName.strip() + " attacked you for " + str(monsterAttack).strip())
                        print("You have " + str(playerHealth).strip() + " left!")
                    else:
                        playerDied()
                else:
                    print("You blocked the " + monsterName.strip() + "'s attack!")
            elif monsterChoice == 2:
                print("You both stand guard!")

def leave():
    move = input("Do you want to go 'N'orth, 'S'outh, 'E'ast or 'W'est or save the 'G'ame? ")
    if move == "N":
        goNorth()
    elif move == "S":
        goSouth()
    elif move == "E":
        goEast()
    elif move == "W":
        goWest()
    elif move == "G":
        savePlayer()
        loadPlayer()
        leave()
    else:
        print("Please select N, S, E, W or G")
        leave()

def home():
    global playerHealth
    playerHealth = int(playerHealth)
    print("You're at your home", playerName.strip(), " (0,0)")
    if playerHealth < 10:
        playerHealth = 10
        print("Your health has been restored to 10 hp!")
    savePlayer()
    leave()

def town():
    global playerWeapon, attackDamage, weaponPrice, playerGold
    
    print("You're at the town! (1,0)")
    choice = input("Do you want to buy a 'W'eapon, 'S'hield or just 'L'eave? ")
    if choice == "W":
        weaponDir = os.listdir(".\\weapons")
        weaponList =[x.split('.')[0] for x in weaponDir]

        choice = input("Type the name of the weapon that you want to buy " + str(weaponList) + " ")
        if choice in weaponList:
            text = "\\weapons\\{}.txt".format(choice)
            path = os.getcwd()+text
            file = open(path,'r')
            playerWeapon, attackDamage, weaponPrice = file.readlines()
            file.close()
            playerWeapon = playerWeapon.strip()
            attackDamage = attackDamage.strip()
            weaponPrice = weaponPrice.strip()
            playerGold = int(playerGold)
            weaponPrice = int(weaponPrice)
            if playerGold >= weaponPrice:
                checkout = input("You have " + str(playerGold).strip() + " gold. Do you want to buy this " + choice + " for " + str(weaponPrice).strip() + "? 'Y'es or 'N'o: ")
                if checkout == "Y":
                    playerGold -= weaponPrice
                    playerWeapon = choice
                else:
                    print(choice + " not bought!")
            else:
                print("The " + choice + " is " + str(weaponPrice) + " gold. You have " + str(playerGold) + ".")
            town()
        else:
            print("Weapon not found!")
            town()
        print("This will work soon and access the player's inventory!")
    elif choice == "S":
        print("This will work soon and access the player's inventory!")
    else:
        leave()

def hole():
    print("You're at a hole! (2,0)")
    leave()

def forrest():
    print("You're at the forrest! (1,2)")
    fight(1)
    leave()

def deepForrest():
    print("You're at the deep forrest! (1,2)")
    fight(2)
    leave()

def location(x, y):

    if x == 0 and y == 0:
        home()
    elif x == 1 and y == 0:
        town()
    elif x == 2 and y == 0:
        hole()
    elif x == 1 and y == 2:
        forrest()
    else:
        print("Place not defined yet (" + str(x).strip() + ",", str(y).strip() +")")
        leave()

def goNorth():
    global x, y
    if y != 0:
        y -= 1
        location(x, y)
    else:
        print("You can't go any further North!")
        location(x, y)

def goSouth():
    global x, y
    if y != 2:
        y += 1
        location(x, y)
    else:
        print("You can't go any further South!")
        location(x, y)

def goEast():
    global x, y
    if x != 2:
        x += 1
        location(x, y)
    else:
        print("You can't go any further East!")
        location(x, y)

def goWest():
    global x, y
    if x != 0:
        x -= 1
        location(x, y)
    else:
        print("You can't go any further West!")
        location(x, y)

location(x, y)