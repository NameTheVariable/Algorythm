class Solution:
    def countAndSay(self, n: int) -> str:
        start = '1'
        for i in range(n-1):
            primary = start[0]
            next=''
            count = 0
            for elment in start:
                if primary == elment:
                    count += 1
                else:
                    next += str(count) + primary
                    primary = elment
                    count = 1
                
            next += str(count) + primary
            start = next
        return start