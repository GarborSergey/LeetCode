# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums: list, target: int) -> int:
    if target < nums[0]:
        return 0
    elif target > nums[len(nums) - 1]:
        return len(nums)
    for index, num in enumerate(nums):
        if num == target:
            return index
        elif num < target:
            continue
        elif num > target:
            return index



x = [1,3,5,6]
print(searchInsert(x, 10))