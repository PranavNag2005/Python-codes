#syntax  list_name=[expression for item in iterable if condition]
'''The list comprehension in python is a compact way to 
 generate or transform a list by using a concise 
 readable syntax'''
import math
squares=[x**2 for x in range(1,9)]
print(squares)
cubes=[y**3 for y in range(1,9)]
print(cubes)
sqrt=[math.sqrt(x) for x in range(1,9)]
print(sqrt)
#even or odd using list comprehension
even=[i for i in range(1,150) if i%2==0 ]
odd=[i for i in range(1,12) if i%2==1]
print(even)
print(odd)
even_odd=[i if i%2==0 else 'odd' for i in range(1,10)]
print(even_odd)

str='qiscetislocatedinongole'
vowels=[char for char in str if char in 'aeiou']
print(vowels)

li=['mango','apple','orange','banana','']
length=[len(i) if len(i)>0 else '0' for i in li   ]
print(length)


primes=[x for x in range(1,100) if 
        all(x%j!=0 for j in range(2,int(x**0.5)+1) )]
print(primes)