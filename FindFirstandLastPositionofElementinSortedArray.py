class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        count = nums.count(target)

        if not count:
            return [-1, -1]

        result.append(nums.index(target))

        for i, e in enumerate(nums[::-1]):
            if e == target:
                result.append(len(nums) - 1 - i)
                break

        return result

