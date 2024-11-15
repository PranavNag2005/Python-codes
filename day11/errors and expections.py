# when an unwanted event occurs which stops the normal flow of 
# the program and which we can handle is known as Exception
# 1)try-> try block is used to handle exceptions 
# 2)except->except block handle the error
# 3)else->else block lets you execute code when there is no error
# 4)finally->finally block lets you execute code whether the result 
# of try and except blocks executed or not 
# syntax:
# try:
#     expression
# except:
#     expression
# else:
#     expression
# finally:
#     expression

# try:
#     x=10/0
# except ZeroDivisionError:
#     print("cannot divide zero")
# #using of raise keyword user can create userdefined exception

# try:
#     n=int(input("enter the positive number "))
#     if n<0:
#         raise ValueError("enter positive value ")
#     print(n)

# except ValueError as e:
#     print("error",e)

