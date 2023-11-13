class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        bound = len(matrix) - 1
        curr = 0

        while curr < bound:
            for i in range(curr, bound):
                matrix[curr][i], matrix[i][bound], matrix[bound][len(matrix)-1-i], matrix[len(matrix)-1-i][curr] = matrix[len(matrix)-1-i][curr], matrix[curr][i], matrix[i][bound], matrix[bound][len(matrix)-1-i]
            curr += 1
            bound -= 1
