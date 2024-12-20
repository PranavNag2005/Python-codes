# Given a string. the task is to check if 
# the string is symmetrical and palindrome or not.
# A string is said to be symmetrical if both the
# halves of the string are the same and a string
# is said to be a palindrome string if one half 
# of the string is the reverse of the other half 
# or if a string appears the same when read 
# forward or backward

s=input("enter a string ")
n=len(s)
mid=n//2
a=""
for i in s:
    a+=i
if s[0:mid] == s[mid:] and s==a:
    print("symmetrical and palindrome ")
else:
    print("both not ")