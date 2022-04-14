# Вернуть самый частовстречаемый элемент из массива
class Solution:
    def majorityElement(self, nums: list) -> int:
        not_repeat = list(set(nums))
        repeats_list = []
        for not_repeat_num in not_repeat:
            repeat = 0

            for num in nums:
                if not_repeat_num == num:
                    repeat += 1

            repeats_list.append(repeat)

        return not_repeat[repeats_list.index(max(repeats_list))]
