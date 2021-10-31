import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        go throug list
        while iterating through array
        make min heap of k elements
        if a new element is greater than the min of heap, remove min and add this
        """
        h = []
        for idx in range(len(nums)):
            if idx < k:
                heapq.heappush(h, nums[idx])
            elif nums[idx] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h,nums[idx])
        return h[0]
                
        