func intersect(nums1 []int, nums2 []int) []int {
    // count occurences of each number in nums1
    map1 := make(map[int]int)
    for _, num := range nums1 {
        map1[num] += 1
    }

    // compare values in nums2 to map1
    res := []int{}
    for _, num := range nums2 {
        if map1[num] > 0 {
            res = append(res, num)
            map1[num]--
        }
    }
    return res
}
