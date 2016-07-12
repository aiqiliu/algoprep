# leetcode 
# 373. find k smallest pairs
# my solution 1: wrong 
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        if k == 0:
            return []
        elif len(nums1) == 0 or len(nums2) == 0:
            return []
        elif k >= len(nums1) * len(nums2):
            for a in nums1:
                for b in nums2:
                    result.append([a,b])
        else:
            i = 0
            j = 0
            while (i < len(nums1) or j < len(nums2)) and len(result) < k:
                if i == len(nums1):
                    i = 0
                if j == len(nums2):
                    j = 0
                result.append([nums1[i], nums2[j]])
                nexta = i + 1
                nextb = j + 1
                if nexta < len(nums1) and nextb < len(nums2):
                    if nums1[nexta] < nums2[nextb]:
                        i = nexta
                    else:
                        j = nextb
                elif nexta == len(nums1):
                    j = nextb
                else:
                    i = nexta
        return result
        
   
# solution 2: loop through all the results.
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        return map(list, sorted(itertools.product(nums1, nums2), key=sum)[:k])

# solution 3: use min heaps to reduce memory to O(k), reduce run time to O(logk)
# top of the heap is initially set to 0xffffff
# 
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        heap = [(0x2ffffff, None, None)]
        in1 = 0
        while len(result) < min(k, len(nums1) * len(nums2)):
            # handles the case when k = 0 or nums1 or nums2 is empty
            if in1 < len(nums1):
                top = heap[0][0]
                if nums1[in1] + nums2[0] < top:
                    for num2 in nums2:
                        heapq.heappush(heap, (nums1[in1] + num2, nums1[in1], num2))
                    in1 += 1
            sum, num1, num2 = heapq.heappop(heap)
            result.append([num1, num2])
        return result

   
        
        
        













        
        
        













        