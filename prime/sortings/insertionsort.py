def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
size=int(input("enter number"))
arr=[]
for i in range(size):
    a=int(input("enter a number"))
    arr.append(a)
result=insertion(arr)
print(arr)