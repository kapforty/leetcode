class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # calculate target
        target, curr = [0 for _ in range(26)], [0 for _ in range(26)]
        for c in s1:
            target[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)-1]:
            curr[ord(c) - ord('a')] += 1
        
        # sliding window
        for i in range(len(s1) - 1, len(s2)):
            curr[ord(s2[i]) - ord('a')] += 1
            if target == curr: 
                return True
            curr[ord(s2[i - len(s1) + 1]) - ord('a')] -= 1
        return False
