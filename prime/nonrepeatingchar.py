# a=input()
# def nonrepating(a):
#     dic={}
#     for i in a:
#         if i not in dic:
#             dic[i]=1
#         else:
#             dic[i]+=1
#     for key,value in dic.items():
#         if value==1:
#             print(key)
#             break
#     else:
#         print("not found")
# nonrepating(a)


def no(a):
    for char in a:
        if a.count(char)==1:
            return char
a=input()
res=no(a)
if res:
    print(f"first non repeating : {res}")
else:
    print("not found")