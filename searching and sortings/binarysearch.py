l=[]
n=int(input("Total number of elements in the list "))
for i in range(1,n+1):
    e=int(input("enter the elements "))
    if len(l)<n:
        l.append(e)
key=int(input("Enter the element to search "))
l.sort()
def binary_search(l,key,n):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif key<l[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
a=binary_search(l,key,n)
if a!=-1:
    print(f"found at {a} Index")
else:
    print("element not found")
        
