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
    def print_list(self):
        a=self.head
        while a:
            print(a.data,end="-> ")
            a=a.next
        print("none")
l1=Linkedlist()
l1.insert_end(5)
l1.insert_end(3)
l1.print_list()
l1.delete_node(5)
l1.print_list()
        
        