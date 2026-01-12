class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def make_circular(head):
    if not head:
        return None

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = head  # last node points to head
    return head
