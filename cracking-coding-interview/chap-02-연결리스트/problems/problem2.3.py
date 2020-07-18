"""
2.3
단방향 연결리스트가 주어졌을 때 중간 (정확히 가운데일 필요는 없다) 에 있는 노드 하나를 삭제하는 알고리즘을 구현하라.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node(%s)" % self.data


class LinkedList(object):
    def __init__(self, val: str):
        self.head = Node(None)
        node = Node(val)
        self.head.next = node
        self.tail = node

    def add(self, val: str):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def __iter__(self):
        cur = self.head.next
        while cur is not None:
            yield cur
            cur = cur.next


# in-memory
def delete_node_from_linked_list(linked_list: LinkedList, node: str) -> LinkedList:
    prev, cur = linked_list.head.next, linked_list.head.next.next
    while cur.next is not None:
        if cur.data == node:
            prev.next = prev.next.next
            break
        cur = cur.next
        prev = prev.next

    return linked_list


if __name__ == '__main__':
    ll = LinkedList("A")
    ll.add("B")
    ll.add("C")
    ll.add("D")
    ll.add("E")

    ans = delete_node_from_linked_list(ll, "C")
    for node in ans:
        print(node)
