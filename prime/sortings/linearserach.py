# def linear(arr,target):
#     for i in range(len(arr)):
#         if(arr[i]==target):
#             return i
#     return -1
# size=int(input("enter size"))
# arr=[]
# for i in range(size):
#     num=int(input("enter a number:"))
#     arr.append(num)
# target=int(input("enter a element to search: "))
# result=linear(arr,target)
# if result!=-1:
#     print(f"element found at index {result}")
# else:
#     print("element not found ")



n=int(input("enter size of array:"))
a=list(map(int,input("enter a number").split(",")))
if len(a)<=n:
    e=int(input("enter a number to search:"))
    for i in range(len(a)):
        if a[i]==e:
            print("element found at index:",i)
            break
    else:
        print("element not found:")
else:
    print("element out of bound ")    
