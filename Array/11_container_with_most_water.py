class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        start with outer most indexes
        move the index of the shorter one inward, because it has already formed the most area it possibly could
        return max height found
        """
        
        left = 0
        right = len(height)-1
        max_area=0
        
        while left < right:
            area = (right-left)*(min(height[left], height[right]))
            if area > max_area:
                max_area=area
            
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
            
        return max_area