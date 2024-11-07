s=input("Enter the characters ").lower()
v=0
c=0
for i in s:
    if i in ['a','e','i','o','u']:
        v+=1
    else:
        c+=1
    
print("The number of vowels ",v)
print("The number of Consonants ",c)