class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # populate common
        common = [0] * 26
        for char in words[0]:
            common[ord(char) - ord('a')] += 1

        # iterate through rest of words
        for word in words[1:]:
            curr = [0] * 26
            for char in word:
                curr[ord(char) - ord('a')] += 1
            for i in range(26):
                common[i] = min(common[i], curr[i])
        
        # build result
        res = []
        for i in range(26):
            for _ in range(common[i]):
                res.append(chr(ord('a') + i))
        return res
