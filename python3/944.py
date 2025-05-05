class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = set()
        for i in range(1, len(strs)):
            for j in range(len(strs[0])):
                if j in delete: 
                    continue
                if ord(strs[i][j]) < ord(strs[i-1][j]):
                    delete.add(j)
        return len(delete)
