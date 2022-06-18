import string


def solution(msg):
    dicts = {}
    cnt = 1
    for a in list(string.ascii_uppercase):
        dicts[a] = cnt
        cnt += 1

    answer = []
    i = 0
    while i < len(msg):
        j = i+1
        while dicts.get(msg[i:j]) and j <= len(msg):
            j += 1
        w, new_word = msg[i:j-1], msg[i:j]
        answer.append(dicts[w])
        dicts[new_word] = len(dicts)+1
        i = j-1
    return answer


result = solution('TOBEORNOTTOBEORTOBEORNOT')
print(result)