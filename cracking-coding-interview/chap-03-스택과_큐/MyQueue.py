"""
링크드리스트로 구현한 큐
"""


class QueueNode(object):

    def __init__(self, data):
        self.data = data
        self.next_ = None


class MyQueue(object):

    def __init__(self):
        self.last = None
        self.first = None

    def add(self, item):

        node = QueueNode(item)

        # 포인터를 first, last 두개 둔다.
        # first 는 가장 오래된 값
        # last 는 가장 최근 값 을 가르키게 한다.
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next_ = node
            self.last = node

    def remove(self):
        # 값을 pop(remove) 할 때는 가장 오래된 값을 꺼낸다.
        node = self.first
        self.first = self.first.next_
        return node.data

    def peek(self):
        return self.first.data

    def is_empty(self):
        return self.first is None

    def print(self):
        dummy = self.first
        while dummy is not None:
            print(dummy.data, "->", end=" ")
            dummy = dummy.next_
        print("")


if __name__ == '__main__':
    sample = [1, 2, 3, 4]
    queue = MyQueue()
    for i in sample:
        queue.add(i)
    queue.print()

    # 1
    print("Remove:", queue.remove())
    queue.print()

    # 2
    print("Remove:", queue.remove())
    queue.print()

    print("Add:", queue.add(7))
    queue.print()

    print("Remove:", queue.remove())
    queue.print()

    print("Remove:", queue.remove())
    queue.print()

    print("Remove:", queue.remove())
    queue.print()
