# function fn(arr):
#     left = 0
#     right = arr.length - 1

#     while left < right:
#         Do some logic here depending on the problem
#         Do some more logic here to decide on one of the following:
#             1. left++
#             2. right--
#             3. Both left++ and right--


s=input("enter the string ").lower()
left=0
right=len(s)-1
ispalindrme=False
while left<right:
    if s[left]==s[right]:
        ispalindrme=True
    else:
        ispalindrme=False
    left+=1
    right-=1
print(ispalindrme)


