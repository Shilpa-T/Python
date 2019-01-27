class Queue:
    def __init__(self):
        self.items =[]

    def IsEmpty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if len(self.items) == 0:
            raise Exception("Queue is empty")
        #self.items.reverse()
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_queue(self):

        counter = len(self.items) - 1
        while counter >= 0:
            print self.items[counter]
            counter -= 1

s=Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.print_queue()
print "Dequeue",s.dequeue()
s.print_queue()

print "len",s.size()
print "isempty",s.IsEmpty()



