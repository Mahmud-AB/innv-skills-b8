# 5. Hybrid Inheritance > Combination of two or more types of inheritance
# class Person: # Base Class
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         return f"Hello, {self.name}"
    
# class Student(Person): #> Single Inheritance
#     def __init__(self, name, student_id):
#         super().__init__(name)
#         self.student_id = student_id
    
#     def study(self):
#         return f"{self.name} is studying"

# class Employee():
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id
    
#     def work(self):
#         return f"{self.name} is working"

# class Intern(Student, Employee): #> Multiple Inheritance
#     def __init__(self, name, student_id, employee_id):
#         Student.__init__(self, name, student_id)
#         Employee.__init__(self, name, employee_id)

#     def intern_info(self):
#         return f"Intern {self.name} with Student ID: {self.student_id} and Employee ID: {self.employee_id}"

#hybrid inheritance structure
# single inheritance > person - student 
# multiple inheritance > student - employee - intern
#not hybrid inheritance structure
# single inheritance > person - student 
# multiple inheritance > teacher - employee - intern

# intern = Intern("Alice", "S123", "E456")
# print(intern.greet())

# Inheritance is a relationship
# Composition has a relationship
# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower

#     def start(self):
#         return "Engine started"
    
# class Car(Engine): # ->  Car is an Engine -> wrong relationship
#     def __init__(self, horsepower, model):
#         super().__init__(horsepower)
#         self.model = model

#     def drive(self):
#         return f"{self.model} is driving with {self.horsepower} horsepower"
    
# car_obj = Car(150, "Toyota")
# print(car_obj.start())

# #composition
# # compistion is a design principle in whichh a class contain instace of another class
# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower

#     def start(self):
#         return "Engine started"
    
# class Car:
#     def __init__(self, model, engine, horsepower):
#         self.model = model
#         self.engine = engine(horsepower)

#     def drive(self):
#         self.engine.start()
#         return f"{self.model} is driving with {self.engine.horsepower} horsepower"
    
# car_obj = Car("Toyota", Engine, 150)
# print(car_obj.drive())

#Encapsulation
# Encapsulation is a principle that operate on single block of code to hide the internal state and behavior of that code

#Access Modifiers
# Public: Accessible from anywhere
# Protected: Accessible within the class and its subclasses (indicated by a single underscore)
# Private: Accessible only within the class (indicated by a double underscore)

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._balance = balance  # Protected attribute
        self.__transaction_history = []  # Private attribute -> _ClassName__attribute

account = BankAccount("123456789", 1000)
print(account.account_number)
print(account._balance)
print(account._BankAccount__transaction_history)