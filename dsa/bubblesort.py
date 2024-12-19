def bubble(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
size=int(input("enter the size of the array "))
arr=[]
for i in range(size):
    s=int(input("enter the elements into the array "))
    arr.append(s)
result=bubble(arr)
print(result)