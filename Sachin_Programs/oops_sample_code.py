# class Person:  # Parent class, Base class
#     def __init__(self, first_name, age1):
#         self.first_name = first_name
#         self.age = age1
#
#     def display(self):
#         print("Parent class method called")
#         print("Name:", self.first_name)
#         print("Age:", self.first_name)
#
#
# class Employee(Person): # Child class, Derived class
#     def __init__(self, name, age, dept, salary):  #dunder methods internal use
#         super().__init__(name, age)
#         self.dept = dept
#         self.salry = salary
#
#
#
#     # def display(self):  #instance method
#     #     print("Child method called")
#     #
#     #     print(f"Dept:{self.dept} and Salary: {self.salry} ")  #python3.6 >
#     #     # print("Dept:{2} and Salary: {1} ".format(self.salry,self.dept))
#     #     # print("Dept:%d
#
#
# e = Employee("Rohan", 21, "mech", 16000)
# e.display()
#
#
#
from mro_example import Point
p1 = Point(5,6)
p2 = Point(10,20)
print(p1+p2)