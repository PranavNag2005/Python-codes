n=int(input("enter the number "))
temp=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if temp==s:
    print("palindrome number")
else:
    print("Not a palindrome number ")