class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        m = len(nums) // 2
        curr = TreeNode(nums[m])
        curr.left = self.sortedArrayToBST(nums[:m])
        curr.right = self.sortedArrayToBST(nums[m+1:])
        return curr
