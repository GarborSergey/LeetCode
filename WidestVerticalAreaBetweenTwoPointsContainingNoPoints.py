class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        axis = []
        for point in points:
            axis.append(point[0])

        result = 0
        axis = sorted(axis)

        for i in range(len(axis)):
            if axis[i] == axis[len(axis) - 1]:
                break

            if abs(axis[i] - axis[i + 1]) > result:
                result = abs(axis[i] - axis[i + 1])

        return result