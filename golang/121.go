func maxProfit(prices []int) int {
    cost, res := math.MaxInt32, 0
    for _, price := range prices {
        if price < cost {
            cost = price
        }
        if price - cost > res {
            res = price - cost
        }
    }
    return res
}
