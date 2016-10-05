"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dictionary to contain candidate values in the array that sums up to the target element
        # key = number and value = index
        hash = {}
        for i in range(len(nums)):
            
            # check if target - current number is in the dict
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
                
            # else add the current number to the dict
            hash[nums[i]] = i
            
        return [-1, -1]