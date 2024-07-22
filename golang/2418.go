func sortPeople(names []string, heights []int) []string {
    sorted := false
    for !sorted {
        sorted = true
        for i := 0; i < len(names) - 1; i++ {
            if heights[i] < heights[i + 1] {
                sorted = false
                names[i], names[i + 1] = names[i + 1], names[i]
                heights[i], heights[i + 1] = heights[i + 1], heights[i]
            }
        }
    } 
    return names
}
