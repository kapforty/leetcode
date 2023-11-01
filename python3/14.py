class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        res = 0
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                break
            res += 1
        return strs[0][:res]

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = list(strs[0])
#         for word in strs:
#             word = list(word)
#             while len(res) > len(word):
#                 res.pop()
#             while len(word) > len(res):
#                 word.pop()
#             while word and res != word:
#                 res.pop()
#                 word.pop()
#         return "".join(res)
