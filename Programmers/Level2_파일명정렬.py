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