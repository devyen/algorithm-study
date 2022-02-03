import sys
input = sys.stdin.readline

queue = []

n = int(input())
for _ in range(n):
    input_list = input().split()
    command = input_list[0]
    if command == 'push':
        queue.append(input_list[1])

    elif command == 'pop':
        if queue:
            print(queue[0])
            queue = queue[1:]
        else:
            print(-1)

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)