# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # calculate heights of left/right subtrees from each node
        left, right = defaultdict(int), defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            left[node.val], right[node.val] = dfs(node.left), dfs(node.right)
            return max(left[node.val], right[node.val]) + 1
        dfs(root)

        # traverse down binary tree until left/right subtrees have equal heights
        curr = root
        while left[curr.val] != right[curr.val]:
            curr = curr.left if left[curr.val] > right[curr.val] else curr.right
        return curr
