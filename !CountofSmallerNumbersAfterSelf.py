from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)  # создаю массив длиной с nums с -1 [-1, -1, -1 ....]
        x = SortedList()  # создаю объект sortedlist
        for i, j in enumerate(nums[::-1]):  # иду по перевернутому массиву nums
            # bisect_left Возвращает индекс для вставки значения в отсортированный список.
            result[len(nums)-i-1] = x.bisect_left(j)  # вставляю в результат на позицию длина - индекс с перевернутого - 1
            x.add(j)  # добавляю в сортедлист значение которое прошел из nums
        return result