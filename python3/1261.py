# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.elements, frontier = set(), [root]
        while frontier:
            x = frontier.pop()
            self.elements.add(x.val)
            if x.left:
                x.left.val = 2 * x.val + 1
                frontier.append(x.left)
            if x.right:
                x.right.val = 2 * x.val + 2
                frontier.append(x.right)

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
