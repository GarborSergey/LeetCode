# Вернуть максимальные значение подмассива из массива
class Solution:
    def maxSubArray(self, nums) -> int:
        result = nums[0]
        max_sub = 0
        for num in nums:
            max_sub += num
            if result < max_sub:
                result = max_sub
            if max_sub < 0:
                max_sub = 0

        return result

