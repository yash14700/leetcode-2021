class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Iterate through nums, and make dict {sum: list of {i, j} that made sum}
        Iterate through nums, find 0 complement, make set of frozen sets
        Iterate through frozen set, convert to list of lists and return
        """
        
        sums_dict = dict()
        left = 0
        while left < len(nums):
            right = left+1
            while right < len(nums):
                two_sum = nums[left]+nums[right]
                if not two_sum in sums_dict:
                    sums_dict[two_sum] = []
                sums_dict[two_sum].append({left, right})
                right+=1
            left+=1
        
        
        k = 0
        result_set = set()
        while k < len(nums):
            comp = 0-nums[k]
            if comp in sums_dict:
                for pairs in sums_dict[comp]:
                    if k in pairs:
                        continue
                    three_list = []
                    for idx in pairs:
                        three_list.append(nums[idx])
                    three_list.append(nums[k])
                    sorted_tuple = tuple(sorted((three_list)))
                    
                    if sorted_tuple in result_set:
                        continue
                        
                    result_set.add(sorted_tuple)
            k+=1
            
        return result_set