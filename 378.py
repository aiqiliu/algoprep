# leetcode 
# 378. Kth Smallest Element in a Sorted Matrix
from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # n = len(matrix)
        # 0 -> matrix[0][0]
        # n^2 -> matrix[n-1][n-1]
        n = len(matrix)
        if k == 0:
            return matrix[0][0]
        if k == n*n:
            return matrix[n-1][n-1]
            
        heapq = []
        for j in range(0,n):
            heappush(heapq, [matrix[0][j], 0, j])
        for j in range(k-1):
            top = heappop(heapq)
            x = top[1]
            y = top[2]
            if x + 1 < n:
                heappush(heapq, [matrix[x+1][y], x+1, y])
                
        return heapq[0][0]