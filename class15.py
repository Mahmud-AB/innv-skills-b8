#abstraction
#pros - force to implemets subclass methods, misuse - no misuse of methods, clean polyporphism
#cons of not using - forget to implement, no clean structure, duplicate code
# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):

#     @abstractmethod
#     def authentication(self):
#         """Method to authenticate the payment method."""
#         pass

#     @abstractmethod
#     def process_payment(self, amount):
#         """Method to process the payment."""
#         pass

#     @abstractmethod
#     def refund_payment(self, amount):
#         """Method to refund the payment."""
#         pass

# class CreditCardPayment(PaymentMethod):
#     def authentication(self):
#         print("Authenticating credit card payment...")

#     def process_payment(self, amount):
#         print(f"Processing credit card payment of ${amount:.2f}.")

#     def refund_payment(self, amount):
#         print(f"Refunding credit card payment of ${amount:.2f}.")

# class StripePayment(PaymentMethod):
#     def authentication(self):
#         print("Authenticating Stripe payment...")

#     def process_payment(self, amount):
#         print(f"Processing Stripe payment of ${amount:.2f}.")

#     def refund_payment(self, amount):
#         print(f"Refunding Stripe payment of ${amount:.2f}.")

# class BkashPayment(PaymentMethod):
#     def authentication(self):
#         print("Authenticating Bkash payment...")

#     def process_payment(self, amount):
#         print(f"Processing Bkash payment of ${amount:.2f}.")

#     def refund_payment(self, amount):
#         print(f"Refunding Bkash payment of ${amount:.2f}.")


# credit_card = CreditCardPayment()
# credit_card.authentication()
# credit_card.process_payment(100.00)
# credit_card.refund_payment(100.00)

# stripe = StripePayment()
# stripe.authentication()
# stripe.process_payment(50.00)
# stripe.refund_payment(50.00)

#types of methods
# static,class,instance,abstract

# class Calculator:
#     def __init__(self,name):
#         self.name = name

#     def greet(self): # instance method for all object independent > self is used, can access instance attributes
#         print(f"Welcome to {self.name}!")

#     @staticmethod # static method not for all object but for class > no self, no cls, no instance
#     def add(a,b):
#         return a + b

#     @classmethod # class method for all object independent > cls is used, can access class attributes
#     def find_avg(cls,number1, number2):
#         sum = cls.add(number1, number2)
#         avg = sum / 2
#         print(f"The average is {avg}.")
        
    
# cal_obj = Calculator("Simple Calculator")
# cal_obj.greet()
# cal_obj.find_avg(5, 3)

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
    
#     @classmethod
#     def from_string(cls, book_string):
#         title, author, price = book_string.split(',')
#         return cls(title.strip(), author.strip(), float(price.strip()))
    
# book = Book.from_string("The Great Gatsby, F. Scott Fitzgerald, 10.99")
# print(book.title)  # Output: The Great Gatsby