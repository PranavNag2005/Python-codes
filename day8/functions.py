#A function is a block of code used to perform a specific task and can be reused throughtout the program:
#A function is way to break up a program into more managable parts
#functions are divided into two types:
# 1)predefined functions
# 2)userdefined functions

#prefined functions are the functions that are exists in 
''''the python like print(),input(),all()->returns true if all the elements of the
given iterable (list,dict,tuple,set) else fasle 
any()->returns true if any of the elements are of the given iterable (list,dict,tuple,set) else false
ascii functions returns a string containing a printable representation of an object
bin()->It converts an integer to a binary string
bool()->return or convert a value to a boolean value 
chr()->returns a string representing a character whose unicode point is an integer
complex()->creates a complex number 
# It is also known as builtin library functions and also called as standard functions
'''
# userdefined functions are created by the users as per their requirements
'''
functions are used to defined by def keyword
syntax:
def functionname():
    statements

'''
#the other functions are lamda functions,recursive functions

# def even(n):
#     if n%2==0:
#         print("even number ")
#     else:
#         print("odd number ")

# even(35)




# def compare():
#     a=int(input("enter the number "))
#     b=int(input("enter the second number "))
#     if a==b:
#         print("two numbers are equal ")
#     elif a>b:
#         print("a is larger number")
#     else:
#         print("b is larger")
# compare()


#armstrong number 
'''def armstrong():
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
armstrong()'''

#palindrome

'''def palindrome():
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
palindrome()'''

#area of circle
'''
def area():
    pi=3.14
    r=int(input("enter the radius "))
    ans=pi*pow(r,2)
    print("The area of circle is ",ans)
area()
'''
#sum of digits of a number
'''def sumofdigit():
    n=int(input("enter a number "))
    temp=n
    ans=0
    while n>0:
        rem=n%10
        ans+=rem
        n=n//10
    print(f"The sum of digits of a number {temp} is {ans}")
sumofdigit()'''


#vowel or consonat
'''def vowelorconsonant():
    s=input("enter a character ")
    l=['a','e','i','o','u']
    if s in l:
        print("vowel")
    else:
        print("consonant")
vowelorconsonant()'''

#perfect number 
'''
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
perfect()'''