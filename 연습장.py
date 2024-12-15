import sys
input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def top(self):
        if not self.stack:
            print(-1)
        else:
            print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def empty(self):
        if not self.stack:
            print(1)
        else:
            print(0)

    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print(-1)


def main():
    N = int(input())
    stack = Stack()

    for _ in range(N):
        chunk = input().split()
        order = chunk[0]

        if order == "push":
            number = int(chunk[1])
            stack.push(number)
        elif order == "top":
            stack.top()
        elif order == "size":
            stack.size()
        elif order == "empty":
            stack.empty()
        elif order == "pop":
            stack.pop()


if __name__ == "__main__":
    main()
