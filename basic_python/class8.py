# Decorators
# a function that modifies the behavior of another function

# def decorator_function(original_function):
#     print(original_function)
#     print("Decorator executed before {}".format(original_function.__name__))
#     def wrapper_function():
#         print("Wrapper executed before {}".format(original_function.__name__))
#     print("Decorator executed after {}".format(original_function.__name__))
#     return wrapper_function
    

# @decorator_function #== decorator_function(display())
# def display(a):
#     print("Display function executed")

# display(2)


# def repeat(n):
#     def decorator_function(original_function):
#         def wrapper_function(*args):
#             for i in range(n):
#                 original_function(*args)
#         return wrapper_function
#     return decorator_function

# @repeat(3)
# def display(a):
#     print("Display function executed", a)

# display(2)

#recursion
# two part > base case, recursive case


# def sum_list(numbers):
#     if len(numbers) == 1:
#         return numbers[0] #base case
#     else:
#         return numbers[0] + sum_list(numbers[1:]) #recursive case
    # step1
    #     len = 5
    #     else > 1 + sum_list([2, 3, 4, 5]) > 15
    #     step2
    #         len = 4
    #         else > 2 + sum_list([3, 4, 5]) > 14
    #         step3
    #             len = 3
    #             else > 3 + sum_list([4, 5]) > 12
    #             step4   
    #                 len = 2
    #                 else > 4 + sum_list([5]) > 9    
    #                     step5
    #                     len = 1
    #                     if > return 5

# list1 = [1, 2, 3, 4, 5]
# print(sum_list(list1)) # 15 

# list2 = [1, 2, 3, 4, 5]    

# def sum(list2):
#     sum = 0
#     for i in list2:
#         sum += i
#     return sum

# print(sum(list2)) # 15


# n!
# 1!=1
# 5! = 5*  4*3*2*1
# 5! = 5*4!
# 4! = 4* 3*2*1
# 3! = 3*2*1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    # step1
    #     n = 5
    #     else > 5 * factorial(4) > 24
    #     step2
    #         n = 4
    #         else > 4 * factorial(3) > 6
    #         step3
    #             n = 3
    #             else > 3 * factorial(2) > 2
    #             step4
    #                 n = 2
    #                 else > 2 * factorial(1) > 1
    #                 step5
    #                     n = 1
    #                     if > return 1
print(factorial(5)) # 120