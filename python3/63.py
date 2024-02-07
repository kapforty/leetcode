class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # check trivial cases (start/end are obstacles)
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        # transform obstacleGrid
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                obstacleGrid[row][col] *= -1
        
        # dp
        obstacleGrid[0][0] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == -1:
                    continue
                top = left = 0
                if row - 1 >= 0 and obstacleGrid[row-1][col] != -1:
                    top = obstacleGrid[row-1][col]
                if col - 1 >= 0 and obstacleGrid[row][col-1] != -1:
                    left = obstacleGrid[row][col-1]
                obstacleGrid[row][col] += top + left
        return obstacleGrid[-1][-1]
