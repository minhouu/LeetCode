class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums :
            if i in nums_dict :
                nums_dict[i] += 1
            else :
                nums_dict[i] = 1
            if nums_dict[i] >= len(nums)/2 :
                return i
        