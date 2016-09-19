# 3sum: 
# 1. get len
# return [] if len<3
# split the list into <= 0 and > 0
# recursion, for every num1 in l1, pair up with num2 in l2. 
# if (0 - num1 - num2) in num1 or in num2, append the [num1, num2, 0-num1-num2] in result
# first iteration: problem - have duplicates
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m < 3:
        	return []
        result = []
        l1 = [num1 for num1 in nums if num1 <= 0]
        l2 = [num2 for num2 in nums if num2 > 0]
        for num1 in l1:
        	for num2 in l2:
        		curr = [num1, num2]
        		num3 = 0 - num1 - num2
        		if num3 in l1 or num3 in l2:
        			curr.append(num3)
        			result.append(curr)
        return result

# second iteration: add a dict to indicate if num1 has occured before
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m < 3:
        	return []
        result = []
        dict = {}
        l1 = [num1 for num1 in nums if num1 <= 0]
        l2 = [num2 for num2 in nums if num2 > 0]
        for num1 in l1:
        	if num1 not in dict:
        		dict[num1] = 1
	        	for num2 in l2:
	        		curr = [num1, num2]
	        		num3 = 0 - num1 - num2
	        		if num3 in nums:
	        			if num3 in curr and nums.count(num3) > 1:
		        			curr.append(num3)
		        			result.append(curr)
	    result = [sorted(l) for l in result] 
	    result = set(tuple(x) for x in result)
	    result = [list(x) for x in result] 
        return result

# third iteration: ignored that all elements may be 0
# second iteration: add a dict to indicate if num1 has occured before
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        if m < 3:
        	return []
        result = []
        dict = {}
        if all(x == 0 for x in nums):
            return [[0,0,0]]
        l1 = [num1 for num1 in nums if num1 <= 0]
        l2 = [num2 for num2 in nums if num2 > 0]
        if l1.count(0) >= 3:
            result.append([0,0,0])
        for num1 in l1:
        	if num1 not in dict and num1 != 0:
        		dict[num1] = 1
	        	for num2 in l2:
	        		curr = [num1, num2]
	        		num3 = 0 - num1 - num2
	        		if num3 in nums:
	        			if num3 in curr and nums.count(num3) > 1 or num3 not in curr and nums.count(num3) > 0:
		        			curr.append(num3)
		        			result.append(curr)

        result = [sorted(l) for l in result] 
        result = set(tuple(x) for x in result)
        result = [list(x) for x in result] 
        return result


