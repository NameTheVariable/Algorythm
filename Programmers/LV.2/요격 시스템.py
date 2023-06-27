def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    s = e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
    # 만약 구긴 s,e 사이에 겹치는 구간이 있다면 그건 미사일 하나로 요격 가능
    # 그건 어떻게 계산하냐, 
    # for i,j in targets:
    #  if targets[m] in targets[n]: 이게 관건인데,
    # targets.sort()
    #   count ++

    return answer