class Solution:
    def minEnd(self, n: int, x: int) -> int:
        x = list(str(bin(x))[2:])
        y = list(str(bin(n - 1))[2:])
        z = deque()
        while x and y:
            if x.pop() == "0":
                z.appendleft(y.pop())
            else:
                z.appendleft("1")
        y += z
        x += y
        return int("".join(x), 2)
