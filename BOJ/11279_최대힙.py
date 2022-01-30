import sys
input = sys.stdin.readline

heap = [0]  # 최대힙
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 1:
            print(0)
        else:
            # 루트 출력 & 삭제
            print(heap[1])
            if len(heap) > 2:
                heap[1] = heap.pop()
            else:
                heap.pop()
            # 재정리
            last = len(heap) - 1
            p = 1
            c1, c2 = p * 2, p * 2 + 1
            while c1 <= last:
                if c2 > last:
                    ch = c1
                else:
                    ch = c1 if heap[c1] > heap[c2] else c2

                if heap[p] < heap[ch]:
                    heap[p], heap[ch] = heap[ch], heap[p]
                    p = ch
                else:
                    break
                c1, c2 = p * 2, p * 2 + 1

    else:
        # 삽입
        heap.append(x)
        c = len(heap)-1
        p = c//2
        while heap[c] > heap[p] and p > 0:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c//2