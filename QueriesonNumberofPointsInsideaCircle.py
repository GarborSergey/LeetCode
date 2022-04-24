# You are given an array points where points[i] = [xi, yi]
# is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.
# You are also given an array queries where queries[j] = [xj, yj, rj]
# describes a circle centered at (xj, yj) with a radius of rj.
# For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle
# are considered inside.
# Return an array answer, where answer[j] is the answer to the jth query.
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        def point_in_circle(circle, point):
            if (circle[0] - point[0]) ** 2 + (circle[1] - point[1]) ** 2 <= circle[2] ** 2:
                return True
            return False

        result = []

        for circle in queries:

            counter = 0

            for point in points:
                yes = point_in_circle(circle, point)
                if yes:
                    counter += 1

            result.append(counter)

        return result