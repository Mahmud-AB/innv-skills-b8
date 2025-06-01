# Class Name Convention:
    # pascalCase > oneTwo > no _
    # Noun,singular
    # not too short or too long
    # not use keywords Class,list

# Key Terminology:
    # __init__
    # self
    # attributes (variables)
        # instance attributes
        # class attributes
    # methods(functions)

# class Django8: #class name
#     # class attributes
#     batch = 8 # class attribute > shared by all objects of the class
#     def __init__(self,n,id): # constructor > automatically called when object created
#         self.name = n  # instance attribute > unique to each object
#         self.id = id    # instance attribute > unique to each object

# # {
# #     "student1" : {
# #         "name": "mahadi hasan",
# #         "id": 12
# #     },
# #     "student2" : {
# #         "name": "ismail habib",
# #         "id": 15
# #     }
# # }
# student1 = Django8("mahadi hasan",12) # object
# student2 = Django8("ismail habib",15) # object

# print(Django8.batch)
# print(student1.name,student1.id)
# print(student2.name,student2.id)
# print(type(student1))


# class Car:
#     wheels = 4 # class attribute > shared by all objects of the class
    
#     def __init__(self,Brand,Model,Year):
#         self.brand = Brand
#         self.model = Model
#         self.year = Year

#     def display(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

# car1 = Car("Toyota", "Model X", 2000)
# print(type(car1))
# print(type(Car("Toyota", "Model X", 2000)))
# car3 = Car("Toyota", "Model X", 2000)
# car2 = Car("BMW", "Model W", 2000)

# car1.display()

# print(car1.__dict__)
# print(car2.__dict__)
# print(Car.__dict__)

# a="10"
# b=20

# c = a + b
# c = (a + b).__add__
# print(c)

class Sum:
    def __init__(self, a):
        self.a = a
    def __add__(self,other):
        if isinstance(self.a, str):
            other.a = str(other.a)
        return Sum(self.a + other.a)
    
digit1 = Sum('10')
digit2 = Sum(20)
sum1 = digit1 + digit2
print(sum1.a)

# __add__ = +
# print(sum1.calculate())  # Output: 30
# print(sum2.calculate())  # Output: 70