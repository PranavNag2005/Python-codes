s1=input("enter a string ")
s2=input("enter a second string ")
result=""
b=""
for i in range(len(s1)):
    if s1[i] not in s2:
        result+=s1[i]
for i in range(len(s2)):
    if s2[i] not in s1:
        b+=s2[i]
print(result+b)