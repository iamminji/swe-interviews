"""
LinkedList 를 python 으로 구현

add 는 O(1)
delete 는 O(n)

Node의 data 는 unique 한 integer 라고 가정한다.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node(%s)" % self.data


class LinkedList(object):
    def __init__(self, val: int):
        self.head = Node(None)
        node = Node(val)
        self.head.next = node
        self.tail = node

    def add(self, val: int):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def delete(self, val: int):
        prev, cur = self.head, self.head.next
        while cur is not None:
            if cur.data == val:
                prev.next = cur.next
                return
            cur = cur.next
            prev = prev.next

    def __iter__(self):
        cur = self.head.next
        while cur is not None:
            yield cur
            cur = cur.next


if __name__ == '__main__':
    nodes = [2, 3, 4]
    ll = LinkedList(1)
    for n in nodes:
        ll.add(n)

    # 1, 2, 3, 4
    for n in ll:
        print(n)

    print("")
    # 1, 3, 4
    ll.delete(2)
    for n in ll:
        print(n)

    print("")
    ll.delete(1)
    # 3, 4
    for n in ll:
        print(n)

    print("")
    ll.add(1)
    # 3, 4, 1
    for n in ll:
        print(n)
