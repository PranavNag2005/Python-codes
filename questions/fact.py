
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        s=1
        for i in range(n,0,-1):
            s=s*i
        return s
            
print(fact(5))