def solution(clothes):
    hashing = {}
    for items in clothes:
        if items[1] in hashing:
            hashing[items[1]] += 1
        else:
            hashing[items[1]] = 1

    combinations = 1
    for i in hashing.values():
        combinations *= (i + 1)
    return combinations - 1
