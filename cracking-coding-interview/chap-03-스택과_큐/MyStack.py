"""
링크드리스트로 구현한 스택
"""


class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next_ = None


class MyStack(object):

    def __init__(self):
        self.top = None

    def push(self, item):
        if self.top is None:
            self.top = StackNode(item)
        else:
            # 추가할 노드를 생성하고
            node = StackNode(item)
            # 추가할 노드의 다음 번 노드를 현재 top 이 가르키는 것으로 바꿔치기 한다.
            # 이러면 추가한 노드의 다음번 노드가 바로 이전에 추가했던 노드가 된다.
            node.next_ = self.top
            # 그리고 top 을 (제일 최근에 추가한) 노드로 바꾼다.
            self.top = node
        return item

    def peek(self):
        return self.top.data

    def pop(self):
        node = self.top
        self.top = node.next_
        return node.data

    def print(self):
        dummy = self.top
        while dummy is not None:
            print(dummy.data, "->", end=" ")
            dummy = dummy.next_
        print("")


if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    stack = MyStack()
    for i in sample:
        stack.push(i)

    # 5
    stack.print()
    print("Pop:", stack.pop())
    # 4
    stack.print()
    print("Pop:", stack.pop())
    # 3
    stack.print()
    print("Peek:", stack.peek())
    # 3
    stack.print()
    print("Pop:", stack.pop())
    stack.print()
    print("Push:", stack.push(7))
    # 7
    stack.print()
    print("Peek:", stack.peek())

    # result
    stack.print()
