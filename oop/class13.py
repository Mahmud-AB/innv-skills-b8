#Encapsulation
# Encapsulation is a principle that operate on single block of code to hide the internal state and behavior of that code

#Access Modifiers
# Public: Accessible from anywhere
# Protected: Accessible within the class and its subclasses (indicated by a single underscore)
# Private: Accessible only within the class (indicated by a double underscore)

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # Public attribute
#         self._balance = balance  # Protected attribute
#         self.__transaction_history = []  # Private attribute -> _ClassName__attribute

# account = BankAccount("123456789", 1000)
# print(account.account_number)
# print(account._balance)
# print(account._BankAccount__transaction_history)
# account._balance = 2000
# print(account._balance)


# class BankAccount:
#     def __init__(self,account_number,pin):
#         self.account_number = account_number  # Public attribute
#         self._pin = pin  # Protected attribute

#     def __display_pin(self):
#         return self._pin
    
#     def set_balance(self, balance):
#         self.__balance = balance

#     def get_balance(self, pin):
#         print(pin)
#         print(self.get_pin)
#         if pin == self.get_pin:
#             return self.__balance
#         else:
#             raise ValueError("Incorrect PIN")

#     @property
#     def get_pin(self):
#         return self.__display_pin()
    
# account = BankAccount("123456789","pin1234")
# account2 = BankAccount("987654321","pin124")

# print(account.get_pin)  # Accessing the protected method through the property
# print(account2.get_pin)  # Accessing the protected method through the property

# print(account.account_number)
# # print(account.get_pin)
# account.set_balance(1000)
# print(account.get_balance("pin124"))


#polymorphism
# allows differect class object to be treated as same type of common interface

# sttr = "Hello, World!"
# # inte = 42
# list_obj = [1, 2, 3]
# set_obj = {1, 2, 3}

# print(len(sttr))  # Output: 13
# # print(len(inte))  # Output: 2 (number of digits)
# print(len(set_obj))  # Output: 3

# types of polymorphism:
# 1. overriding - runtime polymorphism -> multiple methods same name diffrent class same parameters
# 2. overloading - compile time polymorphism -> multiple methods same name same class diffrenct parameters

# Method Overriding
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# dog = Dog()
# cat = Cat()

# dog.sound()
# # dog.sound2()
# cat.sound()

# Method Overloading
# class Person:
#     def __init__(self, name,phone_number=None):
#         self.name = name
#         self.phone_number = phone_number
#         print(self.phone_number)

#     def greet(self):
#         return f"Hello, my name is {self.name}"
    
    
# obj = Person("John", "1234567890")
# print(obj.greet())

# obj2 = Person("Jane")
# print(obj2.greet())