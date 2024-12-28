
nums=list(map(int,input().split(" ")))
target=8
def sums(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
s=sums(nums,target)
print(s)