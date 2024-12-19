num=int(input())
exists=False
if num >= 0 and num <= ((2**31)-1):
	for i in range(0,num):
		for j in range(0,num):
			sum=(i**2)+(j**2)
			if(sum == num):
				exists=True
if exists:
	print("True")
else:
	print("False")
