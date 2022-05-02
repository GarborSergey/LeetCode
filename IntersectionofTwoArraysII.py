# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows
# in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2 and num1 not in result:
                    for i in range(min(nums1.count(num1), nums2.count(num2))):
                        result.append(num1)

        return result