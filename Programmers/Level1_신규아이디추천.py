def solution(new_id):
    for s in '~!@#$%^&*()=+[{]}:?,<>/':
        new_id = new_id.replace(s, '')
    new_id = new_id.lower()
    i = 0
    flag = 0
    cut = 0
    tmp = ''
    normal = 0
    while i < len(new_id):
        if new_id[i] == '.':
            s = i
            tmp += new_id[normal:s] + '.'
            while new_id[i] == '.':
                i += 1
            normal = i
        i += 1
    print(new_id)
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15].strip('.')
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id


result = solution("...!@BaT#*...y.abcdefghijklm")
print(result)