def solution(files):
    sorted_files = []
    for file in files:
        i = 0
        number = ''
        while i < len(file):
            if file[i].isdigit():
                head = file[:i]
                while i < len(file) and file[i].isdigit():
                    number += file[i]
                    i += 1
                tail = file[i:]
                break
            i += 1
        sorted_files.append((head, number, tail))
    sorted_files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(file) for file in sorted_files]
    return answer


result = solution(["O00321", "O49qcGPHuRLR5FEfoO00321"])
print(result)