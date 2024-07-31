class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = {len(books): 0}
        def helper(i):
            if i in dp:
                return dp[i]
            currWidth = maxHeight = 0
            dp[i] = float("inf")
            for j in range(i, len(books)):
                currWidth += books[j][0]
                if currWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                dp[i] = min(dp[i], helper(j+1) + maxHeight)
            return dp[i]
        return helper(0)
