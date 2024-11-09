n=int(input("enter the number "))
b=len(str(n))  #this is used to convert 
#integer into string and find the length of the number
temp=n
s=0
while n>0:
    r=n%10
    s+=pow(r,b)
    n=n//10
if s==temp:
    print("it is an armstrong number ")
else:
    print("not an armstrong number ")