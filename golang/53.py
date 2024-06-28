func maxSubArray(nums []int) int {
    res := nums[0]
    curr := 0
    for _, num := range nums {
        if curr < 0 {
            curr = 0
        }
        curr += num
        if curr > res {
            res = curr
        }
    }
    return res
}
