from singly_linked_list import SinglyLinkedList

ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.insert_at_beginning(5)

ll.insert_in_middle(40, 20)

ll.print_list()

ll.delete(20)
ll.print_list()

ll.delete(5)
ll.print_list()

ll.delete(30)
ll.print_list()
