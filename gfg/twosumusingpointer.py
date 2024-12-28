arr=[]
n=int(input("enter the size of the array: "))
for i in range(n):
    arr.append(int(input("enter the elements in the array: ")))
target=int(input("enter the target "))

left=0
right=len(arr)-1
while left<right:
    sum=arr[left]+arr[right]
    if sum==target:
        print(left,right)
        break
    elif sum<target:
        left+=1
    else:
        right-=1
    

# {1,3,4,5,7,10,11,19,20}