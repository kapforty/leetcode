class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        count = 0
        curr = []
        res = []

        for word in words:
            # check if curr is at capacity
            if len(word) + count > maxWidth:
                if len(curr) > 2 or count == maxWidth + 1:
                    curr.pop()
                    count -= 1
                i = 1
                while count < maxWidth:
                    curr[i] += " "
                    count += 1
                    i += 2
                    if i >= len(curr):
                        i = 1
                res.append("".join(curr))
                count = 0
                curr = []
            curr.append(word)
            curr.append(" ")
            count += len(word) + 1

        # handle last row of words
        curr.pop()
        count -= 1
        curr.append(" " * (maxWidth - count))
        res.append("".join(curr))

        return res
      
