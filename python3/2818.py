class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1000000007

        # calculate score of each number, push to heap and array
        maxHeap, primeScores = [], []
        for idx, num in enumerate(nums):
            score, curr = 0, num
            for x in range(2, int(sqrt(curr)) + 1):
                if curr % x == 0:
                    score += 1
                    while curr % x == 0:
                        curr //= x
            if curr >= 2:
                score += 1
            heappush(maxHeap, (-num, idx))
            primeScores.append(score)

        # find L/R boundary for each idx in array from prev step
        stack = []
        left, right = [-1] * len(nums), [len(nums)] * len(nums)
        for i, primeScore in enumerate(primeScores):
            while stack and primeScore > stack[-1][1]:
                right[stack.pop()[0]] = i
            if stack:
                left[i] = stack[-1][0]
            stack.append((i, primeScore))

        # build result
        res = 1
        while k:
            num, idx = heappop(maxHeap)
            num = -num
            temp = min(k, (idx - left[idx]) * (right[idx] - idx))
            res = (res * pow(num, temp, MOD)) % MOD
            k -= temp
        return res
