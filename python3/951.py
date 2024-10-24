# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        frontier = [(root1, root2)]
        while frontier:
            node1, node2 = frontier.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # transform node1
            if node1.left and node1.right:
                if node1.left.val > node1.right.val:
                    node1.left, node1.right = node1.right, node1.left
            elif node1.right:
                node1.left, node1.right = node1.right, node1.left

            # transform node2
            if node2.left and node2.right:
                if node2.left.val > node2.right.val:
                    node2.left, node2.right = node2.right, node2.left
            elif node2.right:
                node2.left, node2.right = node2.right, node2.left
            
            # add transformed children nodes to frontier
            if node1.left:
                frontier.append((node1.left, node2.left))
            if node1.right:
                frontier.append((node1.right, node2.right))

        return True
