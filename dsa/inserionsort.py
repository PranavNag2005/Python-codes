def insertion(arr):
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
size=int(input("enter the size of the array "))
arr=[]
for i in range(size):
    s=int(input("enter the elements into the array "))
    arr.append(s)
print(insertion(arr))