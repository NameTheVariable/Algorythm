def solution(plans):
    plans.sort(key = lambda x: x[1])

    answer = []
    schedule = []

    for subject, start, playtime in plans:
        hour, min = map(int, start.split(':'))
        start_atoi = 60 * hour + min
        playtime = int(playtime)

        if schedule:
            prev_subject, prev_start, prev_playtime = schedule.pop()
            remain_time = start_atoi - prev_start

            if remain_time < prev_playtime:
                schedule.append((prev_subject, prev_start, prev_playtime-remain_time))
            else:
                answer.append(prev_subject)
                remain_time = remain_time - prev_playtime

                while schedule and remain_time :
                    prev_subject, prev_start, prev_playtime = schedule.pop()

                    if remain_time < prev_playtime:
                        schedule.append((prev_subject, prev_start, prev_playtime-remain_time))
                        break
                    else:
                        answer.append(prev_subject)
                        remain_time = remain_time - prev_playtime

        schedule.append((subject, start_atoi, playtime))

    answer.extend([sub for sub, _, _ in schedule[::-1]])

    return answer