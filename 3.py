#3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
#solution 1: time limit exceeded
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m == 0 or m == 1:
            return m
        if s.count(s[0]) == m:
            return 1

        max_len = 0
        for i in range(0, m):
            h_table = {}
            curr_len = 0
            for j in range(i, m):
                if s[j] not in h_table:
                    h_table[s[j]] = 1
                    curr_len += 1
                else:
                    break
            if curr_len > max_len:
                        max_len = curr_len
                
        return max_len

#solution 2: sliding window. accepted 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m == 0 or m == 1:
            return m
        if s.count(s[0]) == m:
            return 1

        p1 = 0
        p2 = 1
        max_len = 0
        curr_len = 1
        h_table = {}
        h_table[s[p1]] = 1
    
        while p2 < m:
            if s[p2] not in h_table:
                h_table[s[p2]] = 1
                curr_len += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len
                p1, h_table, curr_len = self.helper(s, p1, s[p2], h_table, curr_len)
            p2 += 1
        
        if curr_len > max_len:
            max_len = curr_len
        return max_len    
            
    def helper(self, s, p1, target, h_table, curr_len):
        while s[p1] != target:
             del h_table[s[p1]]
             p1 += 1
             curr_len -= 1
        p1 += 1
        return p1, h_table, curr_len
          
            
            
            
            
            
            
            
            
            
