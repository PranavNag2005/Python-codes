n=int(input("enter the numbers: "))
s=list(map(int,input("enter the elements: ").split(",")))
if len(s)<=n:
    num=int(input("search the element: "))
    for i in range(len(s)):
        if s[i]==num:
            print("element found")
            break
    else:
        print("element not found")
else:
    print("element out of bound")