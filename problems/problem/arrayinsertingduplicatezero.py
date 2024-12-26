# nums=[1,2,3]
# nums.insert(4,100) #insert at end 
# print(nums)
# nums.insert(2,120) #insert at middle
# print(nums)
# nums.insert(0,1000) #insert at begin
# print(nums)

# arr = [1,0,2,3,0,4,5,0]
# n=len(arr)
# for i in range(len(arr)):
#     if arr[i]==0:
#         arr.insert(i+1,0)
#     i=i+2
# print(arr)
arr = [1, 0, 2, 3, 0, 4, 5, 0]
n = len(arr)
i = 0

while i < n:
    if arr[i] == 0:
        arr.insert(i + 1, 0)
        arr.pop()
        i += 1
    i += 1
    
print(arr)


