class Solution(object):
    def romanToInt( s):
        RomanToNumberMapping={
            'I':            1   ,
            'V':            5   ,
            'X':            10  ,
            'L':            50  ,
            'C':            100 ,
            'D':            500 ,
            'M':            1000
        }
        total = 0
        prev_value = 0
        for char in s:
            value=RomanToNumberMapping[char]
            if prev_value<value:
               total = total + value- 2 * prev_value
            else:
                total=total+ value
            prev_value = value

        return total            


print("======================")
print(Solution.romanToInt("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"))        