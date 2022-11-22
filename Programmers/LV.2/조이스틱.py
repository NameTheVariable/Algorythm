def solution(name):
    answer = 0
    min_move = [min(ord(elements) - 65, 90 - ord(elements) + 1) for elements in name]
    position = 0
    left_key = 1  # 좌 키 눌리는 개수
    right_key = 1  # 우 키가 눌리는 개수
    while True:
        answer += min_move[position]
        min_move[position] = 0

        if sum(min_move) == 0:
            break

        while min_move[position - left_key] == 0:  # 바꿔야 하는 문자가 left_key를 누르지 않아도 될 경우 그냥 left 키 추가
            left_key += 1
        while min_move[position + right_key] == 0:  # 바꿔야 하는 문자가 right_key를 누르지 않아도 될 경우 그냥 right 키 추가
            right_key += 1

        if left_key >= right_key:  # left_key를 눌러야 하는게 더 많으면 right_key가 더 효율적인것
            position += right_key
            answer += right_key
        elif left_key < right_key:  # 아니면 left_key가 더 효율적인 것
            position -= left_key
            answer += left_key

    return answer
