# leetcode
# 377. Combination Sum IV
# Given an integer array with all positive numbers and no duplicates, 
# find the number of possible combinations that add up to a positive integer target.

# My solution
class Solution(object):
    def combinationSum4(self, nums, target):
        if len(nums) == 0 or target < min(nums) or sum(1 for num in nums if num > 0) < 1:
            return 0
        result = 0
        return self.helper(sorted(nums), target, result, 0)
        
    def helper(self, nums, target, result, total):
        if total > target:
            return result
        elif total == target:
            result += 1
            return result
        else:
            for num in nums:
                total += num
                result = self.helper(nums, target, result, total)
                total -= num
            return result
        