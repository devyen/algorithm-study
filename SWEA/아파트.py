def is_same(row):
    for col in range(5):
        if apart[0][col] != apart[row][col]:
            return 0

    return 1


def get_same(arr):
    target = arr[0]
    n = len(arr)

    for r in range(1, n):
        flag = 0
        for c in range(n):
            if arr[r][c] != target[c]:
                flag = 1
                break


apart = [
    [3,2,1,7,9],
    [1,2,3,4,5],
    [3,2,1,7,9],
    [4,3,2,1,0],
    [3,2,1,6,9],
    [3,2,1,7,9],
]

