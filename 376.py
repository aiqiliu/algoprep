#376. Wiggle Subsequence
# Given a sequence of integers, return the length of the longest subsequence 
# that is a wiggle sequence. A subsequence is obtained by deleting some number of
# elements (eventually, also zero) from the original sequence, 
# leaving the remaining elements in their original order.
# My solution: incomplete
class Solution(object):
    #[1,7,4,9,2,5]
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return 0
        if nums == sorted(nums) or nums == sorted(nums)[:-1]:
            return 2
            
        longest = []
        for index in range(0, len(nums)-2):
            longest.append(self.helper(nums, index, 1, 0) + 2)
        return max(longest)
        
    def helper(self, nums, index, accu, result):
        for i in range(index+1, len(nums)):
            if i < index + 3:
                accu *= nums[i] - nums[i-1]
            elif i >= 3:
                accu /= nums[i-2] - nums[i-3]
                accu *= nums[i] - nums[i-1]
            
            if accu < 0 and i > index + 1:
                    result += 1
            elif accu >= 0 and i > index + 1:
                return result
        return result
                
            