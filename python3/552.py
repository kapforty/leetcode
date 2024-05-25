# optimized
class Solution:
    def checkRecord(self, n: int) -> int:
        record = [1, 1, 0, 1, 0, 0]
        mod = 10**9 + 7
        for i in range(1, n):
            a, b = sum(record[:3]) % mod, sum(record[3:]) % mod
            record = [a, record[0], record[1], a + b, record[3], record[4]]
        return sum(record) % mod
		
# brute force
class Solution:
    def checkRecord(self, n: int) -> int:
        record = [1, 1, 0, 1, 0, 0]
        # record[0] = zeroAbsentZeroLate
        # record[1] = zeroAbsentOneLate
        # record[2] = zeroAbsentTwoLate
        # record[3] = oneAbsentZeroLate
        # record[4] = oneAbsentOneLate
        # record[5] = oneAbsentTwoLate

        for i in range(1, n):
            temp = [0, 0, 0, 0, 0, 0]
            
            # 0
            temp[0] += record[0] # present
            temp[1] += record[0] # late
            temp[3] += record[0] # absent
            # 1
            temp[0] += record[1] # present
            temp[2] += record[1] # late
            temp[3] += record[1] # absent
            # 2
            temp[0] += record[2] # present
            temp[3] += record[2] # absent
            # 3
            temp[3] += record[3] # present
            temp[4] += record[3] # late
            # 4
            temp[3] += record[4] # present
            temp[5] += record[4] # late
            # 5
            temp[3] += record[5] # present

            record = temp

        return sum(record) % (10**9 + 7)
