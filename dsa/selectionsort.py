def selection(arr):
    n=len(arr)
    for i in range(n):
        minindex=i
        for j in range(i+1,n):
            if arr[j]<arr[minindex]:
                minindex = j
        arr[i],arr[minindex] =arr[minindex], arr[i]
    return arr

size=int(input("enter the size of the array "))
arr=[]
for i in range(size):
    s=int(input("enter the elements into the array "))
    arr.append(s)
print(selection(arr))