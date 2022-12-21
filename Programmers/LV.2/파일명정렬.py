def solution(files):
    answer = []
    for parts in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(parts)):  # 문자열 자르기
            if parts[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += parts[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += parts[i]
            else:  # number_check is True & parts[i].isdigit() is False
                tail = parts[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD 우선, NUMBER 차선으로 정렬

    return [''.join(t) for t in answer]  # 원래 형태로 문자열 만들어서 반환
