class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr = res = 0
        visited = defaultdict(int)
        visited[0] = 1
        for num in nums:
            curr += num
            remainder = curr % k
            res += visited[remainder]
            visited[remainder] += 1
        return res
