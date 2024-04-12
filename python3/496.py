class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextElementDict = defaultdict(int)
        stack = []

        # use decreasing monotonic stack, store next greater element in dict
        for val in nums2:
            while stack and stack[-1] < val:
                nextElementDict[stack.pop()] = val
            stack.append(val)
        
        # build result
        res = []
        for val in nums1:
            res.append(nextElementDict.get(val, -1))
        return res

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # can alternatively use lambda
        nextElementDict = defaultdict(lambda: -1)
        stack = []

        for val in nums2:
            while stack and stack[-1] < val:
                nextElementDict[stack.pop()] = val
            stack.append(val)
        
        res = []
        for val in nums1:
            res.append(nextElementDict[val])
        return res
