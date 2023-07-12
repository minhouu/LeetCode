class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in accounts :
            sum_of_array = sum(i)
            if sum_of_array > max :
                max = sum_of_array
        return max
            