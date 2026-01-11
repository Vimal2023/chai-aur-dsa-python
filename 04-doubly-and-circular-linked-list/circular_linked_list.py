from node import Node
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
            temp.next = self.head
            return

        t = self.head
        while t.next != self.head:
            t = t.next

        t.next = temp
        temp.next = self.head

    def print_list(self):
        if self.head is None:
            return

        t = self.head
        while True:
            print(t.data, end=" -> ")
            t = t.next
            if t == self.head:
                break
        print("(HEAD)")
