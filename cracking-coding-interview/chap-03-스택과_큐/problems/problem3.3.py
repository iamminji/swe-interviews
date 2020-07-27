"""
3.3

Q. 스택이 지정된 용량을 초과하면 새로운 스택을 생성한다. 단, push(), pop() 연산 시에는 스택이 하나인 경우와 동일하게 동작해야 한다.
(즉, 스택을 사용하는 입장에선 이 스택이 새로운 스택으로 값을 추가, 반환 하는지 모른다. 스택이 하나일 때와 동일하다.)

A. nested list 로 구현하였다. list 안에 stack 여러개를 두고 마지막 stack 의 인덱스를 pointer 란 변수로 처리하였다.
"""


class SetOfStacks(object):
    def __init__(self):
        # 지정된 용량을 5개로 둔다.
        self.capacity = 5
        self.pointer = -1
        self.stacks = []

    def push(self, item):

        if len(self.stacks) == 0:
            self.pointer = 0
            self.stacks.append([])

        # 지정한 용량을 초과하면 신규 stack 을 생성
        if len(self.stacks[self.pointer]) >= self.capacity:
            self.pointer += 1
            self.stacks.append([])
        self.stacks[self.pointer].append(item)

    def pop(self):
        item = self.stacks[self.pointer].pop()
        # 마지막 stack 이 비어있으면 없애고 pointer 를 감소시킨다.
        if len(self.stacks[self.pointer]) == 0:
            self.stacks.pop()
            self.pointer -= 1
        return item

    def print(self):
        print(self.stacks)


if __name__ == '__main__':
    samples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    stack = SetOfStacks()
    for i in samples:
        stack.push(i)

    stack.print()
    for _ in range(7):
        print(stack.pop())

    stack.print()
    stack.push(100)
    stack.push(101)
    stack.print()
    print(stack.pop())
    print(stack.pop())
    stack.print()
