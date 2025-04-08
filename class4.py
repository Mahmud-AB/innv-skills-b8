#string formattting
# name = "John doe"
# age = 25

# str1 = f"My name is {name} and I am {age} years old."
# print(type(str1)) # f-string
# print(f"My name is {name} and I am {age} years old.") # f-string

# # printf("My name is %s and I am %d years old." % (name, age)) # c
# print("My name is {} and I am {} years old.".format(name, age)) # format method

# str1 = "My name is" + name + "and I am" + str(age) + "years old." # concatenation

#escape char
# \n new line
# \t tab space
# \\ backslash
# \',\" single quote,double quote


# \b backspace
# \f form feed
# \r carriage return
# \a bell/alert
# \v vertical tab
# \ooo octal value
# \xhh hexadecimal value

# txt = "my name is \"\\abdullah\""

# print(txt)

# str1 = "            hello world                "
# print(str1)
# print(str1.strip()) # remove leading and trailing spaces lstrip()-left,rstrip()-right

# print("hello".endswith("lo")) # True
# print("hello".startswith("he")) # True
# print("hello".isalnum()) # True
# print("hello".isalpha()) # True
# print("hello".isdigit()) # False

#list
# multi data in single varible
#orderd,mutable,duplicate,mixed data type

# list1 = [1,"A",2.5,True,[1,2,3],(1,2,3),{1,2,3},{"name":"abdullah","age":25}]
# print(type(list1))
# print(type(list1[0]))
# print(type(list1[1]))

#access,slicing - same as string
# print(list1[0])
# print(list1[-1])
# print(list1[1:4])
# print(list1[1:4:2])

#adding
# append,insert,extend
# list1.append("hello")
# print(list1)
# list1.insert(2,"world")
# print(list1)
# list1[3] = "python"
# print(list1)
# list1.extend(3,4,5)
# print(list1)

#remove

# # remove, pop,del
# #pop
# print(list1)
# data = list1.pop(2) # remove by index
# print(list1)
# print(data)
# #remove
# list1.remove("A") # remove by value
# print(list1)

# #del
# del list1[0] # remove by index
# print(list1)

# list1.clear() # remove all elements
# print(list1)

#list inbuilt functions
# list2 = [2,5,1,6,3,8,4,7,10,9]
# list3 = [2,5,1,6,3,8,4,7,10,9]

#sort & reverse
# list2.sort() # ascending order
# list2.reverse()
# print("list2",list2)

# list3.sort(reverse=True) #sort + reverse
# print("list3",list3) # descending order

# print(sum(list2)) # sum of all elements
# print(max(list2)) # max element
# print(min(list2)) # min element
# print(len(list2)) # length of list

#copy
# shallow copy
# list3 = list2
# print("list3",list3)
# list3.append(100)
# print("list2",list2)

#deep copy
# list3 = list2.copy()
# print("list3",list3)
# list3.append(200)
# print("list2",list2)
# print("list3",list3)

#list comprehension
#why list comprehension
# 1.faster performance,2.less code,3.readability
# why faster?
# 1.avoid function call,2.fewer code line, 3.c-level bytecode

# structure
# [statement/expression for item in iterable if condition]

#traditional way
# import time
# start = time.time()

# list2 = []
# for item in range(1,1000000):
#     if item % 2 != 0:
#         list2.append(item)
# # print("traditional",list2)
# print("traditional - time",time.time()-start)

# #list comprehension
# start = time.time()
# odd = [item for item in range(1,1000000) if item % 2 != 0]
# # print("comprehension",odd)
# print("comprehension - time",time.time()-start)