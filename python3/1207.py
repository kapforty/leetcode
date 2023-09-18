class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        countSet = set()
        
        for k in count:
            if count[k] in countSet:
                return False
            countSet.add(count[k])
        
        return True
