from itertools import combinations


def solution(relation):
    answer = 0

    students = []
    for i in range(1, len(relation[0]) + 1):
        students.extend(combinations(range(len(relation)), i))

    unique = []
    for i in students:
        temp = [tuple()]

    return answer
