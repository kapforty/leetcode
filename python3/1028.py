# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # preprocess traversal
        d, stack = deque([]), []
        for c in traversal:
            if not stack:
                stack.append(c)
            elif c == "-":
                if stack[-1] == c:
                    stack.append(c)
                else:
                    d.append(int("".join(stack)))
                    stack = [c]
            else:
                if stack[-1] == "-":
                    d.append("".join(stack))
                    stack = [c]
                else:
                    stack.append(c)
        d.append(int("".join(stack)))
        print(d)

        # dfs
        def dfs(node, depth, remaining):
            if remaining and len(remaining[0]) == depth + 1:
                remaining.popleft()
                child = TreeNode(remaining.popleft())
                node.left = child
                dfs(node.left, depth + 1, remaining)
            if remaining and len(remaining[0]) == depth + 1:
                remaining.popleft()
                child = TreeNode(remaining.popleft())
                node.right = child
                dfs(node.right, depth + 1, remaining)

        # generate tree
        root = TreeNode(d.popleft())
        dfs(root, 0, d)
        return root
