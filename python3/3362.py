class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # map queries to start of range
        rangeMap = defaultdict(list)
        for start, end in queries:
            rangeMap[start].append(end)
        
        # greedily pick queries with farthest endpoint
        res, curr, delta, pq = len(queries), 0, [0] * (len(nums) + 1), []
        for i, num in enumerate(nums):
            curr -= delta[i]
            for end in rangeMap[i]:
                heappush(pq, -end)
            while curr < num:
                if not pq or -pq[0] < i:
                    return -1
                res -= 1
                curr += 1
                delta[-heappop(pq) + 1] += 1
        return res
