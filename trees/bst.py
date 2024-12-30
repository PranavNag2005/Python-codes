class bstnode:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value

    def insert(self,data):
        if data<self.value:
            if self.left is None:
                self.left=bstnode(data)
            else:
                self.left.insert(data)
        elif data>self.value:
            if self.right is None:
                self.right=bstnode(data)
            else:
                self.right.insert(data)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value,end="---->")
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.value,end="---->")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value,end="---->")

    def search(self,value):
        if value==self.value:
            return True
        elif value<self.value:
            return self.left.search(value) if self.left else False
        elif value>self.value:
            return self.right.search(value) if self.right else False
        else:
            return False

    def minvaluenode(self):
        current=self
        while current.left:
            current=current.left
        return current.value

    def maxvaluenode(self):
        current=self
        while current.right:
            current=current.right
        return current.value
    def deletenode(self,value):
        if value<self.value:
            if self.left:
                self.left=self.left.deletenode(value)
        elif value>self.value and self.right:
            self.right=self.right.deletenode(value)
        else:
            if not self.left:
                return self.left
            elif not self.right:
                return self.left
            minival=self.right.minvaluenode()
            self.value=minival
            self.right=self.right.deletenode(value)
        return self.value
b=bstnode(100)
b.insert(50)
b.insert(110)
b.insert(45)
b.insert(115)
b.inorder()
print()
b.preorder()
print()
b.postorder()
print()
# print(b.search(100))
# print(b.search(234))
print(b.minvaluenode())
print(b.maxvaluenode())
print(b.deletenode(50))
print(b.preorder())