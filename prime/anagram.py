def anagrams(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)
s1=input()
s2=input()
if anagrams(s1,s2):
    print("anagrams")
else:
    print("not a anagrams")