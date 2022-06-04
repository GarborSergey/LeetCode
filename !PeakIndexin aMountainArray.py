# Let's call an array arr a mountain if the following properties hold:
#
#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... arr[i-1] < arr[i]
#         arr[i] > arr[i+1] > ... > arr[arr.length - 1]
#
# Given an integer array arr that is guaranteed to be a mountain,
# return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1