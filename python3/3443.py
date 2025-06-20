class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = changes = x = y = 0

        # NE
        for c in s:
            if c == "S" and changes < k:
                changes += 1
                y += 1
            elif c == "W" and changes < k:
                changes += 1
                x += 1
            elif c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1
            res = max(res, abs(x) + abs(y))

        # NW
        changes = x = y = 0
        for c in s:
            if c == "S" and changes < k:
                changes += 1
                y += 1
            elif c == "E" and changes < k:
                changes += 1
                x -= 1
            elif c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1
            res = max(res, abs(x) + abs(y))

        # SE
        changes = x = y = 0
        for c in s:
            if c == "N" and changes < k:
                changes += 1
                y -= 1
            elif c == "W" and changes < k:
                changes += 1
                x += 1
            elif c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1
            res = max(res, abs(x) + abs(y))

        # SW
        changes = x = y = 0
        for c in s:
            if c == "N" and changes < k:
                changes += 1
                y -= 1
            elif c == "E" and changes < k:
                changes += 1
                x -= 1
            elif c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1
            res = max(res, abs(x) + abs(y))
            
        return res
