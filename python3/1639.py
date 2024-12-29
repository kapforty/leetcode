class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # Create frequency array
        m, n = len(words[0]), len(target)
        f = [[0 for _ in range(26)] for _ in range(m)]
        for word in words:
            for i in range(m):
                f[i][ord(word[i]) - ord('a')] += 1

        # dp
        dp = {}
        def helper(curr, idx):
            # Base cases
            if curr == n:
                return 1
            if idx >= m:
                return 0
            
            if (curr, idx) in dp:
                return dp[(curr, idx)]

            # Skip the current column
            skip = helper(curr, idx + 1)

            # Use the current column
            use = 0
            if f[idx][ord(target[curr]) - ord('a')] > 0:
                use = f[idx][ord(target[curr]) - ord('a')] * helper(curr + 1, idx + 1)
            
            # Store the result in dp and return
            dp[(curr, idx)] = skip + use
            return dp[(curr, idx)]
        
        return helper(0, 0) % (10**9 + 7)
