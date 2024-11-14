# # variable_name=function_name(filename,mode,a)
# #The key function working with files in python is the open() function

# There are four different methods for opening a file:
#     r-> read opens a file for reading, if the file does not exist Error
#     a->opens a file for appending ,creates the file it does not exist,if exists it write Data 

#     w->opens a file for writing creates the file if it does not exist 
#     x->create It creates the specified file retuns an error if the files exist

# The read function reads the content of the file 
# readline()->reads the entire line once just one line
# close()->used to close the file 





# s=open("C:\\Users\\qis\\Documents\\file1.txt","r+")
# s.write("welcome to codetantra in collobaration with qiscet")
# content=s.read()
# s.close()

# a=open("welcome.txt",'a')
# a.write("hi hello")
# a.close()

# b=open("welcome.txt",'r+')
# print(b.read())
# b.write("hello I am here once again let start the show")

# print(b.read())
#how to delete a file
'''
tell()->used to show the position
seek()->seek is used to start from firstagain
rename()->this function is used to change the file name
mkdir()->make directory
rmdir()->remove directory
chdir()->change directory
'''
import os
# os.remove("welcome.txt")
# os.rename('s.txt','os.txt')
# os.mkdir("qiscet")
# os.rmdir("qiscet")
import json
# data={"name":"pranav","age":40}
# with open("data.json","w") as file:
#     json.dump(data,file)
# with open("data.json","r")as file:
#     data=json.load(file)
#     print(data)
if os.path.exists("os.txt"):
    with open("os.txt","r")as file:
        print(file.read())
else:
    print("file does not exist")




















