import sys
input = sys.stdin.readline


class Deque:
    def __init__(self, *args):
        self.data = list(args)

    def push_front(self, x):
        self.data = [x] + self.data

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        if self.data:
            print(self.data[0])
            self.data = self.data[1:]
        else:
            print(-1)

    def pop_back(self):
        if self.data:
            print(self.data[-1])
            self.data = self.data[:-1]
        else:
            print(-1)

    def size(self):
        print(len(self.data))

    def empty(self):
        if self.data:
            print(0)
        else:
            print(1)

    def front(self):
        if self.data:
            print(self.data[0])
        else:
            print(-1)

    def back(self):
        if self.data:
            print(self.data[-1])
        else:
            print(-1)


deque = Deque()

n = int(input())
for _ in range(n):
    input_list = input().split()
    command = input_list[0]

    if command == 'push_front':
        deque.push_front(input_list[1])
    elif command == 'push_back':
        deque.push_back(input_list[1])
    elif command == 'pop_front':
        deque.pop_front()
    elif command == 'pop_back':
        deque.pop_back()
    elif command == 'size':
        deque.size()
    elif command == 'empty':
        deque.empty()
    elif command == 'front':
        deque.front()
    elif command == 'back':
        deque.back()

