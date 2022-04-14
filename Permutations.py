# Получаю массив и чисел, нуэно вернуть все варианты последовательности этих чисел
def permute(nums):
    def permutation(nums, start, result):
        if start >= len(nums):
            result.append(list(nums))
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            permutation(nums, start + 1, result)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    permutation(nums, 0, result)
    return result