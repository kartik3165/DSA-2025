class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node # type: ignore
        new_node.prev = temp # type: ignore

    def insert_Kth(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head # type: ignore
            if self.head:
                self.head.prev = new_node # type: ignore
            self.head = new_node
            return 
        
        curr = self.head

        for _ in range(position-2):
            if not curr:
                return
            curr = curr.next
        
        if not curr:
            return 
        
        new_node.next = curr.next
        new_node.prev = curr # type: ignore

        if curr.next:
            curr.next.prev = new_node

        curr.next = new_node # type: ignore

    def deleteHead(self):
        if self.head is None:
            return None
        
        if not self.head.next:
            self.head = None
            return
        
        new_head = self.head.next
        new_head.prev = None
        self.head.next = None
        self.head = new_head

        return new_head
        
    def deleteTail(self):
        if not self.head:
            return None
        
        if not self.head.next:
            self.head = None
            return
        
        temp = self.head
        
        while temp.next:
            temp = temp.next
        new_tail = temp.prev
        new_tail.next = None  # type: ignore
        temp.prev = None

        return new_tail

    def delete_Kth(self,position):
        if not self.head:
            return 
        
        if position == 1:
            self.deleteHead()
            return
    
        curr = self.head

        for _ in range(position - 1):
            if not curr:
                return
            curr = curr.next
        
        if not curr:
            return
        
        if curr.prev:
            curr.prev.next = curr.next
        
        if curr.next:
            curr.next.prev = curr.prev

        return self.head

    def printBackward(self):
        curr = self.head
        while curr.next: # type: ignore
            curr = curr.next # type: ignore

        while curr:
            print(curr.data, end=" -> ")
            curr = curr.prev
        print("Null")

    def printForward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("Null")

if __name__ == "__main__": 

    dll = DoublyLinkedList()

    print("\n--- Insert at end ---")
    dll.insert(3)
    dll.insert(5)
    dll.insert(13)
    dll.insert(2)
    dll.printForward()


    print("\n--- Insert at position 3 (99) ---")
    dll.insert_Kth(99, 3)
    dll.printForward()


    print("\n--- Delete Head ---")
    dll.deleteHead()
    dll.printForward()


    print("\n--- Delete Tail ---")
    dll.deleteTail()
    dll.printForward()


    print("\n--- Delete position 2 ---")
    dll.delete_Kth(2)
    dll.printForward()


    print("\n--- Backward Traversal ---")
    dll.printBackward()