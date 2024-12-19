# s=input("enter the message ")
# def nonrepeat(s):
#     dici={}
#     for i in s:
#         if i not in dici:
#             dici[i]=1
#         else:
#             dici[i]+=1
#     for key,value in dici.items():
#         if value==1:
#             print(key)
#             break
#     else:
#         print("not found")
        
# nonrepeat(s)
    


def nonrepeat(s):
    dici = {}
    for i in s:
        if i not in dici:
            dici[i] = 1
        else:
            dici[i] += 1
    non_r = [key for key, value in dici.items() if value == 1]
    print("Non-repeating characters:", non_r)

  
    if non_r:
        print("First non-repeating character:", non_r[0])
    else:
        print("No non-repeating character found")


s = input("Enter the message: ")
nonrepeat(s)
