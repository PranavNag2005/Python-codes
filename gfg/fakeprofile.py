s=input("enter your name ").lower()
l1=[]
count=0
l=['a','e','i','o','u']
for i in s:
    if i not in l and i not in l1:
        l1.append(i)
        count+=1
print(count)
if count%2==0:
    print("SHE!")
else:
    print("HE!")