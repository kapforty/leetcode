func productExceptSelf(nums []int) []int {
    prefix := []int{1}
    postfix := []int{1}
    res := []int{}

    for i := 0; i < len(nums) - 1; i++ {
        prefix = append(prefix, prefix[len(prefix) - 1] * nums[i])
    }
    for i := len(nums) - 1; i > 0; i-- {
        postfix = append(postfix, postfix[len(postfix) - 1] * nums[i])
    }
    for i := 0; i < len(nums); i++ {
        res = append(res, prefix[i] * postfix[len(nums) - 1 - i])
    }
    return res
}
