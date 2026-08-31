class Employee: 
    def __init__(self, employee_id, first_name, last_name, salary, department, position, hire_date):
        self.id = int(employee_id)
        self.firstname = str(first_name)
        self.lastname = str(last_name)
        self.salary = float(salary)
        self.department = str(department)
        self.position = str(position)
        self.hiredate = str(hire_date)

def newEmployee():
    employee_id = int(input("what is the employee's ID"))