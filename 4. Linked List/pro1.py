
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def at_item(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_(self):
        while self.head:
            print(self.head.data, end=' --> ')
            self.head = self.head.next


l = LinkedList()
l.at_item(10)
l.at_item(20)
l.at_item(30)
l.at_item(40)
l.at_item(50)

l.print_()