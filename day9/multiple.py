# when a class can be derived from more than one base class this type of inheritance is called multiple inheritance
class parent1:
    def fun1(self):
        print("the function is in the parent1 class")
class parent2:
    def fun2(self):
        print("this function in the parent2 class")

class parent3(parent1,parent2):
    def child(self):
        print("this function in the combination of parent1,parent2  class")
s=parent3()
s.child()
s.fun2()
s.fun1()