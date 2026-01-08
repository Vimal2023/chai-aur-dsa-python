from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at END
    def insert_at_end(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next

        t1.next = temp

    # Insert at BEGINNING
    def insert_at_beginning(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    # Insert in MIDDLE (after x)
    def insert_in_middle(self, value, x):
        temp = Node(value)
        t1 = self.head

        while t1 is not None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next

        print(f"Value {x} not found in list")

    # Delete a node
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        # Case 1: Delete head
        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print(f"Value {value} not found")

    # Print Linked List
    def print_list(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data, end=" -> ")
            t1 = t1.next
        print("None")
