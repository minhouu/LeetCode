class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums=set(nums[:])
        dict_nums = {}
        for i in set_nums :
            dict_nums[i] = 0
        for i in nums :
            dict_nums[i] += 1
        for i in set_nums :
            if dict_nums[i] > len(nums)/2 :
                return i