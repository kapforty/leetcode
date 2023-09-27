class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda p: p[1])
        intervals = [points[0]]

        for point in points[1:]:
            if point[0] > intervals[-1][-1]:
                intervals.append(point)

        return len(intervals)

# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         points.sorted()
#         intervals = [points[0]]

#         for point in points:
#             if point[0] <= intervals[-1][1]:
#                 intervals[-1] = [point[0], min(intervals[-1][1], point[1])]
#             else:
#                 intervals.append(point)

#         return len(intervals)
