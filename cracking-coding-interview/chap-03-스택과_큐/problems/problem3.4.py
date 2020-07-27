"""
3.4

Q. 스택 두 개로 큐 하나를 구현하라.

A. 스택은 LIFO 이고 큐는 FIFO 이다. 서로 pop 해야 하는 데이터 순서가 정 반대이므로 스택을 거꾸로 다시 넣어준다고 생각하면 된다.
스택을 두 개 쓰면 이 방식이 가능하다.
"""


class Queue(object):

    def __init__(self):
        # stack 은 python list 로 쓴다.
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        # O(1)
        # push 는 stack1 에만 한다.
        self.stack1.append(item)

    def pop(self):
        # O(n)
        if len(self.stack2) == 0:
            # stack1 의 모든 아이템을 reverse 해서 stack1 에 넣는다.
            # stack1 이 LIFO 로 동작함으로 pop 을 해서 다른 스택에 넣어주는 것은, reverse 해서 넣어주는 것과 같다.
            while self.stack1:
                data = self.stack1.pop()
                self.stack2.append(data)

        # pop 은 stack2 에서만 한다.
        item = self.stack2.pop()
        return item

    def peek(self):
        if len(self.stack2) > 0:
            return self.stack2[-1]
        return self.stack1[0]

    def empty(self):
        return len(self.stack2) == 0 and len(self.stack1) == 0


if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    # 1, 2, 2
    print(queue.pop())
    print(queue.peek())
    print(queue.pop())

    queue.push(4)
    queue.push(5)
    queue.push(6)

    # 3, 3, 4, 5
    print(queue.peek())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

    print("----queue2----")
    queue2 = Queue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
