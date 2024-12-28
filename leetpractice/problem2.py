list1=["(","{","["]
list2=[")","}","]"]

def check(mystr):
    stack=[]
    for i  in mystr:
        if i in list1:
            stack.append(i)
        elif i in list2:
            pos=list2.index(i)
            if (len(stack)>0 and list1[pos]==stack[len(stack)-1]):
                stack.pop()
        else:
            return "False"
    if len(stack)==0:
        return True
    else:
        return False
    
print(check("{}([])"))



