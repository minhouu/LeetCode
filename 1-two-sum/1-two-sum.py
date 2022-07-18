class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for index, number in enumerate(nums) :
            s_num=target-number
            if s_num not in dic :
                dic[number]=index
            else :
                return [index, dic[s_num]]
                