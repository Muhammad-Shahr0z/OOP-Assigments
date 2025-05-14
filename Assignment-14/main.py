# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



class Employee:

    def __init__(self,name):
        self.name =name
    def show(self):
        print(f"Employee Name : {self.name}")

class Department:
    def __init__(self , employee:Employee):
        self.employee=employee #Aggregation
        self.employee.show()

emp = Employee("Shahroz")
emp1 = Department(emp)
        
