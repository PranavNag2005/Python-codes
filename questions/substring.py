s=input("enter the string ")
a=input("enter the sub string ")
def check(s,a):
    index=s.find(a)
    if index!=-1:
        print(f"The substring at index {index}")
    else:
        print("There is no substring present in the string ")
check(s,a)