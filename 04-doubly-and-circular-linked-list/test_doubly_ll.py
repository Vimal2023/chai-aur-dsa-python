from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

dll.insert_at_beginning(5)

dll.insert_in_middle(50, 20)

dll.print_list()

dll.delete(5)
dll.print_list()

dll.delete(50)
dll.print_list()

dll.delete(40)
dll.print_list()
