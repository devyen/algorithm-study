def solution(sentences, n):

    # 후보 알파벳 별로 얻을 수 있는 점수를 합산해서 고르기..?

    dict = {}
    arr = []
    for sentence in sentences:
        point = len(sentence)
        keys = list(set(sentence.replace(' ', '')))
        flag = 1
        for i in range(len(keys)):
            if keys[i].isupper():
                if flag:
                    keys.append('shift')
                    flag = 0
                point += 1
                keys[i] = keys[i].lower()

        if len(keys) > n:
            continue

        arr.append([keys, point])

        for key in keys:
            dict[key] = dict.get(key, 0) + point

    sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    final = []
    for c in sorted_dict[:n]:
        final.append(c[0])

    answer = 0
    for i in arr:
        a, b = i
        flag = 0
        for t in a:
            if t not in final:
                flag = 1
                break
        if flag:
            break
        answer += b

    return answer


solution(["line in line", "LINE", "in lion"], 5)