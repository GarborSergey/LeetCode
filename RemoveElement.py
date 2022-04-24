# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# 1 var
class Solution:
    def removeElement(self, nums: list, val: int):
        counter = 0
        for num in nums:
            if num == val:
                counter += 1

        for i in range(counter):
            nums.remove(val)
# 2 var
class Solution2:
    def removeElement(self, nums, val: int):
        counter = nums.count(val)
        for i in range(counter):
            nums.remove(val)