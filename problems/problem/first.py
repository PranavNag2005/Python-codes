def binary(data):
    queue=["1"]
    result=[]
    for i in range(data):
        current=queue.pop(0)
        result.append(current)
        queue.append(current+"0")
        queue.append(current+"1")

    return result
n=int(input("enter the number "))
print(binary(n))