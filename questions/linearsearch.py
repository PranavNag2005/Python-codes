n=int(input("enter the size of the array"))
s=list(map(int,input("enter the no").split(",")))
if len(s)<=n:
    element=int(input("enter the element to search"))
    for i in range(len(s)):
        if s[i]==element:
            print("element found at index ",i)
            break
    else:
        print("element not found")
else:
    print("index out of bound")
