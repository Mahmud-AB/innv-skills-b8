# dict1 = {
#     "key" : "value",
# }
# json - javascript object notation
# json - text format
# dict - data 
#dict characteristics
# # 1. unordered, 
# # 2. value - mutable, can change value of key
# 2.1 key - immutatble,can't use list and dict as key

# dict1 = {
#     "name" : "abdullah",
#     "age" : 25,
#     "is_student" : True,
#     "subjects" : ["math","english"],
#     "address" : {
#         "city" : "Dhaka",
#         "country" : "Bangladesh",
#     },
# }

#access
# print(dict1["subjects"])
# print(type(dict1.keys()))
# print(dict1.values())
# print(dict1.items()) #list of tuples

# for key,value in dict1.items():
#     print(key,value)

# print("city" in dict1["address"])
# print(dict1)

#change
# dict1["full_name"] = "abdullah al mahmud" # add new key value pair
# dict1["age"] = 26 # change value of key
# print(dict1)
# dict1.update({"name":"abdullah al mahmud"}) # change value of key

#remove
# name = dict1.pop("name") # remove by key
# # dict1.popitem() # remove by key
# del dict1["age"] # remove by key
# dict1.clear() # remove all key value pairs

# dict2 = dict1.copy() # copy dict1 to dict2
# dict1.setdefault("name","abdullah") # set default value if key not exist

#tuple
tuple1 = (1,2,3,4,5,6,7,8,9,10)
#tuple characteristics
# 1. ordered,
# 2. immutable, can't change value of tuple
# 3. indexed, can access by index
# 4. allows duplicate values

#access same as list

#update - need to convert it to list
# list1 = list(tuple1) # convert tuple to list
# list1[0] = 10 # same as list
# tuple1 = tuple(list1) # convert list to tuple
# print(tuple1)

#unpack
# tuple3 = (1,2,4,5)
# a,b,c,d = tuple3 # unpacking
# print(a,b,c,d)
# *a,b,c = tuple3 # unpacking
# print("a*",a,b,c)
# a,*b,c = tuple3 # unpacking
# print("b*",a,b,c)
# a,b,*c = tuple3 # unpacking
# print("c*",a,b,c)

# tuple1 = (1,2,3,4,5)
# tuple2 = (6,7,8,9,10)

# tuple3 = tuple1 + tuple2 # concatenation
# print(tuple3)
# print(tuple1 * 2)

#set
#set characteristics
# 1. unordered,unindexed,partially changeable(add,remove)
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {1,3,5,7,9}
# print(set1.symmetric_difference(set2))

# set1.difference,set1.intersection,set1.union,set1.symmetric_difference
# set1.isdisjoint,set1.issubset
# set1,set2 = {1,2,3,4,5}, {4,5,6,7,8}
# set1.isdisjoint(set2) # check if two sets are disjoint