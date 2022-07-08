import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트케이스 수


# 저장된 값이 L < V < R 이려면 중위순회 방식으로 방문하며 숫자를 채우면 된다.
def inorder_traverse(i):
    global cnt

    if i <= n:
        # 왼쪽 방문
        inorder_traverse(i*2)
        # 현재 노드 방문
        tree[i] = cnt
        cnt += 1
        # 오른쪽 방문
        inorder_traverse(i * 2 + 1)


for tc in range(1, T+1):
    n = int(input())

    tree = [0] * (n+1)  # 빈 트리 배열. 0번 인덱스는 비운다.

    # 루트부터 탐색하며 트리 만들기
    cnt = 1
    inorder_traverse(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')
