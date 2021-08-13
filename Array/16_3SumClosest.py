class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        For each number in the sorted nums
            Find the two sum thats "closest" to target-nums[i]
            Add num to the closest two sum
            keep track of the closest among all and return it
        
        How do you find the "closest" two sum in linear time
            do the two pointer iteration and keep track of the closest of them all
            
        """
        
        nums.sort()
        idx = 0
        closest_sum=0
        while idx < len(nums)-2:
            num = nums[idx]
            
            if idx != 0 and num == nums[idx-1]:
                idx+=1
                continue
            
            closest_two_sum = self.twoSumClosest(nums, target-num, idx)
            closest_using_num = closest_two_sum + num
            
            if idx==0 or abs(target-closest_using_num) < abs(target-closest_sum):
                closest_sum = closest_using_num
            
            idx+=1
        
        return closest_sum
    
    def twoSumClosest(self, nums, target, idx):
        left=idx+1
        right = len(nums)-1
        
        closest_sum=nums[left] + nums[right]
        while left < right:
            current_sum = nums[left]+nums[right]
            if abs(target-current_sum) < abs(target-closest_sum):
                closest_sum=current_sum
            if current_sum == target:
                break
            elif current_sum > target:
                right-=1
            else:
                left+=1
        
        return closest_sum