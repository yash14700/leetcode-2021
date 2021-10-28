
from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):        
        self.non_zero_idxs = []
        self.non_zero_vals = dict()
        for idx in range(len(nums)):
            if nums[idx] == 0:
                continue
            self.non_zero_idxs.append(idx)
            self.non_zero_vals[idx] = nums[idx]


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        check which has fewer non zero values and iterate through that
        """
        big = []
        small = []
        if len(self.non_zero_idxs) < len(vec.non_zero_idxs):
            big = vec
            small = self
        else:
            big = self
            small = vec
        
        dot_product = 0
        for idx in small.non_zero_idxs:
            if not idx in big.non_zero_vals:
                continue
            dot_product+=small.non_zero_vals[idx]*big.non_zero_vals[idx]
        
        return dot_product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)