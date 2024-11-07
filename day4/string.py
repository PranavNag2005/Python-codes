s="qiscet is located at vengamukkapalem"
print(s)
print(len(s))

print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())
print(s.startswith("q"))
print(s.endswith('m'))
print(s.replace("vengamukkapalem","Ongole"))
print(s.count('v'))
ss="    hi and hello world  "
print(ss.strip())#used to remove spaces leading and trailing
print(ss.lstrip())#used to remove left spaces
print(ss.rstrip())#used to remove right spaces
print(s[0:])



a="ongole"
print(a.isalpha())#all alphabets return true else false
print(a.isalnum())#all alphabets and numbers returns true else false
print(a.isupper())
print(a.islower())
print(dir(a))

b=' '
c='5'
print(b.isspace())
print(c.isdigit())
print(c.isnumeric())
print(a.find('e'))
print(a.index('g'))
