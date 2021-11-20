class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name} and Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, empid, department, salary):
        super().__init__(name, age)
        self.empid = empid
        self.department = department
        self.salary = salary

    def display(self):
        super().display()
        print(f"EmpId: {self.empid} , Department: {self.department}, Salary: {self.salary}")


e = Employee("Rohan", 23, 1500, "Engineering", 75000)
e.display()
print(Employee.mro())