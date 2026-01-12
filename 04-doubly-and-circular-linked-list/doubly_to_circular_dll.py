class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def make_circular_dll(head):
    if not head:
        return None

    temp = head
    while temp.next:
        temp = temp.next

    # connect last to first
    temp.next = head
    head.prev = temp

    return head
