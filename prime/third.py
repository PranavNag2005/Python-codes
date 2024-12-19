n=int(input("enter no of students: "))
m=int(input("enter no of tickets: "))
if n<=m:
    print("booking is available: ")
    print(" remaining available tickets:",m-n)
elif n-m:
    print("remaining members:",n-m)
else:
    print("booking is not available: ")