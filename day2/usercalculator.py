n1=float(input("enter the value1 "))
n2=float(input("enter the value2 "))
operator=input("enter the operator (+,-,*,%,/)")


if operator=='+':
        print("The Sum of two numbers is ",n1+n2)
elif operator=='-':
        print("The subtraction of two numbers is ",n1-n2)
elif operator=='*':
        print("The multiplication of two numbers is ",n1*n2)
elif operator=='/':
        if n2==0:
                print("zero divison error")
        else:
                print("The division of two numbers is ",n1/n2)
elif operator=='%':
        print("The Modulo divison of two numbers is ",n1%n2)

else:
    print("You should use proper input to get proper output")
