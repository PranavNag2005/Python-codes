class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insertatbegin(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode

    def insertatend(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=newnode
    def insertatposition(self,position,data):
        newnode=node(data)
        if position==0:
            newnode.next=self.head
            self.head=newnode
            return
        current=self.head
        for i in range(position-1):
            if not current:
                print("out of range")
                return
            current=current.next
        if not current:
                print("out of range")
        newnode.next=current.next
        current.next=newnode

    def print(self):
        current=self.head
        if current is not None:
            while current!=None:
                print(current.data,end="---->")
                current=current.next
            print("none")
        else:
            print("linkedlist is empty")



    def reverse(self):
        prev=None
        current=self.head
        while current:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        self.head=prev
s=Linkedlist()
s.insertatbegin(100)
s.insertatbegin(120)
s.print()
s.insertatend(500)
s.print()
s.insertatposition(0,1000)
s.print()
s.insertatposition(9,0)
s.reverse()
s.print()