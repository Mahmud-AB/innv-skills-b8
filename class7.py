#error handling
# 1. prevent crash
# 2. handle error gracefully
# 3. help debugging

#syntax error,name error, type error, index error, indentation error, value error, keyerror, iOerror, zeroDivision error, 
# print("hello")
# try:
#     exec("if True print('True')")#syntax error
# except SyntaxError:
#     print("aaaaa")
#     print("Synta Error:")

# print("After syntax error")
# try:
#     a #name error
# except NameError:
#     print("aaaaa")
#     print("Name Error:")
# print("After name error")
# try:
#     list1 = [1,2,3]
#     print(list1[4]) #index error
#     "hello" + 1 #type error
# except (TypeError, IndexError) as e:
#     print("aaaaa")
#     print("Type Error:")
#     print(f"Error Message:{str(e)}")
# except TypeError:
#     print("aaaaa")
#     print("Type Error:")
# except IndexError:
#     print("aaaaa")
#     print("Index Error:")

# list1 = [1,2,3]
# print(list1[4]) #index error


# for i in range(5):
#     print(i)
#  print(i)
#  print(i+1)
# print(i) #indentation error
# import traceback
# try:
#     print(1/0) #zeroDivision error
# except Exception as e:
#     print("aaaaa")
#     print("Zero Division Error:")
#     tb = traceback.format_exc()
#     print(tb)
#     print(f"Error Message:{str(e)}")
# else:
#     print("No error occurred")
# finally:
#     print("This will always execute")


# File handling -> open, read, write

#mode
# r -> read, w -> write, a -> append, x -> exclusive creation, b -> binary, t -> text, + -> read and write
# file_data = open("test_file.txt", "r")
# print(file_data.read())
# print(file_data.read(5))
# print(file_data.readline())
# print(file_data.readline())
# print(file_data.readline())
# print(file_data.readlines())

# f = open("test_file.txt", "a")
# f.write("Hello World1\n")
# f = open("test_file.txt", "w")
# f.write("Hello World\n")

# with open("test_file.txt", "rb") as f:
#     # print("first",f.tell())
#     # print(f.readline())
#     # print("after first read",f.tell())
#     # seek(offset, whence=0) #0-start,1-current,2-end
#     # print(f.read(5)), #0-start,1-current,2-end
#     print(f.seek(-2,2)), #1- current position,0-start,2-end
#     print("after seek 0",f.readline())
#     print("after seek 0",f.tell())

# with open("image.jpeg", "rb") as f:
#     data = f.read()
#     print(data)