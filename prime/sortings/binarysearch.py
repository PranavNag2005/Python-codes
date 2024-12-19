def binary(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if(arr[mid]==target):
            return mid
        elif arr[mid]<target:
            return mid+1
        else:
            return mid-1
    return-1
size=int(input("enter a size:"))
arr=[]
for i in range(size):
    a=int(input("enter element into array:"))
    arr.append(a)
target=int(input("enter target number:"))
result=binary(arr,target)
if result!=-1:
    print("element is found at index",result)
else:
    print("element not found")