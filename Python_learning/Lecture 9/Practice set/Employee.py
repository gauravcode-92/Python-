class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print("Role is:",self.role)
        print("Department is:",self.department)
        print("Salary is:",self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Name of the employee is:", name)
        print("Age of the employee is:", age)

emp1=Employee("acoountant","account",90000)
emp1.showDetails()

eng1=Engineer("Gaurav",22)
        
        
