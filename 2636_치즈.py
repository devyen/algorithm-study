import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    picks = [0] + list(map(int, input().split()))

    rst = n
    check = [0] * (n+1)
    for i in range(1, n+1):
        if not check[i]:
            # 한 텀
            students = []
            while True:
                if check[i]:  # 이미 확인한 번호면 pass
                    break
                students.append(i)
                check[i] = 1
                i = picks[i]
                if i in students:
                    cut = students.index(i)
                    rst -= len(students[cut:])
                    break

    print(rst)