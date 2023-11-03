class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomMap = defaultdict(int)
        magazineMap = defaultdict(int)

        for char in ransomNote:
            ransomMap[char] += 1
        for char in magazine:
            magazineMap[char] += 1

        for k, v in ransomMap.items():
            if ransomMap[k] > magazineMap[k]:
                return False

        return True
