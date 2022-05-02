# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Time Limit Exceeded Как говорится так и пишется !!!
class Solution1:
    def findDisappearedNumbers(self, nums):
        result = []

        for i in range(1, len(nums) + 1):
            if i not in nums:
                result.append(i)

        return result


# Подсмотрел только то что можно использовать множества!
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        not_in = set(i for i in range(1, len(nums)+1))
        return not_in - set(nums)