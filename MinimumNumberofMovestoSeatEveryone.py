# There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the
# position of the ith seat. You are also given the array students of length n, where students[j] is the position of
# the jth student.
#
# You may perform the following move any number of times:
#
# Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or
# x - 1)
#
# Return the minimum number of moves required to move each student to a seat such that no two students are in the
# same seat.
#
# Note that there may be multiple seats or students in the same position at the beginning.

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        while seats and students:
            min_seat = min(seats)
            min_student = min(students)

            while min_seat != min_student:
                if min_seat > min_student:
                    min_student += 1
                else:
                    min_student -= 1

                result += 1

            seats.remove(min(seats))
            students.remove(min(students))

        return result

# Runtime: 156 ms, faster than 5.23% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
# Memory Usage: 13.9 MB, less than 63.29% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            result += abs(seats[i] - students[i])

        return result

# Runtime: 104 ms, faster than 29.96% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
# Memory Usage: 14 MB, less than 18.30% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
