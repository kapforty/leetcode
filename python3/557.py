class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         stack = ""
#         res = ""

#         for char in s:
#             if char == " ":
#                 res += stack[::-1] + " "
#                 stack = ""
#             else:
#                 stack += char
#         res += stack[::-1]

#         return res
