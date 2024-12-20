class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        frontier, level = [root], 0
        while frontier:
            level += 1
            newFrontier = []
            for node in frontier:
                if node.left:
                    newFrontier.append(node.left)
                    newFrontier.append(node.right)
            if level % 2:
                l, r = 0, len(newFrontier) - 1
                while l < r:
                    newFrontier[l].val, newFrontier[r].val = newFrontier[r].val, newFrontier[l].val
                    l += 1
                    r -= 1
            frontier = newFrontier
        return root
