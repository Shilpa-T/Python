class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def list_print(self):
        n= self.head
        while n !=None:
            print n.data,'->',
            n=n.next
    

ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.list_print()


