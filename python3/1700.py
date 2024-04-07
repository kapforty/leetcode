class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0, count1 = students.count(0), students.count(1)
        sandwiches = sandwiches[::-1]
        while sandwiches:
            if sandwiches[-1] == 0:
                if count0 == 0:
                    break
                count0 -= 1
            if sandwiches[-1] == 1:
                if count1 == 0:
                    break
                count1 -= 1
            sandwiches.pop()
        return count0 + count1
        