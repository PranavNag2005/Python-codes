s=input("enter a string ")
def reverse(s):
    stack=[]
    for i in s:
        stack.append(i)
    reverse=""
    while stack:
        reverse+=stack.pop()
    return reverse
r=reverse(s)
if r==s:
    print("palindrome ")
else:
    print("not a palindrome ")