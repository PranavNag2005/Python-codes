nums=[1,1,0,1,1,1]
count=0
maxcount=0
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
    else:
       count=0
    maxcount=max(count,maxcount)
print(maxcount)
    
cnt = 0
maxi = 0
for i in range(len(nums)):
    if nums[i] == 1:
        cnt += 1
    else:
        count=0
    maxi = max(count,maxi)
   
print(maxi)


