#nested loop
# for i in range(10):
#     print("first",i) #step 1: 0
#     for j in range(3):
#         print("second",j) #step 1: 0,1
#     print("first",i) #step 1: 0
#1
#22
#333
#4444
#55555

# row = 5
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("\n")


#String
# sequence of characters
#'', "", (""" """)multiline string

str1 = 'Hello'
str2 = "Hello"
str3 = """hello
world"""
#properties of string
#1. immutable,2. slicing, 3.indexing, 4. concatenation, 5. repetition

#access
print(str1)
print(str1[2])
print(str1.index('l')) #case sensitive
print(str1.count('l'))
print(str3)
print(str3[1:8:2]) # func same as range

#inbuilt functions

# print(str1.upper())
# print(str3.title())
# print(str3.capitalize())

# print(str3.find('world'))
# print(str3.replace('world','python'))

str4 = str3.split('\n')
c1,*c2 = str3.split('\n')
print(str4)
print(c1,c2)
print(type(str4))
print(type(c1))

print("-".join(str4))
print(c1 + " " + c2[0])
