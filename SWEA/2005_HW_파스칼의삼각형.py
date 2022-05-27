import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')

    N = int(input())

    n = 1
    pascal = []
    while n < N+1:
        if n < 3:
            before_list = [1 for _ in range(n)]
            pascal.append(before_list)

        else:
            new_list = [0] * n
            new_list[0] = 1

            for i in range(1, n-1):
                new_list[i] = before_list[i-1] + before_list[i]

            new_list[n-1] = 1
            pascal.append(new_list)
            before_list = new_list

        n += 1

    for i in range(N):
        print(*pascal[i])