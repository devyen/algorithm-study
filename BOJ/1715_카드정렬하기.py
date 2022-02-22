import sys
input = sys.stdin.readline


class CardHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        child = len(self.heap) - 1
        parent = (child - 1) // 2
        while self.heap[child] > self.heap[parent] and parent > -1:
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child = parent
            parent = (child - 1) // 2
        # 자식 순서 정렬
        child1, child2 = (parent + 1) * 2 - 1, (parent + 1) * 2
        if self.heap[child2] > self.heap[child1]:  # 같은 레벨 자식 순서 정렬
            self.heap[child1], self.heap[child2] = self.heap[child2], self.heap[child1]

    def pop(self):
        if len(self.heap) == 0:
            return 0

        else:
            # 루트 출력 & 삭제
            root = self.heap[0]
            if len(self.heap) >= 2:
                self.heap[0] = self.heap.pop()  # 마지막 요소를 루트에 넣는다
            else:  # 길이가 1일땐 pop만 하면 됨
                self.heap.pop()

            # 순서 재정리
            last = len(self.heap) - 1
            parent = 0
            child1, child2 = (parent+1)*2 - 1, (parent+1)*2
            while child1 <= last:
                if child2 > last:
                    change_target = child1
                else:
                    change_target = child1 if heap[child1] > heap[child2] else child2

                if self.heap[parent] > self.heap[change_target]:
                    self.heap[parent], self.heap[change_target] = self.heap[change_target], self.heap[parent]

                    if self.heap[child2] > self.heap[child1]:  # 같은 레벨 자식 순서 정렬렬
                       self.heap[child1], self.heap[child2] = self.heap[child2], self.heap[child1]

                    parent = change_target
                else:
                    break
                child1, child2 = (parent+1)*2 - 1, (parent+1)*2

            return root


heap = CardHeap()

n = int(input())
for _ in range(n):
    heap.push(int(input()))
