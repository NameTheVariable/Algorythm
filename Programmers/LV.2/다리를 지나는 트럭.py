from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    index = 0
    count = 0
    bridge_queue = deque()

    for i in range(bridge_length):
        bridge_queue.append(0)

    while True:
        if bridge_queue[0] != 0:
            count += 1

        bridge_queue.popleft()

        if index <= len(truck_weights) - 1 and weight - sum(bridge_queue) - truck_weights[index] >= 0:
            bridge_queue.append(truck_weights[index])
            index += 1
        else:
            bridge_queue.append(0)

        answer += 1
        if count == len(truck_weights):
            break

    return answer
