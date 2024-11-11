#sets are unordered,unindexed
#sets are writted with curly brackets
s={} #if no element present in the set it return the type of dictionary
print(s)
print(type(s))
s1={1,10,20,200,30}
print(type(s1))#type of set
print(s1)
#remove():It is used to remove a specified element 
# and raised an error in the element not found

#discard():same as remove but doesnot raise an error is element not found

s1.add(4)
s1.add(40)
s1.add(41)
s1.add(42)

print(s1)
# s1.remove(100)# as the element 100 was not their in the set is 
# KeyError: 100
# s1.remove(100)
print(s1)
s1.discard(42)
print(s1)


print("--------------------- set operations --------------------------")

set1={1,2,3}
set2={4,5,6,3}

#union of two sets
print("union of two sets ",set1|set2)
print("intersection of two sets ",set1&set2)
print("difference of two sets",set1-set2) #It is used to remove common elements and discard 2nd set
print("symmetric difference between two sets is ",set1^set2) #removes common elements
print("--------------------- set operations completed --------------------------")
issubset=set1.issubset(set2)
print(issubset)
issuperset=set1.issuperset(set2)
print(issuperset)

isdisjoint=set1.isdisjoint(set2)
print(isdisjoint)

s={'a','b',1}
print(type(s),s)