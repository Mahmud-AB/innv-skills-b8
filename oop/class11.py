#inheritance struucture > is a relationship
# class Base:
#     pass

# class Derived(Base):
#     pass

# class Animal: # > Base Class
#     def __init__(self):
#         self.name = "Animal"
#         self.age = 0

#     def speak(self):
#         print("Print from Animal class")
    
# class Human(Animal): # Derived Class > Human is an animal
#     def __init__(self):
#         super().__init__()
#         base_name = self.name
#         self.name = "Human"
#         print(f"Base class name: {base_name}")

# human_obj = Human()

# human_obj.speak()

#types of inheritance
# 1. Single Inheritance > 1 base,1 derived
# class Book:
#     def __init__(self,title):
#         print('second')
#         self.title = title
    
#     def get_info(self):
#         print(self.title,self.file_size)
    
# class EBook(Book): # Single Inheritance
#     def __init__(self, title, file_size):
#         print('first')
#         super().__init__(title)
#         self.file_size = file_size
    
#     def get_file_size(self):
#         return self.file_size
    
# ebook = EBook("Python Programming", "2MB")
# ebook.get_info()

# 2. Multiple Inheritance > 2 or more base,1 derived
# class Shareable:
#     def share(self):
#         return "Sharing content"
    
# class Commentable:
#     def comment(self):
#         return "Commenting on content"
    
# class Post(Shareable, Commentable):
#     def __init__(self, content):
#         self.content = content
    
#     def display(self):
#         return f"Post content: {self.content}"

# post = Post("Hello, World!")
# print(post.display())
# print(post.share())
# print(post.comment())

# 3. Multilevel Inheritance > 1 base, 1 derived, 1 or more derived
class User:
    def __init__(self, username):
        self.username = username
    
    def login(self):
        return f"{self.username} logged in"
    
class WRITER(User):
    def __init__(self, username):
        super().__init__(username)
    
    def write(self):
        return f"{self.username} is writing"

class PREMIUM_WRITER(WRITER):
    def __init__(self, username):
        super().__init__(username)
    
    def premium_features(self):
        return f"{self.username} has premium features"

premium_writer = PREMIUM_WRITER("premium_john_doe")
print(premium_writer.login())
print(premium_writer.write())
print(premium_writer.premium_features())

writer = WRITER("write_jane_doe")
print(writer.login())
print(writer.write())


# 4. Hierarchical Inheritance > 1 base, 2 or more derived
class User:
    def __init__(self, username):
        self.username = username
    
    def login(self):
        return f"{self.username} logged in"
    
class Buyer(User):
    def __init__(self, username):
        super().__init__(username)
    
    def buy(self):
        return f"{self.username} is buying"
    
class Seller(User):
    def __init__(self, username):
        super().__init__(username)
    
    def sell(self):
        return f"{self.username} is selling"
    
buyer = Buyer("buyer_jane_doe")
print(buyer.login())
print(buyer.buy())
seller = Seller("seller_john_doe")
print(seller.login())
print(seller.sell())

# 5. Hybrid Inheritance > Combination of two or more types of inheritance


# class Bird:
#     def __init__(self):
#         self.name = "Bird"

#     def speak(self):
#         return "Some sound"
    
# class Dog:
#     def __init__(self):
#         self.name = "Dog"

#     def speak(self):
#         return "Some sound"



