# s=input("enter the name ")
# dici={}
# for i in s:
#     if i not in dici:
#         dici[i]=1
#     else:
#         dici[i]+=1
# print(dici)

# def count(s):
#     dici={}
#     for i in s:
#         if i not in dici:
#             dici[i]=1
#         else:
#             dici[i]+=1
#     for key,value in dici.items():
#         print(f"{key}:{value}")
# s=input("enter the string to count ")
# print(count(s))

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def b(start,end):
    ar=[]
    for i in range(start,end+1):
        if prime(i):
            ar.append(i)
    return ar                     
print(b(10,20))
