def add():
    '''adding of two numbers'''  
    global a,b#global variables we can access this from outside as global keyword is present
    a=int(input("enter a value "))
    b=int(input("enter b value "))
    print("addition of two numbers",a+b)
def sub():
    print("subtraction of two numbers",a-b)
add()
sub()
#when we declare varibales using of global variable thus we can access that variables any where in the function and outside of the function also
print("usage of doc strings",add.__doc__)