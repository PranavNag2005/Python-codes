#default arguments 
class addition:
    def add(self,a,b,c):
        return a+b+c
    def sub(self,a,b,c):
        return a-b-c
    def mul(self,a,b,c):
        return a*b*c
class another(addition):
    def nn(self,a,b,c):
        return a-b+c
a=addition()
print(a.add(10,20,30))
print(a.sub(90,50,4))
print(a.mul(10,20,30))
b=another()
print(b.nn(100,200,30))
print(b.add(100,200,30))
print(b.sub(100,200,30))
print(b.mul(100,200,30))