class Queue:
    def __init__(self,size):
        self.queue=[None] *size
        self.front=self.rear=-1
        self.size=size
    def enqueue(self,item):
        if self.is_full():
            print("queue is full cannot enqueue items")
            return
        if self.front==-1:
            self.front=0
        

        self.rear+=1
        self.queue[self.rear]=item
        print(f"Enqueued item is {item} ")
        

    def dequeue(self):
        if self.isempty():
            print("Queue is empty ")
            return None
        item=self.queue[self.front]
        self.queue[self.front]=None 
        self.front+=1

        if self.front>self.rear:
            self.front=self.rear=-1
        print(f"dequed item is {item}")
        return item

    def peek(self):
        if self.isempty():
            print("queue is empty ")
            return None

        print(f'peek value is {self.queue[self.front]} ')
        return self.queue[self.front]
    def isempty(self):
        return self.front==-1

    def is_full(self):
        return self.rear==self.size-1

    def display(self):
        if self.isempty():
            print("queue is empty ")
            return 
        print(f"items : {self.queue}")

q=Queue(5)

q.enqueue(100)
q.enqueue(10)
q.enqueue(23)
q.enqueue(34)
q.enqueue(444)
q.display()
q.enqueue(3)
q.display()
# q.dequeue()
# q.display()
# q.dequeue()
# q.dequeue()
# q.display()
# q.dequeue()
# q.display()
# q.dequeue()
# q.display()