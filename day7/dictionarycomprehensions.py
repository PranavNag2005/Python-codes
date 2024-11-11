#{key_expression: value_expression for item in iterable if condition}

#squares of a number
s={i:i**2 for i in range(1,10)}
print(s)
#cubes of a number 
c={i:i**3 for i in range(1,10)}
print(c)
#converting dictionary into lists and get only keys as output
l=list(s)
print(l)

even_odd = {i: 'even' if i % 2 == 0 else 'odd' for i in range(1, 10)}
print(even_odd)