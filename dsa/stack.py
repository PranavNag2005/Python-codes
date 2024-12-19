class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack+=[item]
        print(f"pushed:{item}")
    
    def pop(self):
        if self.is_empty():
            print("stack is empty cannot pop ")
            return None
        item=self.stack[-1]
        self.stack=self.stack[:-1]
        print(f"popped: {item}")
        # return item
    def peek(self):
        if self.is_empty():
            print("stack is empty ")
            return None
        print(f"peek is {self.stack[-1]}")
        # return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        count=0
        for _ in self.stack:
            count+=1
        print(f"size : {count}")
        return count 
    def arr(self):
        return self.stack


s=Stack()
s.push(2)
s.push(22)
s.push(231)
s.push(1233)
s.pop()
s.pop()
s.peek()
print(s.arr())
print(s.is_empty())
s.size()