# n1=float(input("enter the number1"))
# n2=float(input("enter the number2"))

# print("addition of two numbers",n1+n2)

# print("subtraction of two numbers",n1-n2)

# print("divison of two numbers",n1/n2)

# print("modulo of two numbers",n1%n2)

# print("multiplication of two numbers",n1*n2)


# #comparison operators
# print(n1>n2)
# print(n1>=n2)
# print(n1<=n2)
# print(n1<n2)
# print(n1==n2)
# print(n1!=n2)

# # logical operatos

# a=True
# b=False
# print("a and b ",a and b)
# print("a or b ",a or b)

#bitwise operators

# a=5
# b=6

# print("a and b",a&b)
# print("a or b",a |b)
# print("~a", ~a)
# print("a<<1",a<<1)
# print("a>>1",a>>1)

#identity operators

a=10
b=10
c=a
print(" a is c",a is c)
print(" a is not c", a is not c)

# membership operators
li=[1,2,3,4,5,6,7,5]

a=int(input("enter the value to check "))
if True:
    print(a in li,"the number present in the list")
else:
    print(a not in list,"the number not present in the list")