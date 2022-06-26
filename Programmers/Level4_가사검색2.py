'''
idea
1. queries의 키워드들을 접두사/접미사로 분리하기
2. 첫글자/끝글자로 정렬을 한 후 해당 부분만 확인하면 시간을 줄일 수 있을것같음
'''


def solution(words, queries):
    def find_start(letter):
        for i in range(len(words)):
            if words[i][0] == letter:
                return i


    answer = []

    head = tail = []
    for query in queries:
        if query[0] != '?':
            head.append(query)
        else:
            tail.append(query)

    # 접두사 검사
    words.sort()
    head.sort()
    for word in words:
        check = [1]*len(queries)
        for i in len(word):
            if word[i] !=
            for j in len(queries):
                if len(word) != len(queries[i]):
                    check[i] = 0
                if not check[i]:
                    continue


    return answer


result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(result)