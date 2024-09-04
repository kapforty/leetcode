class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = direction = x = y = 0

        obstacleSet = set()
        for obstacle in obstacles:
            obstacleSet.add(tuple(obstacle))

        for command in commands:
            if command == -2:
                direction -= 1
                if direction < 0: direction = 3
            elif command == -1:
                direction += 1
                if direction > 3: direction = 0                 
            else:
                if direction == 0:
                    for i in range(1, command + 1):
                        if (x, y + i) in obstacleSet:
                            command = i - 1
                            break
                    y += command
                elif direction == 1:
                    for i in range(1, command + 1):
                        if (x + i, y) in obstacleSet:
                            command = i - 1
                            break
                    x += command
                elif direction == 2:
                    for i in range(1, command + 1):
                        if (x, y - i) in obstacleSet:
                            command = i - 1
                            break
                    y -= command
                else:
                    for i in range(1, command + 1):
                        if (x - i, y) in obstacleSet:
                            command = i - 1
                            break
                    x -= command
            res = max(res, x**2 + y**2)
        return res
