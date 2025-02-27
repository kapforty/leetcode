class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res, nums = 0, set(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                # define vars
                length, x, y = 2, arr[i], arr[j]

                # skip if not at start of fib sequence
                if y - x in nums and y - x < x:
                    continue

                # calculate length of sequence
                while x + y in nums:
                    length += 1
                    x, y = y, x + y

                # update result
                res = max(res, length)
        return res if res >= 3 else 0
