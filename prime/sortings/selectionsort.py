def selection(arr):
    n=len(arr)
    for i in range(n):
        index=i
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                index=j
        arr[i],arr[index]=arr[index],arr[i]
size=int(input("enter a size of array:"))
arr=[]
for i in range(size):
    a=int(input("enter a number"))
    arr.append(a)
result=selection(arr)
print(arr)