class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val


def list_overlap(head1, head2):
    while head1.next:
        head1 = head1.next

    while head2.next:
        head2 = head2.next

    return head1 is head2


if __name__ == "__main__":
    n11 = Node(1)
    n12 = Node(2)
    n13 = Node(3)
    n14 = Node(4)
    n15 = Node(5)
    n16 = Node(6)
    n17 = Node(7)

    n11.next = n12
    n12.next = n13
    n13.next = n14
    n14.next = n15
    n15.next = n16
    n16.next = n17

    n21 = Node(21)
    n22 = Node(22)
    n23 = Node(23)
    n24 = Node(24)
    n21.next = n22
    n22.next = n23
    n23.next = n24

    print(list_overlap(n11, n21))
    n24.next = n14
    print(list_overlap(n11, n21))
