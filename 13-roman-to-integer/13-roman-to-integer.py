class Solution:
    def romanToInt(self, s: str) -> int:
        map_roman = {"I" : 1,
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000}
        value = 0
        pre_value = 0
        integer = 0
        
        for letter in s :
            value=map_roman.get(letter)
            if pre_value < value :
                integer = integer - pre_value * 2 + value
                pre_value = value
            else : 
                integer = integer + value
                pre_value = value
        return integer