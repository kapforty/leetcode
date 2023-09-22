class Solution:
    def compress(self, chars: List[str]) -> int:
        currChar, currCount = chars[0], 0
        idx = 0

        for char in chars:
            if char != currChar:
                chars[idx] = currChar
                idx += 1
                if currCount > 9:
                    for num in str(currCount):
                        chars[idx] = num
                        idx += 1
                elif currCount > 1:
                    chars[idx] = str(currCount)
                    idx += 1
                currChar = char
                currCount = 1
            else:
                currCount += 1
        
        chars[idx] = currChar
        idx += 1
        if currCount > 9:
            for num in str(currCount):
                chars[idx] = num
                idx += 1
        elif currCount > 1:
            chars[idx] = str(currCount)
            idx += 1

        return idx

        
