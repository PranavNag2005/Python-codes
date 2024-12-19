s=input()
s1=input()
index=s.find(s1)
if index !=-1:
    print(f"the substring starting at aindex: {index}")
else:
    print(f"the substring not")


if s1 in s:
    print("substring is present")
else:
    print("not present")