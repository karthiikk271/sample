class student():
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("name",self.name)
        print("Emp_id",self.emp_id)
        print("salary",self.salary)
s2= student("shri",101,22222)
s2.display()