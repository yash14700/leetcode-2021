class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        #assuming uniqueness of numbers because they there can only be one solutions
        #no need to deal with edge case of no solutions, because there is exactly one solution
        
        #iterate through list
        #check for complement to target
        #if exists, return list of answers
        #else add item to dict
        
        available_nums = dict()
        pos = 0
        while pos < len(nums):
            num = nums[pos]
            if target-num in available_nums:
                return [available_nums[target-num], pos]
            available_nums[num] = pos
            pos+=1
        