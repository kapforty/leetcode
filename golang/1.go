func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for idx, val := range nums {
        if i, ok := m[target - val]; ok {
            return []int{idx, i}
        }
        m[val] = idx
    }
    return []int{}
}