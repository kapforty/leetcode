class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = []
        for i in range(len(names)):
            people.append((heights[i], names[i]))
        people = sorted(people, reverse=True)
        for i in range(len(people)):
            people[i] = people[i][1]
        return people
