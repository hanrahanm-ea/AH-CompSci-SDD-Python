# Task 12 - CSV to Fixed Object Array
# Complete this file to read CSV into a fixed-size array of Event objects.
import datetime 
from datetime import date 
class Vehicle: 
    def __init__(self, num_wheels, colour, fuel, seats, roof, maxVel):
        self.num_wheels = int(num_wheels)
        self.colour = str(colour)
        self.fuel = str(fuel)
        self.seats = int(seats)
        self.roof = str(roof)
        self.maxVel = float(maxVel)


    def get_colour(self):
        return self.colour

    def get_maxVel(self):
        return self.maxVel


def populate_array_from_file():
    lines = open("dataFiles/vehicleData.csv").read().splitlines()
    data_lines = lines[1:]
    vehicleArray = [] * len(data_lines)
    for line in data_lines:
        lineSplit = line.split(",")
        currentVehicle = Vehicle(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5]) 
        vehicleArray.append(currentVehicle)
        #print(type(currentVehicle))
    return vehicleArray


    

array = populate_array_from_file() 
colour = array[0].get_colour()
maxVel = array[20].get_maxVel()
print(maxVel)
print(colour)

    