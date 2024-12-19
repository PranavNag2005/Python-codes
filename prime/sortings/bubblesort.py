def bubble(arr):
    n=len(arr)
    for i in range(0,n-1,1):
        for j in range (0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
size=int(input("enter the size: "))
arr=[]
for i in range(size):
    a=int(input("enter anumber:"))
    arr.append(a)
result=bubble(arr)
print(arr)