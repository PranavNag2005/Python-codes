l=list()
print(l)   #[]
l=['pizza','burger','sandwitch','samosa']
print(l)  #['pizza', 'burger', 'sandwitch', 'samosa']
print(l[0:]) 
#accessing list items  by slicing ['pizza', 'burger', 'sandwitch', 'samosa']
print(l[2:]) #['sandwitch', 'samosa']
#difference between sort and sorted is sort is used in list and sorted is used in any iterable while sort modifies given the list and sorted modifies the list and keeping the orignial list as it is
l.sort()
print(l)
l.append("dosa")
print(l)
l.pop(2)#need to pass index number
print(l)
l.remove('dosa')#used to pass strings
print(l)
s=[1,2,3]
l.append(s)
print(l)
l.extend(s)
print(l)
l.reverse()
print(l)
s=['sweet','jalebi','kova','halwa','kalakanda','palakova']
print(s)
print("-----------------------------------------")
a=s.copy()
print(a)
a.insert(1,'mysorepak')
print(a)
print("-----------------------------------------")
numbers=[1,2,3,4,5,6,7]
print(numbers.count(5))
numbers.reverse()
print(numbers)
print(len(numbers))
print(min(numbers))

print(max(numbers))
print(sum(numbers))
numbers[5]=125
print(numbers)