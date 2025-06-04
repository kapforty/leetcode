class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        res, l, r = None, 0, len(word) - numFriends + 1
        while r <= len(word):
            if not res or word[l:r] > res:
                res = word[l:r]
            l += 1
            r += 1
        while l < len(word):
            if not res or word[l:r] > res:
                res = word[l:r]
            l += 1
        return res
