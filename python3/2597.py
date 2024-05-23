class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = -1
        def bt(processed, unprocessed, visited):
            nonlocal res
            res += 1
            for i in range(len(unprocessed)):
                if unprocessed[i] - k not in visited and unprocessed[i] + k not in visited:
                    visited[unprocessed[i]] += 1
                    bt(processed + [unprocessed[i]], unprocessed[i+1:], visited)
                    if visited[unprocessed[i]] == 1:
                        del visited[unprocessed[i]]
                    else:
                        visited[unprocessed[i]] -= 1
        bt([], nums, defaultdict(int))
        return res
