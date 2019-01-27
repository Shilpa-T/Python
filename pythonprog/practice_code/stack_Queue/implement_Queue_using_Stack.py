from stack import Stack
"""
A queue can be implemented using two stacks,stack1 and stack2
"""

class Queue(Stack):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,item):
        self.stack1.push(item)
        #self.stack1.print_stack()

    def dequeue(self):
        #print "size",self.stack2.size()
        #print "size", self.stack1.size()
        if self.stack2.size()== 0:
            while self.stack1.size() > 0:
               self.stack2.push(self.stack1.pop())
                #print self.stack2.print_stack()
        return self.stack2.pop()

    def size(self):
        return self.stack1.size()+self.stack2.size()





if __name__=="__main__":
    s=Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    #s.dequeue()
    print "Dequeue",s.dequeue()
    print "Dequeue", s.dequeue()
   # s.print_queue()
