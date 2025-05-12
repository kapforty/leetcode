class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res, numMap = [], defaultdict(int)
        for digit in digits:
            numMap[digit] += 1
        for i in range(100, 1000, 2):
            counter, valid = Counter(str(i)), True
            for k, v in counter.items():
                if numMap[int(k)] < v:
                    valid = False
                    break
            if valid:
                res.append(i)
        return res
