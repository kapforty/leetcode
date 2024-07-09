class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalTime, currentTime = 0, customers[0][0]
        for arrival, time in customers:
            currentTime = max(currentTime, arrival)
            currentTime += time
            totalTime += currentTime - arrival
        return totalTime / len(customers)
