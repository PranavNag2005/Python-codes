#dictionary are unordered,changeable,indexed
#It has key value pairs
# dictionary is a collection datatype that stores keyvalue pairs
# each key is unique and you can access or modify 
# values by referencing their corresponding values
#dictionary is mutable and symbol {},seperated by ':'
# keys must be unique and immutable and unrepeatale

di={'name':'pranav','age':30,'profession':'student','city':'Ongole'}
print(di)
for i in di:
    print(di[i])
#adding and updating the dictionary 
di['name']='nag'
print(di)
di.pop("city")
print(di)

for key,value in di.items():
    print(f"{key}:{value}")

#get method
print(di.get('name'))
print(di.get('paper'))#used to give none because paper key not present in the dictionary
print(di.popitem())
print(di)

if "name" in di:
    print("exists")

for key in di.keys():
    print(key)
for i in di.values():
    print(i)


s=di.copy()
print(s)
s['job']='ab'
print(s)
s.update({'name':'pranav'}) #update method by using update method
print(s)
print(s.keys())
print(s.values())
print(s.items())