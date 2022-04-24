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


x = [1, 2, 4, 5, 5, 2, 2, 2]
val = 5
counter = 0
for i in x:
    if i == val:
        counter += 1

for i in range(counter):
    x.remove(val)
    
print(x)
print(counter)