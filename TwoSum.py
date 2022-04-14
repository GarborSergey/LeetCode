# Получаешь массив и определенное число
# Вернуть два индекса числа из массива, которые в сумме дают искомое число
def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

