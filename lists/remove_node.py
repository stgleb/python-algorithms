class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val


def remove_node(node):
    node.val = node.next.val
    node.next = node.next.next


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

    remove_node(n5)
    head = n1
    while head:
        print(head.val)
        head = head.next

