#  *args allows you to pass a variable number of 
#  positional arguments to a function. 
#  It collects these arguments into a tuple.
# **kwargs allows you to pass a variable number of
#   keyword arguments to a function. It collects 
#   these arguments into a dictionary.

# class addition():
#     def add(self,*a):
#         return sum(a)
# a=addition()
# print(a.add(1,0,2,3,4,5,2,2,3))

class person:
    def details(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            print(f"name is: {kwargs['name']} and Age is {kwargs['age']}")
        elif 'name' in kwargs:
            print(f"name is: {kwargs['name']}")
        elif 'age' in kwargs:
            print(f"Age is {kwargs['age']}")
        else:
            print("No details provided.")
p=person()
p.details(name="pranav")
p.details(name="nag",age=45)
p.details(age=100)
p.details()