# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
#
# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
#
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

        d = [
            distance(p1, p2),
            distance(p1, p3),
            distance(p1, p4),
            distance(p2, p3),
            distance(p2, p4),
            distance(p3, p4),
        ]

        d.sort()

        return 0 < d[0] == d[1] == d[2] == d[3] and d[4] == d[5]
