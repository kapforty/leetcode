class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even, odd, target = [0 for _ in range(26)], [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len(s1)):
            if i % 2 == 0:
                even[ord(s1[i]) - ord('a')] -= 1
                even[ord(s2[i]) - ord('a')] += 1
            else:
                odd[ord(s1[i]) - ord('a')] -= 1
                odd[ord(s2[i]) - ord('a')] += 1
        return even == odd == target
