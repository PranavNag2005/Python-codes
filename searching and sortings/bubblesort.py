k=[]
t=int(input("Enter the total no of elements "))
for i in range(0,t):
    e=int(input("Enter the element one after one "))
    k.append(e)
print(k)

def bubble_sort(k):
    for i in range(len(k)):
        e=0
        for j in range(0,t-i-1):
            if k[j]>k[j+1]:
                k[j],k[j+1]=k[j+1],k[j]
                e=e+1
    if e==0:
        return k
print(bubble_sort(k))
            
