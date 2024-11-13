
'''Recursion is a technique where a function calls itself to solve smaller instances of a problem untill it reaches a base case
-> It is especially useful for problems that can be broken down into similar sub problems like factorial calculation,fibonacci sequence generation,tree traversal
->There are two cases in recursion one 
1)base class:- It stops the recursion when it is satisfied with out it the function would keep calling itself indefinitely
2)recursive class:- The function calls itself with modified arguments to approach the base case gradually
'''
# memory allocation is the disadvantage of Recursion
# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))



# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
    
# print(fibo(10))


# def add(a,b):
#     if a==0:
#         return b 
#     elif b==0:
#         return a 
#     else:
#         return add(a+1,b-1)
# print(add(4,5))



def sub(a,b):
    if a==0:
        return -b
    elif b==0:
        return a
    else:
        return a+sub(a,b)
print(sub(10,20))

#Recursion is two types 
# 1)direct Recursion ->A function which call itself inside of that function
# 2)Indirect Recursion ->A function which call inside the another function


# def mul(a,b):
#     if b==0:
#         return 0
#     elif b>0:
#         return a+mul(a,b-1)
#     else:
#         return mul(-a,-b)
# print(mul(-2,-4))

