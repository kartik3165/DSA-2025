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

def add_Kth(head, position, data):
    node = Node(data)

    if position == 1:
        node.next = head
        return node

    curr = head

    for _ in range(position - 2):
        if not curr:
            return head
        curr = curr.next

    node.next = curr.next
    curr.next = node
    return head

def deleteHead(head):
    return head.next if head else None

def deleteTail(head):
    if not head or not head.next:
        return None

    curr = head
    while curr.next.next:
        curr = curr.next

    curr.next = None
    return head

def delete_Kth(head, value):
    if not head:
        return None

    if head.data == value:
        return head.next

    curr = head
    while curr.next and curr.next.data != value:
        curr = curr.next

    if curr.next:
        curr.next = curr.next.next

    return head


if __name__ == "__main__":

    head = None

    for x in [5, 8, 9]:
        head = insertTail(head, x)

    print("Original List:")
    printList(head)

    head = add_Kth(head, 3, 87)
    print("\nAfter inserting 87 at position 2:")
    printList(head)