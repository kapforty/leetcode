class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Counter, word2Counter = Counter(word1), Counter(word2)
        return set(word1Counter.keys()) == set(word2Counter.keys()) and sorted(word1Counter.values()) == sorted(word2Counter.values())

# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1) != len(word2):
#             return False
        
#         wordSet1, wordSet2 = defaultdict(int), defaultdict(int)

#         for char in word1:
#             wordSet1[char] += 1
#         for char in word2:
#             wordSet2[char] += 1

#         if wordSet1.keys() != wordSet2.keys():
#             return False

#         values1, values2 = list(wordSet1.values()), list(wordSet2.values())
#         values1.sort()
#         values2.sort()

#         return values1 == values2
        
