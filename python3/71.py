class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        res = "/"
        stack = []

        for p in path:
            if p == "" or p == ".":
                continue
            if p == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(p)

        res += "/".join(stack)
        return res
