NUMBERS = {}
num = 0
for name in ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
    NUMBERS[name] = num
    num += 1


def solution(s):
    answer = ''
    word = ''
    for char in s:
        if char.isdecimal():
            answer += str(char)
            continue
        word += char
        if NUMBERS.get(word, -1) != -1:
            answer += str(NUMBERS[word])
            word = ''
    return int(answer)


result = solution('1zerozerofour')
print(result)