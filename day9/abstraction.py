# Abstraction is one of the important in oops'
# It refers to programming approach by which only the relevant data about an object is 
# exposed and hiding all other details 
# Abstract class can contain both abstract methods and concrete methods 
# The function which has same name inside both parent and child class is called methodoverriding or function overriding

class shape():
    def area(self):
        print("area")
    def perimeter(self):
        print("perimeter")
    def concrete(self):
        print("This is a concrete class ")
class rectangle(shape):
    def area(self):
        width=5
        height=10
        return width*height
    def perimeter(self):
        length=5
        breadth=10
        return 2*(length+breadth)
s=rectangle()
print(s.area())
print(s.perimeter())
s.concrete()
o=shape()
o.concrete()
o.area()