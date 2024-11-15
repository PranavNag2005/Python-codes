# a pacakge contains all the files needed for the module 
# pip install module name 
# pip uninstall package name 
# use the list command to list all the packages installed on your system 
# a lambda function is a small anonymous function that can take any number of arguments but can only have a single or one expression 
# syntax:
# lambda arguments:expression 
# add=lambda a,b:a+b
# print(add(1,2))

# def fun(n):
#     return lambda a:a*n
# my=fun(5)
# print(my(2))
#usage of lambda functions with conditional statements
maxvalue=lambda x,y:x if x>y else y 
print(maxvalue(10,100))

minvalue=lambda x,y: x if x<y else y
print(minvalue(3,4))
print(minvalue(4,-1))