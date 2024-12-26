# nums = [-4,-1,0,3,10]
# result=[]
# for i in nums:
#     result.append(i^2)
# print(result)
# result.sort()
# print(result)



arr = [1, 0, 2, 3, 0, 4, 5, 0]
n = len(arr)
i = 0

while i < n:
    if arr[i] == 0:
        arr.insert(i + 1, 0)  # Insert a zero immediately after the current zero
        arr.pop()             # Remove the last element to maintain the original array size
        i += 1                # Increment i to skip the newly inserted zero
    i += 1                    # Move to the next element
    
print(arr)
