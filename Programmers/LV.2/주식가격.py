def solution(prices):

    answer = [0] * len(prices)  # 일단 index에 값이 있어야함

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
