"""
2.1
정렬되어 있지 않은 연결리스트가 주어졌을 때 이 리스트에서 중복되는 원소를 제거하는 코드를 작성하라

* 임시 버퍼를 사용하지 않는 방법은?
내 생각엔... 포인터 여러개 둬서, 서로 다른 속도로 진행하다가 같은 값을 발견하면, 더 빨리 진행한 포인터의 prev.next = prev.next.next 로 해서 하면 될 것 같은데.. 구현이 참...
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

    def __iter__(self):
        cur = self.head.next
        while cur is not None:
            yield cur
            cur = cur.next


def remove_duplicates(linked_list: LinkedList) -> LinkedList:
    duplicates = set()
    head = linked_list.head
    prev, cur = head.next, head.next.next

    while cur is not None:
        if cur.data in duplicates:
            prev.next = prev.next.next
            cur = cur.next
            continue
        duplicates.add(cur.data)
        prev = prev.next
        cur = cur.next

    return linked_list


if __name__ == '__main__':
    linked_list = LinkedList(1)
    linked_list.add(3)
    linked_list.add(8)
    linked_list.add(11)
    linked_list.add(8)
    linked_list.add(7)
    linked_list.add(7)
    linked_list.add(100)

    for node in linked_list:
        print(node)

    print("")
    result = remove_duplicates(linked_list)
    for node in result:
        print(node)
