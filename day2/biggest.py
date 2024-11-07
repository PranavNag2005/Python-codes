n1=int(input("enter the first number "))
n2=int(input("enter the second number "))
n3=int(input("enter the third number "))

if n1>n2 and n1>n3:
    print(n1,"is the biggest number")
elif n2>n1 and n2>n3:
    print(n2,"is the biggest number")

elif n3>n1 and n3>n2:
    print(n3,"is the biggest number")

else:
    print("you need to enter unique numbers")