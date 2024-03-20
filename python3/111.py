class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        res = 0
        frontier = [root]

        while frontier:
            res += 1
            temp = []
            for node in frontier:
                if not node.left and not node.right:
                    return res
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            frontier = temp
