n=int(input("Enter the number "))
s=0
while n>0:
    rem=n%10
    s=s*10+rem
    n=n//10
print(s)