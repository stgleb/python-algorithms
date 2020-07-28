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


def list_overlap_no_cycle(head1, head2):
    while head1.next:
        head1 = head1.next

    while head2.next:
        head2 = head2.next

    return head1 is head2


def list_overlap_cycle(head1, head2):
    start1, start2 = has_cycle(head1), has_cycle(head2)
    if start1 is None and start2 is None:
        return list_overlap_no_cycle(head1, head2)

    if start1 is None or start2 is None:
        return False

    tmp = start1
    while tmp:
        tmp = tmp.next
        if tmp is start2 or tmp is start1:
            break

    if tmp is start2:
        return True

    return False


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
    n17.next = n15

    n21 = Node(21)
    n22 = Node(22)
    n23 = Node(23)
    n24 = Node(24)
    n21.next = n22
    n22.next = n23
    n23.next = n24

    print(list_overlap_cycle(n11, n21))
    n24.next = n14
    print(list_overlap_cycle(n11, n21))
