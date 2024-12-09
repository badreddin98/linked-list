class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                if self.head:
                    self.head.prev = None
                return
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next
        if temp is None:
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Testing Singly Linked List
print("\nTesting Singly Linked List:")
sll = SinglyLinkedList()
sll.insert_at_beginning(3)
sll.insert_at_beginning(2)
sll.insert_at_beginning(1)
sll.insert_at_end(4)
print("Initial list:")
sll.display()
print("After deleting 2:")
sll.delete_node(2)
sll.display()

# Testing Doubly Linked List
print("\nTesting Doubly Linked List:")
dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.insert_at_end(4)
print("Initial list:")
dll.display()
print("After deleting 2:")
dll.delete_node(2)
dll.display()
