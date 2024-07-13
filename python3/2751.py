class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        robots = []
        for i in range(len(healths)):
            robots.append([positions[i], healths[i], directions[i], i])
        robots.sort()
        
        for robot in robots:
            # pos, hp, direction, num 
            if robot[2] == 'R':
                stack.append(robot)
                continue
            while stack and stack[-1][2] == 'R' and stack[-1][1] < robot[1]:
                stack.pop()
                robot[1] -= 1
            if stack and stack[-1][2] == 'R' and stack[-1][1] == robot[1]:
                stack.pop()
            elif stack and stack[-1][2] == 'R' and stack[-1][1] > robot[1]:
                stack[-1][1] -= 1
            else:
                stack.append(robot)
        
        stack.sort(key=lambda x:x[3])
        res = []
        for val in stack:
            res.append(val[1])
        return res

