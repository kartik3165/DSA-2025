class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
         
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("null")

def insertTail(head, data):
    new_node = Node(data)

    if not head:
        return new_node

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = new_node
    return head

