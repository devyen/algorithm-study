def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    for number in numbers:
        if number == 0:
            number = 11

        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            # 거리 비교
            left_d = sum(divmod(abs(number - left), 3))
            right_d = sum(divmod(abs(number - right), 3))
            if left_d > right_d:
                answer += 'R'
                right = number
            elif left_d < right_d:
                answer += 'L'
                left = number
            else:  # 거리가 같을 때
                if hand == 'right':
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number
    return answer


result = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
print(result)