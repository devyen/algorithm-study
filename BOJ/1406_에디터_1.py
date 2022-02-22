import sys
input = sys.stdin.readline

chars = list(input().rstrip())  # 리스트
cursor = len(chars)

m = int(input())
for _ in range(m):
    tmp = input().split()
    command = tmp[0]

    if command == 'L' and cursor != 0:
        cursor -= 1
    elif command == 'D' and cursor != len(chars):
        cursor += 1
    elif command == 'B' and cursor != 0:
        # chars = chars[:cursor-1] + chars[cursor:]
        chars.pop(cursor-1)
        cursor -= 1
    elif command == 'P':
        back = []
        if cursor != len(chars):
            back = chars[cursor:]
        chars = chars[:cursor] + [tmp[1]] + back
        cursor += 1

sys.stdout.writelines(''.join(chars))
