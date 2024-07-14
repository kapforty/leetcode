class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                stack.append(Counter())
            elif formula[i] == ")":
                # calculate number
                i += 1
                num = ""
                while i < len(formula) and formula[i].isnumeric():
                    num += formula[i]
                    i += 1
                i -= 1
                num = 1 if not num else int(num)

                # update map
                atomMap = stack.pop()
                for k in atomMap.keys():
                    atomMap[k] *= num

                # update top map
                if stack:
                    stack[-1] += atomMap
                else:
                    stack.append(atomMap)
            elif formula[i].isnumeric():
                # calculate element
                j = 1
                ele = ""
                while ord(formula[i - j]) > ord("Z"):
                    ele = formula[i - j] + ele
                    j += 1
                ele = formula[i - j] + ele

                # calculate number
                num = ""
                while i < len(formula) and formula[i].isnumeric():
                    num += formula[i]
                    i += 1
                i -= 1
                num = int(num)

                stack[-1][ele] += num - 1
            else:
                ele = ""
                while i < len(formula) and formula[i].isalpha():
                    if formula[i].isupper() and ele != "":
                        break
                    ele += formula[i]
                    i += 1
                i -= 1
                stack[-1][ele] += 1
            i += 1
        
        # sort elements
        elementList = []
        for k, v in stack[-1].items():
            elementList.append([k, v])
        elementList.sort()

        # generate res
        res = ""
        for element, count in elementList:
            res += element
            if count > 1:
                res += str(count)
        return res
