from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]* n for _ in range(n)]
        x_start, x_end, y_start, y_end, num = 0, n - 1, 0, n - 1, 1

        while x_start <= x_end and y_start <= y_end:
            for x in range(x_start, x_end + 1): # move right
                matrix[y_start][x] = num
                num += 1
            for y in range(y_start + 1, y_end): # move down
                matrix[y][x_end] = num
                num += 1
            for x in reversed(range(x_start, x_end + 1)): # move left
                if y_start < y_end:
                    matrix[y_end][x] = num
                    num += 1
            for y in reversed(range(y_start + 1, y_end)): # move up
                if x_start < x_end:
                    matrix[y][x_start] = num
                    num += 1
            x_start, x_end, y_start, y_end = x_start + 1, x_end - 1, y_start + 1, y_end - 1

        return matrix
