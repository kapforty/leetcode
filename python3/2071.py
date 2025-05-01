class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # helper function
        def valid(n):
            idx = 0
            tempTasks = deque()
            tempPills = pills
            for i in range(n-1,-1,-1):
                while idx < n and tasks[idx] <= workers[i]+strength:
                    tempTasks.append(tasks[idx])
                    idx += 1
                if len(tempTasks) == 0:
                    return False
                if workers[i] >= tempTasks[0]:
                    tempTasks.popleft()
                elif tempPills > 0:
                    tempTasks.pop()
                    tempPills -= 1
                else:
                    return False
            return True
        tasks.sort()
        workers.sort(reverse = True)
        
        # binary search
        res, l, r = -1, 0, min(len(tasks), len(workers))
        while l <= r:
            m = (l+r)//2
            if valid(m):
                res = m
                l = m+1
            else:
                r = m-1
        return res
