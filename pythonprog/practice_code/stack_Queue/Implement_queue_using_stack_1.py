"""
Implementing queue using 2 stacks
"""
class Queue:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        """
        :type item: int
        :return: nothing
        """
        self.stack1.append(item)

    def dequeue(self):
        """
        :return: item
        """

        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def size(self):
        return len(self.stack1) + len(self.stack2)



q = Queue()
for i in range(5):
    q.enqueue(i)
for i in range(5):
    print "returning data ...", q.dequeue()

#print "len",s.size()


