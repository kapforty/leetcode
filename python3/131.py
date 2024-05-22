class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        visited = set()
        def bt(curr):
            res.append(curr)
            for i in range(len(curr)):
                case1, case2 = None, None
                if i > 0 and i < len(curr) - 1:
                    case1 = "".join(curr[i-1:i+2])
                if i < len(curr) - 1:
                    case2 = "".join(curr[i:i+2])
                if case1 and case1 == case1[::-1]:
                    temp = curr[:i-1] + [case1] + curr[i+2:]
                    if tuple(temp) not in visited:
                        visited.add(tuple(temp))
                        bt(temp)
                if case2 and case2 == case2[::-1]:
                    temp = curr[:i] + [case2] + curr[i+2:]
                    if tuple(temp) not in visited:
                        visited.add(tuple(temp))
                        bt(temp)
        bt(list(s))
        return res
