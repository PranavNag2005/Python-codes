class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        a=self.head
        while a.next:
            a=a.next
        a.next=new_node
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_position(self,position,data):
        new_node=Node(data)
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        b=self.head
        for _ in range(position -1):
            if not b:
                print("out of range")
            b=b.next
        if not b:
            print("out ofrange")
            return
        new_node.next=b.next
        b.next=new_node
    def delete_node(self,key):
        a=self.head
        if a and a.data==key:
            self.head=a.next
            a=None
            return
        prev=None
        while a and a.data!=key:
            prev=a
            a=a.next
        if not a:
            print("node not found")
            return
        prev.next=a.next
        a=None
    def print_list(self):
        a=self.head
        while a:
            print(a.data,end="-> ")
            a=a.next
        print("none")
l1=Linkedlist()
l1.insert_end(5)
l1.insert_end(3)
l1.insert_begin(6)
l1.insert_position(2,2)
l1.print_list() 
l1.delete_node(5)
l1.delete_node(3)

l1.print_list()
        
        