class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        res = 0
        seen = set()
        length = (n+1) // 2
        for i in range(10**(length-1), 10**length):
            # generate palindrome
            curr = str(i)
            curr += curr[:-1][::-1] if n % 2 else curr[::-1]

            # check for k-palindromicity
            if int(curr) % k:
                continue

            # check if palindrome has been processed before
            curr = sorted(curr)
            temp = "".join(curr)
            if temp in seen:
                continue
            seen.add(temp)

            # calculate number of combinations
            counter = Counter(curr)
            combinations = (n - counter["0"]) * factorial(n - 1)
            for num, count in counter.items():
                combinations //= factorial(count)
            res += combinations
        return res
