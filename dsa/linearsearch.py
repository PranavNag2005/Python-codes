def linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1
            
    
size=int(input("enter the size of the array "))
arr=[]
for i in range(size):
    s=int(input("enter the elements into the array "))
    arr.append(s)
target=int(input("enter the element to search in the array "))
result=linear(arr,target)
if result!=-1:
    print(f"Element found at {result} ")
else:
    print("element not found ")