from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at END
    def insert_at_end(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t.next is not None:
            t = t.next

        t.next = temp
        temp.prev = t

    # Insert at BEGINNING
    def insert_at_beginning(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    # Insert in MIDDLE (after x)
    def insert_in_middle(self, value, x):
        t = self.head

        while t is not None:
            if t.data == x:
                temp = Node(value)

                temp.next = t.next
                temp.prev = t

                if t.next is not None:
                    t.next.prev = temp

                t.next = temp
                return

            t = t.next

        print(f"{x} not found in list")

    # Delete a node
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        # Delete head
        if self.head.data == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        t = self.head

        while t is not None:
            if t.data == value:
                if t.next:
                    t.next.prev = t.prev
                if t.prev:
                    t.prev.next = t.next
                return
            t = t.next

        print(f"{value} not found")

    # Print list (forward)
    def print_list(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next
        print("None")
