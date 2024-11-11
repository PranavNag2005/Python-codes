s={i**2 for i in range(1,10)}
print(s)
s={i**3 for i in range(1,10)}
print(s)
even_odd = {i if i % 2 == 0 else 'odd' for i in range(1, 10)}
print(even_odd)