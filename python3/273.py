class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        res = ""
        num = list(str(num))
        endings = ["Billion", "Million", "Thousand", ""]
        sub20 = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen"
        }
        over20 = {
            "2": "Twenty",
            "3": "Thirty",
            "4": "Forty",
            "5": "Fifty",
            "6": "Sixty",
            "7": "Seventy",
            "8": "Eighty",
            "9": "Ninety"
        }
        while num:
            temp = ""
            curr = []
            for i in range(3):
                curr.append(num.pop())
                if not num: break
            while len(curr) < 3:
                curr.append('0')
            curr = curr[::-1]
            if curr[0] != '0':
                temp += " " + sub20[curr[0]] + " " + "Hundred"
            if curr[1] == '1':
                temp += " " + sub20[str(int(curr[1] + curr[2]))]
            else:
                if curr[1] != '0':
                    temp += " " + over20[curr[1]] 
                if curr[2] != '0':
                    temp += " " + sub20[curr[2]]
            currEnding = endings.pop()
            if temp != "":
                temp += " " + currEnding
            res = temp + res
        return res.strip()
