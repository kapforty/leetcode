class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        farthestIndex = defaultdict(int)
        for i in range(len(s)):
            farthestIndex[s[i]] = i
        partition, partitionIdx = farthestIndex[s[0]], -1
        res = []
        for i in range(len(s)):
            partition = max(partition, farthestIndex[s[i]])
            if i == partition:
                res.append(i - partitionIdx)
                partitionIdx = i
        return res
