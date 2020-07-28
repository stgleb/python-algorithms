class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val


def has_cycle(head):
    fast, slow = head, head

    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            # Find where cycle starts
            slow = head
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
    return None


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n4

    cycle_start = has_cycle(n1)
    if cycle_start:
        print(cycle_start.val)
