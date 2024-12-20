s=input("enter a string ")
n=len(s)
a=n//2
if n%2==0:
    print(s[0:a]+s[a:].upper())
else:
    print(s[0:a+1]+s[a+1:].upper())