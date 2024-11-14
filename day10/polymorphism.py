# The word polymorphism means many forms and in programming it refers to methods/operators/functions with the same name that can be executed on many classes and objects 
#polymorphism can achieve through method overriding and operator overloading
# method overriding: the function name which we declared in the super class is implemented by the sub-class with the same function name 
# operator overloading: with in the class the function was implemented with different parameters and have same function name 


class vehicle():
    def __init__(self,name,model) -> None:
        self.name=name
        self.model=model
    def start(self):
        print("vehicle is started")
class cars(vehicle):
   def start(self):
       print("starting")

class train(vehicle):
    def start(self):
        print("train is starting")
class bus(vehicle):
    def start(self):
        print("bus is starting")

s=train("vandebharat","WAP-7")
m=cars("bmw","abc")
b=bus("apsrtc","ashokleyland")
for i in(s,m,b):
    print(i.name)
    print(i.model)
    i.start()
