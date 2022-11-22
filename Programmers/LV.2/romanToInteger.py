class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        count: int = 0
        for i in range(len(s) - 1):
            if rom[s[i]] < rom[s[i + 1]]:
                count -= rom[s[i]]
            else:
                count += rom[s[i]]

        return count + rom[s[-1]]