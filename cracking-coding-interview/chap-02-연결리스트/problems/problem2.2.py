"""
2.2
단방향 연결리스트가 주어졌을 때 뒤에서 k 번째 원소를 찾는 알괴즘을 구현하라
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node(%s)" % self.data


class LinkedList(object):
    def __init__(self, val: int):
        self.length = 1
        self.head = Node(None)
        node = Node(val)
        self.head.next = node
        self.tail = node

    def add(self, val: int):
        self.length += 1
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def __iter__(self):
        cur = self.head.next
        while cur is not None:
            yield cur
            cur = cur.next

    def __len__(self):
        return self.length


def find_k_elements(linked_list: LinkedList, k: int) -> Node:
    res = len(linked_list) - k
    cur = linked_list.head.next
    count = 0
    while cur is not None:
        if count == res:
            return cur
        cur = cur.next
        count += 1
    return None


if __name__ == '__main__':
    linked_list = LinkedList(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(5)
    linked_list.add(6)
    linked_list.add(7)
    linked_list.add(8)

    for node in linked_list:
        print(node)

    print("")
    # 6
    print(find_k_elements(linked_list, 3))
