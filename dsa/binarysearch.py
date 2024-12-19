def binary(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1


size=int(input("enter the size of the array "))
arr=[]
for i in range(size):
    s=int(input("enter the elements into the array "))
    arr.append(s)
target=int(input("enter the element to search in the array "))
arr.sort()
result=binary(arr,target)
if result!=-1:
    print(f"element found at {result} index ")
else:
    print("element not found in the array ")