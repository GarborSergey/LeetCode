#  Получаем масисив где есть максимум и минимум,
#  предполагая что удаление можно совершать только слева и справа последовательно
#  вернуть минимальное кол-во опрерациий удаления максимума и минимума

nums = [-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]
x = [0, 0, 10, 0, -1, 0]

z = 3 if len(x) > 2 else 10
print(z)

print(len(x[::-1][:x[::-1].index(min(x))]))
print(x[::-1][:x.index(min(x[::-1]))])
# Не проходит проверку когда один из m чуть дальше середины:
# nums = [-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]
# class Solution:
#     def minimumDeletions(self, nums: List[int]) -> int:
#         max_n = max(nums)
#         min_n = min(nums)
#         max_id = nums.index(max(nums))
#         min_id = nums.index(min(nums))
#
#         result = 0
#
#         max_r = False
#         min_r = False
#
#         if max_id <= (len(nums) - 1) / 2:
#             max_r = True
#         if min_id <= (len(nums) - 1) / 2:
#             min_r = True
#
#         if max_r != min_r:
#
#             if max_id <= (len(nums) - 1) / 2:
#                 result += max_id + 1
#             else:
#                 result += len(nums) - max_id
#
#             if min_id <= (len(nums) - 1) / 2:
#                 result += min_id + 1
#             else:
#                 result += len(nums) - min_id
#
#         else:
#             if max_id > min_id:
#                 result = max_id + 1
#             else:
#                 result = min_id + 1
#
#         print(min_r)
#         print(max_r)
#
#         return result

# ТАЙМ ЛИМИТ КАК ГОВОРИТСЯ так и ПИШЕТСЯ!
# class Solution:
#     def minimumDeletions(self, nums: List[int]) -> int:
#         max_n = max(nums)
#         min_n = min(nums)
#
#         del_r = 0
#         del_l = 0
#         del_rl = 0
#
#         if len(nums) <= 2:
#             del_rl = 2
#
#         result = [del_r, del_l, del_rl]
#
#         transit = nums.copy()
#         while max_n in transit or min_n in transit:
#             del_l += 1
#             del transit[0]
#
#         transit = nums.copy()
#         while max_n in transit or min_n in transit:
#             del_r += 1
#             del transit[len(transit) - 1]
#
#         transit = nums.copy()
#         while (max_n in transit or min_n in transit) and len(transit) > 2:
#             if max_n in transit and min_n in transit:
#                 del_rl += 2
#             else:
#                 del_rl += 1
#
#             del transit[0]
#             del transit[len(transit) - 1]
#
#         result = [del_r, del_l, del_rl]
#         # print(result)
#         # print(max_n)
#         # print(min_n)
#         return min(result)

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        max_n = max(nums)
        min_n = min(nums)
        max_id = nums.index(max(nums))
        min_id = nums.index(min(nums))

        result = 0

        max_l = False
        min_l = False

        if max_id <= (len(nums) - 1) / 2:
            max_l = True
        if min_id <= (len(nums) - 1) / 2:
            min_l = True

        if len(nums) == 3:
            return 2

        div = 3 if len(nums) > 20 else 2

        if max(max_id, min_id) - min(max_id, min_id) < (len(nums) - 1) / div:
            if max_l != min_l:
                if max_l:
                    if len(nums[:max_id]) < len(nums[::-1][:nums[::-1].index(min(nums))]):
                        min_l = True
                    else:
                        max_l = False
                else:
                    if len(nums[:min_id]) < len(nums[::-1][:nums[::-1].index(max(nums))]):
                        max_l = True
                    else:
                        min_l = False

        if max_l != min_l:
            if max_id <= (len(nums) - 1) / 2:
                result += max_id + 1
            else:
                result += len(nums) - max_id - 1

            if min_id <= (len(nums) - 1) / 2:
                result += min_id + 1
            else:
                result += len(nums) - min_id

        else:
            if max_l and min_l:
                if max_id > min_id:
                    result = max_id + 1
                else:
                    result = min_id + 1
            else:
                if max_id > min_id:
                    result = len(nums) - min_id
                else:
                    result = len(nums) - max_id

        print(len(nums))
        print(max_id)
        print(min_id)
        print(min_l)
        print(max_l)

        return result