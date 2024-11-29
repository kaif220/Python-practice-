# Q6. Create an Employee class with attributes name, salary, and a method to display details.
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_records(self):
        print(f"the name of the employee is : {self.name} \nsalary of employee : {self.salary} per/month")

jobs = employee("kaif" ,50000)
jobs.display_records()