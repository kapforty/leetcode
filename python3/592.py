class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerators, denominators = [], []
        switch = True
        curr = expression[0]

        def flip():
            nonlocal switch
            if switch:
                numerators.append(int(curr))
            else:
                denominators.append(int(curr))
            switch = not switch

        for char in expression[1:]:
            if char == "/" or char == "+":
                flip()
                curr = ""
            elif char == "-":
                flip()
                curr = "-"
            else:
                curr += char
        denominators.append(int(curr))

        denominator = 1
        for val in denominators:
            denominator *= val
        
        for i in range(len(numerators)):
            multiplier = denominator//denominators[i]
            numerators[i] *= multiplier
            denominators[i] *= multiplier
        
        numerator = sum(numerators)
        
        if numerator == 0:
            return "0/1"

        res = ""

        if numerator < 0:
            res += "-"
        numerator = abs(numerator)
        
        i = numerator
        while i > 1:
            if numerator % i == 0 and denominator % i == 0:
                numerator //= i
                denominator //= i
                i = numerator
                continue
            i -= 1
        
        res += str(numerator) + "/" + str(denominator)

        return res
