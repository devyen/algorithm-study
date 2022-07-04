import sys

sys.stdin = open('input.txt')


def inorder_traverse(i):
    if i <= n:
        inorder_traverse(i * 2)  # left
        words.append(tree[i])
        inorder_traverse(i * 2 + 1)  # right


for tc in range(1, 11):
    n = int(input())
    tree = ['']  # 0번 인덱스는 빈 문자열
    for i in range(1, n + 1):
        data = input().split()
        tree += data[1]

    words = []
    inorder_traverse(1)

    print(f'#{tc} ', *words, sep='')