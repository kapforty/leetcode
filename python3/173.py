# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.add(root)
        print(self.stack)

    def next(self) -> int:
        curr = self.stack.pop()
        self.add(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
    
    def add(self, node):
        if not node:
            return
        self.stack.append(node)
        self.add(node.left)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
