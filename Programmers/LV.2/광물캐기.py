from ast import main


def solution(picks, minerals):
    answer = 0
    for i in range(len(minerals)):
        
        # print(f"{minerals[i]}: {answer}")
        print(f"picks: {picks} | answer: {answer} | step: {i}")
        if picks[0] > 0:
            for _ in range(picks[0]):
                answer += 1
            picks[0] -= 1
        elif picks[0] <= 0 and picks[1] > 0:
            for _ in range(picks[1]):
                if minerals[i] == "diamond":
                    answer += 5
                else:
                    answer += 1
            picks[1] -= 1
        else:
            for _ in range(picks[1]):
                if minerals[i] == "diamond":
                    answer += 25
                elif minerals[i] == "iron":
                    answer += 5
                else:
                    answer += 1
            picks[2] -= 1
    print(answer)
    return answer


pick = [1, 3, 2]
mineral =  ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
if __name__ == "__main__":
    print(pick)
    print(mineral)
    solution(pick, mineral)