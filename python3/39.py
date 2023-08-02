class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
            elif i >= len(candidates) or total > target:
                return
            else:
                curr.append(candidates[i])
                dfs(i, curr, total + candidates[i])
                curr.pop()
                dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res

        # res = []
        # numMap = {}
        # for i in range(len(candidates)):
        #     nums = []
        #     for j in range(i, len(candidates), 1):
        #         nums.append(candidates[j])
        #     numMap[candidates[i]] = nums
        # print(numMap)
        
        # frontier = [[candidates[i]] for i in range(len(candidates))]
        # while frontier:
        #     for i in range(len(frontier)):
        #         curr = frontier.pop(0)
        #         currSum = sum(curr)
        #         if currSum > target:
        #             continue
        #         elif currSum == target:
        #             res.append(curr)
        #         else:
        #             for nextNum in numMap[curr[-1]]:
        #                 temp = curr.copy()
        #                 temp.append(nextNum)
        #                 frontier.append(temp)
        # return res
