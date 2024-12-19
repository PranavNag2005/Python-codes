def quick(arr):
        if len(arr)<=1:
                return arr
        pivot=arr[len(arr)//2]
        left=[x for x in arr if x < pivot]
        middle=[x for x in arr if x==pivot ]
        right=[x for x in arr if x>pivot]
        return quick(left)+middle+quick(right)
size=int(input("enter size:"))
arr=[]
for i in range(size):
        a=int(input("enter a number:"))
        arr.append(a)
result=quick(arr)
print(result)