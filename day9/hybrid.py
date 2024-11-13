# Inheritance  consists of multiple types of inheritance is known as hybrid inheritance
class parent:
    def fun1(self):
        print("the function is in the main class")
class child1(parent):
    def childs(self):
        print("this function in the child1 class")

class child2(child1,parent):
    def child(self):
        print("this function in the child2 class")
s=child2()
s.child()
s.childs()
s.fun1()