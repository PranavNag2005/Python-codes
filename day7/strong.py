# A Strong Number is a special number where the sum of the factorials of its digits is equal to the number itself.
# For example, the number 145 is a Strong Number because:
# (1! + 4! + 5! = 1 + 24 + 120 = 145),2,40835
n=int(input("enter a number "))
sumoffactorials=0
temp=n
while n>0:
    factorial=1
    rem=n%10
    for i in range(1,rem+1):
        factorial=factorial*i
    sumoffactorials+=factorial
    n=n//10
if temp==sumoffactorials:
    print("It is strong number ")
else:
    print("It is not a strong number ")