class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        sLen = len(s)

        if not sLen:
            return True

        for char in t:
            if char == s[ptr]:
                ptr += 1
                if ptr == sLen:
                    return True

        return False
