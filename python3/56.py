class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for first, second in intervals:
            last = res[-1][1]
            if last < first:
                res.append([first, second])
            else:
                res[-1][1] = max(last, second)
        return res


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals = sorted(intervals, key=lambda x: x[0])
#         res = []
#         currInterval = intervals[0]

#         for interval in intervals:
#             if currInterval[1] < interval[0]:
#                 res.append(currInterval)
#                 currInterval = interval
#             else:
#                 currInterval = [
#                     min(currInterval[0], interval[0]),
#                     max(currInterval[1], interval[1])
#                 ]
        
#         res.append(currInterval)
#         return res
