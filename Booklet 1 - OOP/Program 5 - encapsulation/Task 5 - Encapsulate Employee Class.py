# Task 5 - Encapsulate Employee Class
# Complete this file to refactor Employee class with proper encapsulation.
# Include one validation example similar to Program 5 by using get_department()
# to check that the stored department is between 6 and 20 characters before returning it.

import datetime 
from datetime import date 
class Employee: 
    def __init__(self, employee_id, first_name, last_name, salary, department, position, hire_date):
        self.__id = int(employee_id)
        self.__firstname = str(first_name)
        self.__lastname = str(last_name)
        self.__salary = float(salary)
        self.__department = str(department)
        self.__position = str(position)
        self.__hiredate = str(hire_date)

    def set_employee_id(self):
        self.__id = int(input("what is the new employee id "))
        if self.__id < 0:
            raise ValueError("id must be a positive integer")
        return self.__id

    def set_first_name(self):
        self.__firstname = input("what is the new employee name ")
        if len(self.__firstname) == 0 or len(self.__firstname) > 50:
            raise ValueError("Name must be present and be less than 50 characters ")

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__firstname

    def get_last_name(self):
        return self.__lastname

    def get_salary(self):
        return self.__salary

    def get_department(self):
        length = len(self.__department)
        if length >=6 and length <=20:    
            return self.__department
        else: 
             raise ValueError("invalid Department")
    
    def get_position(self):
        return self.__position

    def get_hire_date(self):
        return self.__hiredate

    def get_full_name(self): 
        return self.__firstname , self.__lastname

    def get_annual_salary(self):
        return self.__salary

    def calculate_monthly_salary(self):
        monthly_salary = self.__salary/12
        return monthly_salary 

    def apply_raise(self, raise_percentage):
        raise_percentage = float(input("by how much would you like to raise the salary (%)"))
        while raise_percentage < 0 or raise_percentage > 100:
            print("error, please re-enter raise percentage")
            raise_percentage = float(input("by how much would you like to raise the salary (%)"))
        new_salary = self.__salary * float(1 + (raise_percentage/100))
        self.__salary = new_salary
        return new_salary

    def get_employment_info(self):
        info = str(self.__firstname + "," + self.__lastname + "," + str(self.__id) + "," + str(self.__salary) + "," + self.__department + "," + self.__position + "," + self.__hiredate)
        return info

    def years_employed(self):
        from datetime import date 
        today = str(date.today())
        years = int(today[2:4]) - int(self.__hiredate[6:8])
        return years 


    
item1 = Employee("01", "A", "H", "3000", "Computing", "Head", "26/08/26")
id = item1.set_employee_id() 
id = item1.get_id()
print(id)
item1.set_first_name()




#name = item1.get_full_name()department = item1.get_department()print(name)
#month = item1.calculate_monthly_salary()
#print(month)
#new_salary = item1.apply_raise(15)
#info = item1.get_employment_info()
#print(info)
#years = item1.years_employed()
#print(years)

