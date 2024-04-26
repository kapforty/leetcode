class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        frontier = grid[0]
        for row in grid[1:]:
            # calculate smallest values in previous row
            smallest = []
            for i in range(len(frontier)):
                smallest.append([frontier[i], i])
            smallest.sort()

            # update frontier
            temp = []
            for i in range(len(row)):
                if i == smallest[0][1]:
                    temp.append(row[i] + smallest[1][0])
                else:
                    temp.append(row[i] + smallest[0][0])
            frontier = temp

        return min(frontier)
