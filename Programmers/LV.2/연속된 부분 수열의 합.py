def solution(sequence, k):
    answer = []
    result = [i for i in range(sequence)]
    n = len(sequence)
    limit_sum, end = 0,0
    # sequence에서 합이 k인 것을 만족하는 수열을 찾는다
    # 첫 수열의 길이를 저장한다.
    # 다음 수열의 길이와 첫 수열의 길이를 비교한다.
    # 첫 수열이 짧으면 그게 답이고 아니면 다음 수열을 첫수열로 변경한다.
    # 그 수열의 첫쨰 인덱스와 마지막 인덱스를 반환한다.
    # for element in sequence:
    #   if element[i] + element[i+1] == k
    #       result.append(element[i], element[i+1])
    # answer = result[0].index, result[result.length].index
    for i in n:
        while limit_sum < k and end < n:
            
    answer = result[0].index, result[-1].index
    return answer