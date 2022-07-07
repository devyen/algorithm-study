import sys

sys.stdin = open('input.txt')

T = 10  # 테스트케이스 수


# 후위순회 방식
def postorder_cal(i):
    if i <= n:
        node = tree[i]
        # 정점이 연산자인 경우 => node[1]이 왼쪽, node[3]이 오른쪽 자식노드
        if len(node) == 3:
            operator = node[0]
            left = postorder_cal(int(node[1]))
            right = postorder_cal(int(node[2]))

            # 연산
            if operator == '+':
                result = left + right
            elif operator == '-':
                result = left - right
            elif operator == '*':
                result = left * right
            elif operator == '/':
                result = left / right

            return result

        # 정점이 수인 경우 -> 그 수를 리턴
        return int(node[0])


for tc in range(1, T+1):
    n = int(input())  # 정점의 개수
    tree = [0] * (n + 1)  # 빈 트리 배열. 0번 인덱스는 비운다.

    for _ in range(n):
        info = input().split()
        # 인풋 처리가 까다롭다
        # 각각 배열을 채울 때 리스트로 값을 넣어줌 ->이유: 정점이 연산자일 경우 자식정보를 포함한 정보를 넣기 위해서.
        tree[int(info[0])] = info[1:]  # tree = [0, ['-', '2', '3'], ['-', '4', '5'], ['10'], ['88'], ['65']]

    # 루트부터 탐색하며 계산
    answer = int(postorder_cal(1))

    print(f'#{tc} {answer}')
