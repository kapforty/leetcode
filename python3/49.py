class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapski = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in mapski.keys():
                mapski[sortedStr].append(s)
            else:
                mapski[sortedStr] = [s]
        
        return mapski.values()
