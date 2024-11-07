n=int(input("enter the number "))
ans=0
while n>0:
    rem=n%10
    ans+=rem 
    n=n//10
print("the sum of digis of a number ",ans)
