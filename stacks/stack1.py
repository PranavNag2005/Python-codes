class stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
        print(f"pushed element is { (element)}")


    def isempty(self):
        return len(self.stack)==0
    
    def pop(self):
        if self.stack.isempty():
            print("stack is empty can't delete")
        
s=stack()
s.push(1)
s.push(2)
print(s.isempty())