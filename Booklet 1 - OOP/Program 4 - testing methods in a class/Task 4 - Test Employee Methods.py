# Task 4 - Test Employee Methods
# Complete this file to write comprehensive tests for Employee class methods

import datetime 
from datetime import date 
class Employee: 
    def __init__(self, employee_id, first_name, last_name, salary, department, position, hire_date):
        self.id = int(employee_id)
        self.firstname = str(first_name)
        self.lastname = str(last_name)
        self.salary = float(salary)
        self.department = str(department)
        self.position = str(position)
        self.hiredate = str(hire_date)

    def get_full_name(self): 
        return self.firstname , self.lastname

    def get_annual_salary(self):
        return self.salary

    def calculate_monthly_salary(self):
        monthly_salary = self.salary/12
        return monthly_salary 

    def apply_raise(self, raise_percentage):
        raise_percentage = float(input("by how much would you like to raise the salary (%)"))
        while raise_percentage < 0 or raise_percentage > 100:
            print("error, please re-enter raise percentage")
            raise_percentage = float(input("by how much would you like to raise the salary (%)"))
        new_salary = self.salary * float(1 + (raise_percentage/100))
        self.salary = new_salary
        return new_salary

    def get_employment_info(self):
        info = str(self.firstname + "," + self.lastname + "," + str(self.id) + "," + str(self.salary) + "," + self.department + "," + self.position + "," + self.hiredate)
        return info

    def years_employed(self):
        from datetime import date 
        today = str(date.today())
        years = int(today[2:4]) - int(self.hiredate[6:8])
        return years 


    
item1 = Employee("01", "A", "H", "3000", "IT", "Head", "26/08/26")
name = item1.get_full_name()
print(name)
month = item1.calculate_monthly_salary()
print(month)
new_salary = item1.apply_raise(15)
info = item1.get_employment_info()
print(info)
years = item1.years_employed()
print(years)
