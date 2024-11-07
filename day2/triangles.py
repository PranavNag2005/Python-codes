side1=int(input("enter the value of side1 "))
side2=int(input("enter the value of side2 "))
side3=int(input("enter the value of side3 "))

if (side1+side2)>side3 and (side2+side3)>side1 and (side3+side1)>side2:
    if side1==side2==side3:
        print("It is an equilateral triangle")
    
    elif side1!=side2 and side2!=side3 and side3!=side1:
        print("It is an scalene triangle")
    
    else:
        print("It is an Isoceles triangle")

else:
    print("sum of two digits is lessthan the third")