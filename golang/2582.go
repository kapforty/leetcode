func passThePillow(n int, time int) int {
    direction := -1
    curr := 1
    for i := 0; i < time; i++ {
        if curr == 1 || curr == n {
            direction = -direction
        }
        curr += direction
    }
    return curr
}
