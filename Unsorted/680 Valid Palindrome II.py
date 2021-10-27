class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        mistakes = 0
        while right > left:
            check if s at left == s at right
            if yes, 
            increment and continue
            if no, 
                check if past mistake
                if past mistake -> return false
                if no past mistake, 
                    try to find a valid variation
                    if found -> continue
                    if none -> return false
        return true
        """