import numpy, pandas, random
rows, cols = (10,10) #define the number of rows and columns in the 2-D Array
Game = [[" " for i in range(cols+1)] for j in range(rows+1)] #Create the empty 2-D Array using a nested loop. Note the use of +1 to account for 0th element.

#used to set a specific element in an array
for i in range(6): 
    empty = False
    Game[random.randint(1,10)][random.randint(1,10)]
    if Game[random.randint(1,10)][random.randint(1,10)] == Game[random.randint(1,10)][random.randint(1,10)]: 
      Game[random.randint(1,10)][random.randint(1,10)] 
    Game[random.randint(1,10)][random.randint(1,10)] = "R"

Game[random.randint(1,10)][random.randint(1,10)] = "P"



#the following sections of code use numpy and pandas imported modules to ease display of 2-D Arrays.
rowHeaders = ["1","2","3","4","5","6", "7", "8","9","10"] #creates the row headers for the display
colHeaders = ["1","2","3","4","5","6", "7", "8","9","10"] # creates the column headers for the display
dispGame = numpy.array(Game)
dispGame = pandas.DataFrame(dispGame[1:,1:], columns = colHeaders, index = rowHeaders)
dispGame.columns.name = ""
print("Game")
print (dispGame)



