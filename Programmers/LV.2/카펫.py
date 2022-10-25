def solution(brown, yellow):
    total_count = brown + yellow
    for y in range(2, total_count + 1):
        if (total_count / y) % 1 == 0:
            x = total_count // y
            if x >= y and (2 * x) + (2 * y) == brown + 4:
                return [x, y]
