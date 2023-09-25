class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         sSet, tSet = defaultdict(int), defaultdict(int)

#         for char in s:
#             sSet[char] += 1
#         for char in t:
#             tSet[char] += 1
        
#         for k, v in tSet.items():
#             if sSet[k] != v:
#                 return k
