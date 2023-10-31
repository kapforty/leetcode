class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i > citations[i]:
                return min(i, citations[i-1])
        return min(len(citations), citations[-1])
        
