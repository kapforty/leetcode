class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        time = defaultdict(int)
        stack = []
        for log in logs:
            x, y, z = log.split(":")
            x, z = int(x), int(z)
            if not stack:
                stack.append([x, z])
                continue
            if y == "start":
                time[stack[-1][0]] += z - stack[-1][1]
                stack.append([x, z])
            else:
                time[x] += z - stack[-1][1] + 1
                stack.pop()
                if stack:
                    stack[-1][1] = z + 1
        return [time[funcID] for funcID in range(n)]