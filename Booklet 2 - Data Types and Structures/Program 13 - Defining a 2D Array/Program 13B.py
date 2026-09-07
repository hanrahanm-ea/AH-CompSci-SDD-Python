import numpy, pandas, random 
rows, cols = (10,10) #define the number of rows and columns in the 2-D Array
Game = [[" " for i in range(cols+1)] for j in range(rows+1)] #Create the empty 2-D Array using a nested loop. Note the use of +1 to account for 0th element.

def move():
    wasd = str(input("what is your move"))
#used to set a specific element in an array
for i in range(6): 
    empty = False 
    randomX = random.randint(1,10)
    randomY = random.randint(1,10)
    while empty == False:
        if Game[randomX][randomY] == " ":
            empty = True 
            Game[randomX][randomY] = "R"
        else: 
            empty = False
            randomX = random.randint(1,10)
            randomY = random.randint(1,10)



empty = False 
randomXP = random.randint(1,10)
randomYP = random.randint(1,10)
while empty == False:
        if Game[randomXP][randomYP] == " ":
            empty = True 
            Game[randomXP][randomYP] = "P"
            playerX = randomXP
            playerY = randomYP 
        else: 
            empty = False
            randomX = random.randint(1,10)
            randomY = random.randint(1,10)




    



#the following sections of code use numpy and pandas imported modules to ease display of 2-D Arrays.
rowHeaders = ["1","2","3","4","5","6", "7", "8","9","10"] #creates the row headers for the display
colHeaders = ["1","2","3","4","5","6", "7", "8","9","10"] # creates the column headers for the display
dispGame = numpy.array(Game)
dispGame = pandas.DataFrame(dispGame[1:,1:], columns = colHeaders, index = rowHeaders)
dispGame.columns.name = ""
print("Game")
print (dispGame)



