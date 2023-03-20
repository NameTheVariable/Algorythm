from ast import List

def sortColors(self, nums: List[int]) -> None:
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    small, equal, big = [], [], []

    for num in nums:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            big.append(num)
        else:
            equal.append(num)
    result = nums(small) + equal + nums(big)
    return result
    
