from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, col
        for i in range(9):
            col = []
            row = list(filter(lambda x: x.isalnum(), board[i]))
            if len(row) != len(set(row)):  # set을 쓰면 중복값 사라짐
                return False
            for j in range(9):
                col.append(board[j][i])
            col = list(filter(lambda x: x.isalnum(), col))
            if len(col) != len(set(col)):
                return False

        # box
        for i in range(3):
            for j in range(3):
                box = []
                for k in range(3):
                    for l in range(3):
                        box.append(board[3 * i + k][3 * j + l])
                box = list(filter(lambda x: x.isalnum(), box))
                if len(box) != len(set(box)):
                    return False
        return True
