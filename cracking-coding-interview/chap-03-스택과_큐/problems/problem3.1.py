"""
3.1

Q. 배열 한 개로 스택 세개를 구현하기

A. 리스트를 하나 두고 3 mod 연산으로 구현하였다.
단점은, 리스트 길이가 줄어들지 않고 무한히 늘어난다는 것. 이를 위해 compact 연산을 하나 더 넣었다.
"""


class Stack(object):

    def __init__(self):
        self.list_ = []
        self.index0 = 0
        self.index1 = 1
        self.index2 = 2

    def push(self, num, item):

        if len(self.list_) < self.index0 or len(self.list_) < self.index1 or len(self.list_) < self.index2:
            # 3개씩 아이템을 추가해준다.
            self.list_.append(None)
            self.list_.append(None)
            self.list_.append(None)

        if num == 0:
            self.list_[self.index0] = item
            self.index0 += 3
        elif num == 1:
            self.list_[self.index1] = item
            self.index1 += 3
        else:
            self.list_[self.index2] = item
            self.index2 += 3

    def pop(self, num):
        if num == 0:
            item = self.list_[self.index0 - 3]
            self.list_[self.index0 - 3] = None
            self.index0 -= 3
        elif num == 1:
            item = self.list_[self.index1 - 3]
            self.list_[self.index1 - 3] = None
            self.index1 -= 3
        else:
            item = self.list_[self.index2 - 3]
            self.list_[self.index2 - 3] = None
            self.index2 -= 3
        return item

    def peek(self, num):
        if num == 0:
            return self.list_[self.index0 - 3]
        elif num == 1:
            return self.list_[self.index1 - 3]
        else:
            return self.list_[self.index2 - 3]

    def is_empty(self, num):
        if num == 0:
            return self.index0 == 0
        elif num == 1:
            return self.index1 == 1
        else:
            return self.index2 == 2

    def compact(self):
        while len(self.list_) > self.index2 and self.list_[self.index2] is None:
            self.list_.pop()

    def print(self):
        print(self.list_)


if __name__ == '__main__':
    stack = Stack()
    stack.push(0, 1)
    stack.push(1, 2)
    stack.push(2, 3)
    stack.push(0, 4)
    stack.push(1, 5)
    stack.push(2, 6)
    stack.print()
    print("0:Pop", stack.pop(0))
    print("1:Pop", stack.pop(1))
    print("2:Pop", stack.pop(2))
    stack.print()
    print("0:Pop", stack.pop(0))
    print("2:Pop", stack.pop(2))
    stack.print()
    print(stack.is_empty(0))
    print(stack.is_empty(1))
    print(stack.is_empty(2))
    print("0:Push", stack.push(0, 1))
    print("1:Push", stack.push(1, 100))
    print("1:Push", stack.push(1, 400))
    print("2:Push", stack.push(2, 3))
    stack.print()
    print("1:Peek", stack.peek(1))
    print("0:Pop", stack.pop(0))
    stack.print()
    stack.compact()
    stack.print()
    print("2:Push", stack.push(2, 3))
    print("0:Pop", stack.pop(0))
    print("1:Pop", stack.pop(1))
    print("2:Pop", stack.pop(2))
    stack.print()
