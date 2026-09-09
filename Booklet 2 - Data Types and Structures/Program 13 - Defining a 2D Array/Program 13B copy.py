# import numpy, pandas, random 
# rows, cols = (10,10) #define the number of rows and columns in the 2-D Array
# Game = [[" " for i in range(cols+1)] for j in range(rows+1)] #Create the empty 2-D Array using a nested loop. Note the use of +1 to account for 0th element.



# empty = False 
# randomXP = random.randint(1,10)
# randomYP = random.randint(1,10)
# while empty == False:
#         if Game[randomXP][randomYP] == " ":
#             empty = True 
#             Game[randomXP][randomYP] = "O" 
#         else: 
#             empty = False
#             randomX = random.randint(1,10)
#             randomY = random.randint(1,10)




    



# #the following sections of code use numpy and pandas imported modules to ease display of 2-D Arrays.
# rowHeaders = ["1","2","3","4","5","6", "7", "8","9","10"] #creates the row headers for the display
# colHeaders = ["1","2","3","4","5","6", "7", "8","9","10"] # creates the column headers for the display
# dispGame = numpy.array(Game)
# dispGame = pandas.DataFrame(dispGame[1:,1:], index = rowHeaders,  columns = colHeaders)
# dispGame.columns.name = ""
# print("Game")
# print (dispGame)

# disp2Game = numpy.array(Game)
# disp2Game = pandas.DataFrame(disp2Game[1:,1:], index = rowHeaders,  columns = colHeaders)
# disp2Game.columns.name = ""
# Game[5][5] = "T"
# print(disp2Game)



import numpy, pandas, random 
rows, cols = (1,10) #define the number of rows and columns in the 2-D Array
Game = [[" " for i in range(cols+1)] for j in range(rows+1)] #Create the empty 2-D Array using a nested loop. Note the use of +1 to account for 0th element.




def DisplayGame():
    rowHeaders = ["1"] #creates the row headers for the display
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
    DisplayGame()
    return playerY, playerX



def robotMove(robotX, robotY, playerX, playerY):
        Game[robotY][robotX] = "R"
        print("robot pos is", robotY, robotX)
        if robotX - playerX < 0: 
             robotX = robotX + 1 #working
             print("new pso should be", robotY, robotX)
             Game[robotY][robotX] = "R"
robotX = 1
robotY = 1
playerY = 1
playerX = 10 
for i in range(10):
    playerX, playerY = move(playerX, playerY)
    robotMove(robotX, robotY, playerX, playerY)





