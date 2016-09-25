# 16. 3Sum Closest
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, 
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # the starter pointer will terminate at the first number greater than the target
        # during the search, terminate when summation == target
        m = len(nums)
        if m < 3:
        	return 0
        result = 0
        nums = sorted(nums)
        smallest_diff = 100000000000

        for i in range(0, m-2):
        	j, k = i + 1, m - 1
        	while j < k:
        		curr_val = nums[i] + nums[k] + nums[j]
        		curr_diff = abs(curr_val - target)
        		if curr_val == target:
        			return target
        		if curr_diff < smallest_diff:
        			smallest_diff = curr_diff
        			result = curr_val
        		if curr_val < target: j += 1 
        		else: k -= 1
        return result




















