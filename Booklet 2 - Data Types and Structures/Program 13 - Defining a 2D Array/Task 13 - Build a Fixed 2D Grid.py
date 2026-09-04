# Task 13 - Build a Fixed 2D Grid
# Complete this file to define and use a fixed-size 2D array.
import numpy
import pandas 
def bookSeat():
   coord = str(input("which seat do you want to sit in (r,c) "))
   col = int(coord[1:2])
   row = int(coord[3:])
   row, col


rows, cols = (13,4) #define the number of rows and columns in the 2-D Array
coach = [[" " for i in range(cols+1)] for j in range(rows+1)] #Create the empty 2-D Array using a nested loop. Note the use of +1 to account for 0th element.

#used to set a specific element in an array
coach[5][3] = "T"
coach[6][3] = "T"
coach[5][4] = "T"
coach[6][4] = "T"
coach[3][2] = "B"
coach[8][4] = "B"
coach[10][1] = "B"



#the following sections of code use numpy and pandas imported modules to ease display of 2-D Arrays.
rowHeaders = ["1","2","3","4","5","6", "7", "8","9","10","11","12","13"] #creates the row headers for the display
colHeaders = ["1","2","3", "4"] # creates the column headers for the display
dispCoach = numpy.array(coach)
dispCoach = pandas.DataFrame(dispCoach[1:,1:], columns = colHeaders, index = rowHeaders)
dispCoach.columns.name = ""
print("coach")
print (dispCoach)



