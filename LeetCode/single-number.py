"""Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Algorithm should have a linear runtime complexity. Could you implement it without using extra memory?"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        for i in range(1,len(nums)):
            ret = ret ^ nums[i]
            
            
        return ret 