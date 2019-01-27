class Stack:
    def __init__(self):
        self.items =[]

    def IsEmpty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        counter = len(self.items) - 1
        while counter >= 0:
            print self.items[counter]
            counter -= 1

if __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.print_stack()


    print "pop",s.pop()
    print "peek",s.peek()