def even(n):
    if n%2==0:
        print("even number ")
    else:
        print("odd number ")





def compare():
    a=int(input("enter the number "))
    b=int(input("enter the second number "))
    if a==b:
        print("two numbers are equal ")
    elif a>b:
        print("a is larger number")
    else:
        print("b is larger")



#armstrong number 
def armstrong():
    n=int(input("enter a number "))
    temp=n
    l=len(str(n))
    s=0
    while n>0:
        rem=n%10
        s+=pow(rem,l)
        n=n//10
    if temp==s:
        print("armstrong number ")
    else:
        print("not an armstrong number ")


#palindrome

def palindrome():
    n=input("input a number ")
    temp=n
    s=str(n)
    a=''
    for i in range(len(s)-1,-1,-1):#using s=s*10+r also can do like we done in armstrong
        a=a+s[i]
    if temp==a:
        print("palindrome ")
    else:
        print("not a palindrome ")


#area of circle

def area():
    pi=3.14
    r=int(input("enter the radius "))
    ans=pi*pow(r,2)
    print("The area of circle is ",ans)


def sumofdigit():
    n=int(input("enter a number "))
    temp=n
    ans=0
    while n>0:
        rem=n%10
        ans+=rem
        n=n//10
    print(f"The sum of digits of a number {temp} is {ans}")



#vowel or consonat
def vowelorconsonant():
    s=input("enter a character ")
    l=['a','e','i','o','u']
    if s in l:
        print("vowel")
    else:
        print("consonant")


#perfect number 
def perfect():
    n=int(input("enter the number "))
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        print("perfect number ")
    else:
        print("not a perfect number ")

while True:
    print("1:compare")
    print("2:even")
    print("3:armstrong")
    print("4:palindrome")
    print("5:area of circle")
    print("6:sum of digits")
    print("7:vowel or not ")
    choice=eval(input("enter your choice 1 to 7 other to quit"))
    if choice==1:
        compare()
    elif choice==2:
        even()
    elif choice==3:
        armstrong()
    elif choice==4:
        palindrome()

    elif choice==5:
        area()

    elif choice==6:
        sumofdigit()

    elif choice==7:
        vowelorconsonant()
    else:
        break
