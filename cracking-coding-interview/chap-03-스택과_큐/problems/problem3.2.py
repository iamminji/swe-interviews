"""
3.2

Q. push, pop, min 연산이 있는 Stack 구현하기.
min 은 Stack 의 가장 최솟값을 리턴해야 한다.  모든 연산은 상수 O(1) 로 동작해야 한다.

A. item 값에 추가할 data 와 item 을 추가할 시점의 stack 의 최솟값을 같이 갖고 있으면 된다.
"""


class MinNode:
    def __init__(self, data, min_):
        self.data = data
        self.min_ = min_


class MinStack(object):
    def __init__(self):
        self.list_ = []

    def push(self, item):
        if len(self.list_) == 0:
            self.list_.append(MinNode(item, item))
        else:
            min_ = min(self.list_[-1].min_, item)
            self.list_.append(MinNode(item, min_))

    def pop(self):
        node = self.list_[-1]
        self.list_.pop()
        return node.data

    def peek(self):
        return self.list_[-1].data

    def min(self):
        node = self.list_[-1]
        return node.min_


if __name__ == '__main__':
    stack = MinStack()
    stack.push(99)
    stack.push(3)
    stack.push(100)
    stack.push(1)

    print("Min:(1)", stack.min())
    print("Pop:(1)", stack.pop())
    print("Min:(3)", stack.min())
    print("Pop:(100)", stack.pop())
    print("Min:(3)", stack.min())
    print("Pop:(3)", stack.pop())
    print("Min:(99)", stack.min())

    print("---stack2---")
    stack2 = MinStack()
    stack2.push(-2)
    stack2.push(0)
    stack2.push(1)

    print(stack2.min())
    print(stack2.peek())
    print(stack2.pop())
    print(stack2.min())
