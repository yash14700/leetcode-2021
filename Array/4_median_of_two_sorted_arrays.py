## Effecient solution (O(log(m+n)))
# Lots of subtle details, come back to this one

## Inefficient solution (O(m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        implement dumb solution
        sort in m+n time, and get median
        """
        
        num1_iter = 0
        num2_iter = 0
        
        sorted_nums = []
        
        while num1_iter < len(nums1) and num2_iter < len(nums2):
            num1 = nums1[num1_iter]
            num2 = nums2[num2_iter]
            if  num1 <= num2:
                sorted_nums.append(num1)
                num1_iter+=1
            else:
                sorted_nums.append(num2)
                num2_iter+=1
                
        while num1_iter < len(nums1):
            num1 = nums1[num1_iter]
            sorted_nums.append(num1)
            num1_iter+=1
                
        while num2_iter < len(nums2):
            num2 = nums2[num2_iter]
            sorted_nums.append(num2)
            num2_iter+=1
            
        #get median
        even = (len(sorted_nums))%2 == 0
        left_index = int((len(sorted_nums)-1)/2)
        if(even):
            return sorted_nums[left_index]+(sorted_nums[left_index+1]-sorted_nums[left_index])/2
        else:
            return sorted_nums[left_index]