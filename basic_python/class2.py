#condition
# if,if else,nested if else, if elif

#structure
# if condition:
#     statement
# else:
#     statement

# age = 18
# nid = False
# if age >= 18 and nid == True:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

#nested if else
# marks = 68
# if marks >= 80:
#     print("A+")
# else:
#     if marks >= 70:
#         print("A")
#     else:
#         if marks >= 60:
#             print("B")
#         else:
#             if marks >= 50:
#                 print("C")
#             else:
#                 if marks >= 40:
#                     print("D")
#                 else:
#                     print("Fail")

#if elif
# marks = 68
# if marks >= 80 :
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("B")
# elif marks >= 50:
#     print("C")
# elif marks >= 40:
#     print("D")
# elif marks < 40:
#     print("Fail")

#ternary condition
#structure
# value_if_true if condition else value_if_false
# age = 18
# nid = False
# print("You are eligible to vote") if age >= 18 and nid == True else print("You are not eligible to vote")

# marks = 68
# print("A+") if marks >= 80 else print("A") if marks >= 70 else print("B") if marks >= 60 else print("C") if marks >= 50 else print("D") if marks >= 40 else print("Fail")

# marks = 68
# print("A+") if marks >= 80 elif marks >= 70 print("A") elif marks >= 60 print("B") elif marks >= 50 print("C") elif marks >= 40 print("D") elif marks < 40 print("Fail")

########loops
# for loop, while loop
# for loop structure
# for variable in iterable:
#     statement

# for i in range(1,11,2):
#     #range structure range(start,stop,step)
#     #inital start = 0,step = 1,stop = n-1
#     print(i)
# var = "abcd"
# for i in var:
#     print(i)

#while
# variable
# while condition:
#     statement
#     increment/decrement

# x = 1
# while x <= 10:
#     print(x)
#     x += 1

# var = "abcd"
# x = 0
# print(len(var))
# while (len(var) != x):
#     print(var[x])
#     x += 1

#step 1: x = 0, len(var) = 4, 0 != 4, print(var[0]) = a, x = 1
#step 2: x = 1, len(var) = 4, 1 != 4, print(var[1]) = b, x = 2
#step 3: x = 2, len(var) = 4, 2 != 4, print(var[2]) = c, x = 3
#step 4: x = 3, len(var) = 4, 3 != 4, print(var[3]) = d, x = 4

#break, continue
# for i in range(1,11,2):
#     if i == 5:
#         break
#     print(i)

# for i in range(1,11,2):
#     if i == 5 or i == 7:
#         continue
#     print(i)


