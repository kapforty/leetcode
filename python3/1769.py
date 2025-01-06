class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefix, postfix = [0], [0]

        # calculate prefix sum
        curr = 1 if int(boxes[0]) == 1 else 0
        for i in range(1, len(boxes)):
            prefix.append(prefix[i - 1] + curr)
            if int(boxes[i]) == 1:
                curr += 1

        # calculate postfix sum
        boxes = boxes[::-1]
        curr = 1 if int(boxes[0]) == 1 else 0
        for i in range(1, len(boxes)):
            postfix.append(postfix[i - 1] + curr)
            if int(boxes[i]) == 1:
                curr += 1

        # build result
        res = []
        for i in range(len(boxes)):
            res.append(prefix[i] + postfix[len(boxes) - 1 - i])
        return res
        
