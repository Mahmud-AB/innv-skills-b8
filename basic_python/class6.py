#Function
# a block of code that performs a specific task
#1. reusable
#structure
# def function_name(parameters):
#     statematents
# function_name(arguments)

# def add(a,b): # function definition parameters == a,b
#     print(a+b)

# print(add(10,20)) # function call arguments == 10,20
# add(20,30) # function call

#arguments vs parameters
#arguments are the value passed
#parameters are the variable to catch the value


# def add(a,b,c): # give error if c is not passed
#     print(a+b+c)

# def add(a,b,c=2): # c is default parameter
#     print(a+b+c)

# add(10,20) # c = 0
# add(10,20,30) # c = 30
# add(10,20,30,40)

#*args and **kwargs

# def add(*args): # *args is a tuple
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# add(10,20,30,40,50)

# def add(**kwargs): # **kwargs is a dictionary
#     sum = 0
#     for key,value in kwargs.items():
#         print(key,value)
#         sum += value
#     print(sum)

# add(a=10,b=20,c=30,d=40,e=50)
# def add(sum1,*ars,**kwargs):
#     print("inside func",sum1)
#     x = 0 # local variable
#     for i in ars:
#         sum1 += i
#     # for key,value in kwargs.items():
#     #     print(key,value)
#     #     sum += value
#     print("inside func",sum1)
#     return sum1

# sum1 = 20 # global variable
# add(10,20,30,40,50,sum1)
# print("outside func",sum1)

#in built function
# print(sum([1,2,3,4,5])) # sum of list
# max,min,abs
# list1 = [1,2,3,4,5]

# for index,i in enumerate(list1):
#     print(i)
# print("index",index)

#lambda function
# structure
# lambda arguments: statements

# sum1 = lambda a,b: a+b # lambda function
# sum1 = lambda *a,**b: f"args: {a}, kwargs: {b}" # lambda function

# # print(sum1(10,20)) # function call
# print(sum1(10,20,30,40,50,a=10,b=20,c=30,d=40,e=50)) # function call

#map()
# map(function,iterable) func + loop

# def square(x): #func
    # ans = [] # empty list
    # for i in x:
    #     ans.append(i*i)
    # return x*x

# list1 = [1,2,3,4,5] 
# list_ans = square(list1)
# print(list_ans) # function call
# list_ans2 = [] # empty list
# for i in list1: #loop
#     list_ans2.append(square(i))

# print(list_ans2) # function call

# print(tuple(map(square,list1))) # map function