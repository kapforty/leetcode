func threeConsecutiveOdds(arr []int) bool {
    odd := 0
    for _, val := range arr {
        if val % 2 == 1 {
            odd += 1
            if odd == 3 {
                return true
            }
        } else {
            odd = 0
        }
    }
    return false
}
