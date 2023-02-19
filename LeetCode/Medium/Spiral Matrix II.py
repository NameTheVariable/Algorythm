from typing import List
class Solution:
    def generateMatrix(self, n) -> List[List[int]]:
        res = [[0]* n for _ in range(n)]
        col, row, num_elements, e, zone, data = n, n, n*n, 0, 0, 1
        
        while data <= num_elements:
            # move right 
            for i in range(zone, col - zone):
                res[zone][i] = data
                data +=1
            if data == num_elements+1:
                return res
            # move down
            for j in range(zone+1,row-zone):
                res[j][col-1-zone] = data
                data +=1
            if data == num_elements+1:
                return res
            # move left
            for i in range(col-1-zone,zone,-1):
                res[col-1-zone][i-1] = data
                data+=1
            if data == num_elements+1:
                return res
            # move up
            for j in range(row-2-zone,zone,-1):
                res[j][zone] = data
                data+=1
            if data == num_elements+1:
                return res
            zone +=1
        return res     