import sys

input = sys.stdin.readline

DIRECTION = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

n, M, k = map(int, input().split())
atoms = [list(map(int, input().split())) for _ in range(M)]

for _ in range(k):
    # 이동
    place_dic = {}
    new_atoms = []
    for atom in atoms:
        i, j, m, s, d = atom
        ni, nj = (i+DIRECTION[d][0]*s) % n, (j+DIRECTION[d][1]*s) % n
        ni = n if ni == 0 else ni
        nj = n if nj == 0 else nj
        place_dic[(ni, nj)] = place_dic.get((ni, nj), []) + [[m, s, d]]

    # 합성 & 쪼개기
    for key, val in place_dic.items():
        if len(val) < 2:
            m, s, d = val[0]
            new_atoms.append([key[0], key[1], m, s, d])
            continue
        m_sum = 0
        s_sum = 0
        d_stan = val[0][2] % 2  # 홀수 -> 대각선, 짝수 -> 상하좌우
        d_flag = 0
        for m, s, d in val:
            m_sum += m
            s_sum += s
            if d%2 != d_stan:
                d_flag = 1  # 다름! -> 대각선으로 퍼짐
        # 분할
        nm = m_sum//5
        if nm == 0:  # 질량이 0이면 소멸
            continue
        ns = s_sum//len(val)
        for dir in range(4):
            if d_flag:  # 대각선
                new_atoms.append([key[0], key[1], nm, ns, dir*2+1])
            else:  # 상하좌우
                new_atoms.append([key[0], key[1], nm, ns, dir*2])

    atoms = new_atoms

result = 0
for atom in atoms:
    result += atom[2]

print(result)