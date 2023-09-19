class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = [], []
        size = len(senate)
        
        for i in range(size):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + size)
            else:
                dire.append(dire[0] + size)
            radiant.pop(0)
            dire.pop(0)
        
        return "Radiant" if radiant else "Dire"

# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         queue = list(senate)

#         while True:
#             voter = queue.pop(0)
#             for i in range(len(queue)):
#                 if queue[i] != voter:
#                     break
#             if not queue or i == len(queue):
#                 return "Radiant" if voter == "R" else "Dire"
#             queue.pop(i)
#             queue.append(voter)
