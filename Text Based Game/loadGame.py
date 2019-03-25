import os

# Global Variables #
playerName = ""
playerHealth = 0
playerWeapon = ""
playerShield = ""
playerGold = 0
attackDamage = 0
defenseValue = 0

def savePlayer():
    global playerName
    global playerHealth
    global playerWeapon
    global playerShield
    global playerGold
    
    text = "\\gameplay\\playerData.txt"
    path = os.getcwd()+text
    file = open(path,'w')

    playerStats = [playerName.strip(), str(playerHealth).strip(), playerWeapon.strip(), str(playerShield).strip(), str(playerGold).strip()]

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
        global playerName
        global playerHealth
        global playerWeapon
        global playerShield
        global playerGold

        playerName, playerHealth, playerWeapon, playerShield, playerGold = file.readlines()
        print("Name:", playerName + "Health:", playerHealth + "Weapon:", playerWeapon + "Defense:", playerShield + "Gold:", playerGold)
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
    global playerWeapon
    global playerShield
    global attackDamage
    global defenseValue

    playerWeapon = playerWeapon.strip()
    text = "\\weapons\\{}.txt".format(playerWeapon)
    path = os.getcwd()+text
    file = open(path,'r')
    playerWeapon, attackDamage = file.readlines()
    file.close()
    playerWeapon = playerWeapon.strip()
    attackDamage = attackDamage.strip()
    print(playerWeapon, attackDamage)

    playerShield = playerShield.strip()
    text = "\\shields\\{}.txt".format(playerShield)
    path = os.getcwd()+text
    file = open(path,'r')
    playerShield, defenseValue = file.readlines()
    file.close()
    playerShield = playerShield.strip()
    defenseValue = defenseValue.strip()
    print(playerShield, defenseValue)

startGame()