def solution(num_teams, remote_tasks, office_tasks, employees):

    info = []  # 인덱스: 사원번호, 값: [팀번호, 재택유무]
    for i in range(len(employees)):
        tmp = employees[i].split()
        team_num = int(tmp[0])
        tasks = tmp[1:]
        info.append([team_num, 1])  # [팀번호, 재택유무]
        for task in tasks:
            if task in office_tasks:
                # 출근
                info[i][1] = 0

    # 출근자 없는 팀 체크
    team_check = [0] * (num_teams+1)  # 1번부터 시작이므로
    for person in info:
        if person[1] == 0:  # 출근하면
            team_check[person[0]] = 1

    all_remote_teams = [i for i in range(1, len(team_check)) if team_check[i] == 0]
    # all_remote_teams = []
    # for i in range(1, len(team_check)):
    #     if team_check[i] == 0:
    #         all_remote_teams.append(i)

    for team in all_remote_teams:
        for person in info:
            if person[0] == team:
                person[1] = 0
                break

    # 재택 직원 구하기
    answer = [i + 1 for i in range(len(info)) if info[i][1] == 1]
    # answer = []
    # for i in range(len(info)):
    #     if info[i][1] == 1:
    #         answer.append(i+1)

    return answer