import numpy, pandas, random 
rows, cols = (10,10) #define the number of rows and columns in the 2-D Array
Game = [[" " for i in range(cols+1)] for j in range(rows+1)] #Create the empty 2-D Array using a nested loop. Note the use of +1 to account for 0th element.

def displayGame():
    rowHeaders = ["1","2","3","4","5","6", "7", "8","9","10"]
    colHeaders = ["1","2","3","4","5","6", "7", "8","9","10"] # creates the column headers for the display
    dispGame = numpy.array(Game)
    dispGame = pandas.DataFrame(dispGame[1:,1:], index = rowHeaders,  columns = colHeaders)
    dispGame.columns.name = ""
    print("Game")
    print (dispGame)

def move(playerY, playerX):
    print( "coords are", playerX, playerY)
    Game[playerX][playerY] = " "
    wasd = str(input("what is your move "))
    if wasd == "w":
        print("move is W")
        playerX = playerX - 1
        while playerX> 10 or playerX < 0: 
                    print("error cannot move this way")
                    wasd = str(input("what is your move "))
    elif wasd == "a":
        playerY = playerY - 1 
        while playerY > 10 or playerY < 0: 
                    print("error cannot move this way")
                    wasd = str(input("what is your move "))
    elif wasd == "s":
        playerX = playerX + 1
        while playerX > 10 or playerX < 0: 
                    print("error cannot move this way")
                    wasd = str(input("what is your move "))
    elif wasd == "d":
        playerY = playerY + 1 
        while playerY > 10 or playerY < 0: 
            print("error cannot move this way")
            wasd = str(input("what is your move "))
    else: 
        print("inelligible movement please re-enter")
        wasd = str(input("what is your move "))
    print("new coords", playerX, playerY)
    Game[playerX][playerY] = "P"
    #displayGame()
    return playerY, playerX


def robotMove(robotX, robotY, playerX, playerY):
    for i in range(len(robotX)):
        Game[robotY[i]][robotX[i]] = " "
        print("robot pos is", robotY, robotX)
    for i in range(len(robotX)):
        if robotY[i] - playerY > 0: 
             robotY[i] = robotY[i] - 1 #working

        # elif robotY[i] - playerY > 0:
        #      robotY[i] = robotY[i] + 1 

        # elif robotX[i] - playerX < 0:
        #      robotY[i] = robotY[i] + 1 

        # elif robotX[i] - playerX > 0:
        #      robotX[i] = robotX[i] + 1 # working 

        # elif robotX[i] == robotY[i]:
        #       robotX[i] = robotX[i] + 1
    for i in range(len(robotX)):
          Game[robotY[i]][robotX[i]] = "R"
    #      if Game[robotY[i]][robotX[i]] == Game[playerY][playerX]:
    #           print("explosion, you have died") 
    #           Game[playerX][playerY] = " "
    #      for i in range(len(robotX)-1):
    #             if robotX[i] == robotX[i+1] and robotY[i] == robotY[i+1]:
    #                print("robots have crashed")
    #                Game[robotX[i]][robotY[i]] = "D"
    # if robotX[i] > 11 or robotX[i] < 0:
    #     print("robot has moved off board")
    # elif robotY[i] > 11 or robotY[i] < 0:
    #     print("robot has moved off board")
    displayGame()
#used to set a specific element in an array
robotX = []
robotY = []
for i in range(1): 
    empty = False 
    randomY = random.randint(1,10)
    randomX = random.randint(1,10)
    while empty == False:
        if Game[randomX][randomY] == " ":
            empty = True 
            Game[randomY][randomX] = "R"
        else: 
            empty = False
            randomX = random.randint(1,10)
            randomY = random.randint(1,10)
    robotX.append(randomX) 
    robotY.append(randomY)



empty = False 
randomXP = random.randint(1,10)
randomYP = random.randint(1,10)
while empty == False:
        if Game[randomXP][randomYP] == " ":
            empty = True 
            Game[randomXP][randomYP] = "P" 
        else: 
            empty = False
            randomX = random.randint(1,10)
            randomY = random.randint(1,10)




    



#the following sections of code use numpy and pandas imported modules to ease display of 2-D Arrays.


displayGame()
for i in range(100):
    randomYP, randomXP = move(randomYP, randomXP)
    robotMove(robotX, robotY, randomXP, randomYP)




