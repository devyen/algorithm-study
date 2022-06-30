'''
idea
1. queries의 키워드들을 접두사/접미사로 분리하기
2. 첫글자/끝글자로 정렬을 한 후 해당 부분만 확인하면 시간을 줄일 수 있을것같음
'''


def solution(words, queries):
    answer = [0]*len(queries)
    sorted_queries = sorted(list(enumerate(queries)), key=lambda x: x[1])

    for idx, query in enumerate(queries):
        # query == 'fro??'
        for word in words:
            if len(word) != len(query):
                continue
            i = 0
            flag = 0
            while i < len(word):
                if word[i] != query[i] and query[i] != '?':
                    flag = 1
                    break
                i += 1
            if not flag:
                answer[idx] += 1
    return answer


result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(result)