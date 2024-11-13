'''class dog:
    def eat(self):
        print(f"{self.name} was barking")
        print(f"{self.name} was {self.age} old")
d=dog()



d.name="snoofy"
d.age=7
d.eat()'''
#addition of two numbers using oops concept

'''class arithmetic:
    a=int(input("enter the number1 "))
    b=int(input("enter the number 2"))
    def add(self):
        print("addition of two numbers ",self.a+self.b)

a=arithmetic()
a.add()'''
#parameterized constructor
'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("potato",45)
print(p.name)
print(p.age)'''


#non parameterized parameters
class person:
    def __init__(self):
        self.name="nag"
        self.age=56
p1=person()
print(p1.name)
print(p1.age)



