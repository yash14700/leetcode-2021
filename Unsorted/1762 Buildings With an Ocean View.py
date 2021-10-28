from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        going from right to left
            if the height of the current building is greater than the max so far, 
                add to list
        reverse list and return
        """
        results = []
        idx = len(heights)-1
        max_height = 0
        while idx >= 0:
            if heights[idx] > max_height:
                results.append(idx)
                max_height = heights[idx]
            idx-=1
        
        return reversed(results)
        