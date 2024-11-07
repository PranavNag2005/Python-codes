a=int(input("enter the value of a "))
b=int(input("Enter the value of b "))

print("Before swappping a= ",a)
print("Before swappping b= ",b)

a=a^b
b=a^b
a=a^b
print("AFter swapping a= ",a)

print("AFter swapping b= ",b)
