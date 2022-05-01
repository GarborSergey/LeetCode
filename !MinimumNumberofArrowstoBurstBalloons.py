# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])  # Сортировка по концам отрезков
        ans = 1
        curr = points[0]

        for i in range(len(points)):  # Проход по всем точкам
            # Если у точки начало дальше чем у текущей точки конец, нужна еще стрела
            # устанавливаем новую текущую точку
            if points[i][0] > curr[1]:
                ans += 1
                curr = points[i]

        return ans