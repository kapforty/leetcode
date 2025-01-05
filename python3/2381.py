class Solution:
    def shift(self, letter: str, shift: int):
            newASCIIVal = ord(letter) + shift
            return chr(((newASCIIVal - ord("a")) % 26) + ord("a"))
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        shift = [0] * len(s)
        for x, y, z in shifts:
            if z == 0:
                z = -1
            shift[x] += z
            if y+1 < len(s):
                shift[y+1] += -z
        curr = 0
        for i, c in enumerate(s):
            curr += shift[i]
            s[i] = self.shift(c, curr)
        return "".join(s)
