n=int(input("enter the number "))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i 
if n==s:
    print(s," is a prefect number ")
else:
    print("Ït is not a perfect number ")
