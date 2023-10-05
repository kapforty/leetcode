class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        res = []
        counter = Counter(nums)
        for ele in counter:
            if counter[ele] > n:
                res.append(ele)
        return res
