l=[]
n=int(input("Total number of elements in the list "))
for i in range(1,n+1):
    e=int(input("enter the elements "))
    if len(l)<n:
        l.append(e)
key=int(input("Enter the element to search "))
def linear_search(l,key):
    for i in range(0,len(l)):
        if l[i]==key:
            return i
    return -1
        
a=linear_search(l,key)
if a!=-1:
    print(f"Element found at {a} index")
else:
    print("Element not found ")
