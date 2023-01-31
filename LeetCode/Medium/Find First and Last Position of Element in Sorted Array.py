from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        def search(l, h, target):
            while l < h:
                m = (l + h) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    h = m
            return l

        left_end = search(0, size, target)
        if left_end == size or nums[left_end] != target:
            return [-1, -1]
        right_end = search(left_end + 1, size, target + 1) - 1
        return [left_end, right_end]
