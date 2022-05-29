# time 길이에 따라 music을 최대 2번까지만 반복하는것
# def solution(m, musicinfos):
#     result = []
#     for musicinfo in musicinfos:
#         s, e, title, music = musicinfo.split(',')
#         time = int(e[-2:]) - int(s[-2:]) + (int(e[:2]) - int(s[:2]))*60
#
#         if time <= len(music):
#             music = music[:time]
#         elif time <= len(music)*2:
#             music +=  music[:time%len(music)]
#         else:
#             music += music
#
#         if m in music:
#             result.append((time, title))
#
#     result.sort()
#     answer = result[0][1]
#     return answer

# in으로 찾기
# def solution(m, musicinfos):
#     result = []
#     for musicinfo in musicinfos:
#         s, e, title, music = musicinfo.split(',')
#         time = int(e[-2:]) - int(s[-2:]) + (int(e[:2]) - int(s[:2]))*60
#
#         if len(music) >= time:
#             music = music[:time]
#         else:
#             music += music*(time//len(music)-1) + music[:time%len(music)]
#
#         if m in music:
#             result.append((time, title))
#
#     result.sort(reverse=True)
#     print(result)
#     answer = result[0][1]
#     return answer

# split
def solution(m, musicinfos):
    change_dic = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}
    result = []
    for musicinfo in musicinfos:
        s, e, title, music = musicinfo.split(',')
        time = int(e[-2:]) - int(s[-2:]) + (int(e[:2]) - int(s[:2]))*60
        for key in change_dic:
            music = music.replace(key, change_dic[key])
            m = m.replace(key, change_dic[key])

        if len(music) >= time:
            music = music[:time]
        else:
            music += music*(time//len(music)-1) + music[:time%len(music)]

        if m in music:
            result.append((time, title))

    result.sort(key=lambda a: a[0], reverse=True)
    if len(result) == 0:
        return '(None)'
    answer = result[0][1]
    return answer


result = solution("ABC", ["13:50,14:20,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD2,ABCDEF","13:50,14:20,WORLD3,ABCDEF"])
print(result)