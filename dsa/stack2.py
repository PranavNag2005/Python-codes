class Stack:
    def __init__(self):
        self.stack=[]
    def arr(self):
        print(self.stack)
    def push(self,element):
        self.stack.append(element)
        print(f"pushed element is {element}")
    def isempty(self):
        return len(self.stack)==0
    def pop(self):
        if self.isempty():
            print("stack is empty ")
        else:
            print(self.stack[-1])
            self.stack.pop()
    def size(self):
        c=0
        for i in self.stack:
            c+=1
        print(f"size of the stack is {c}")
s=Stack()
s.push(45)
s.push(34)
s.push(123)
s.arr()
print(s.isempty())
s.size()
s.pop()
s.size()
s.push(100)
print(s.isempty())