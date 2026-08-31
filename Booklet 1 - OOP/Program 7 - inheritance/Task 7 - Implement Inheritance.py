# Task 7 - Implement Inheritance
# Complete this file to create a Manager class inheriting from Employee

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

class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, salary, department, position, hire_date, team_size, budget):
        super().__init__(employee_id, first_name, last_name, salary, department, position, hire_date)
        self.__teamsize = int(team_size) #integer
        self.__budget = float(budget) #float

    def get_team_size(self):
        return self.__teamsize

    def set_team_size(self):
        self.__teamsize = int(input("what is the team size "))
        if self.__teamsize < 0: 
            raise ValueError("team must be larger than 0")

    def get_budget(self):
        return self.__budget

    def set_budget(self):
        self.__budget = float(input("what is the new budget "))
        if self.__budget == 0:
            raise ValueError("budget must be higher than 0 ")
    
    def get_budget_by_employee(self):
        if self.__teamsize == 0:
            budget_per== self.__budget
        else:
            budget_per = self.__budget / self.__teamsize
        return budget_per 

    def add_team_member(self):
        yes = str(input("would you like to add a team member (y/n) "))
        while yes != "y" and yes != "n":
            print ("error")
            yes = str(input("would you like to add a team member (y/n) "))
        if yes == "y":
            self.__teamsize = self.__teamsize + 1
            return self.__teamsize
        else: return self.__teamsize

    def remove_team_member(self):
        yes = str(input("would you like to remove a team member (y/n) "))
        while yes != "y" and yes != "n":
            print ("error")
            yes = str(input("would you like to remove a team member (y/n) "))
        if yes == "y":
            self.__teamsize = self.__teamsize - 1
            if self.__teamsize < 0:
                raise ValueError("team size must be above 0 ")
            return self.__teamsize
        else: return self.__teamsize




item1 = Employee("01", "A", "H", "3000", "Computing", "Head", "26/08/18")
item2 = Manager("02", "M", "H", "400000", "Managerial", "Head Manager", "25/02/13", team_size = 5, budget = 3000)

teamsize = item2.get_team_size()
item2.set_team_size()
        
budget = item2.get_budget()
        
item2.set_budget()
        
budget_per_person = item2.get_budget_by_employee()
print(budget_per_person)

teamsize = item2.add_team_member()
print(teamsize)
       
teamsize = item2.remove_team_member()
print(teamsize)

years = item1.years_employed()
print("this employee has been working at the company for",years,"years")







id = item2.set_employee_id() 
id = item2.get_id()
print("the new id is",id)
item2.set_first_name()
name = item2.get_full_name()
department = item2.get_department()
print(name)
month = item2.calculate_monthly_salary()
print("the monthly salary is",month)
new_salary = item2.apply_raise(15)
info = item2.get_employment_info()
print(info)


