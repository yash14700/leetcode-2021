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
                    return whether s[left:right] or s[left+1:right+1] is a perfect palindrome
        return true
        """
        mistakes = 0
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
                continue

            if mistakes > 0:
                print("mistake")
                print(s[left], left, s[right], right)
                return False

            return self.perfectPalindrome(s[left:right]) or self.perfectPalindrome(s[left+1:right+1])
        
        return True

    def perfectPalindrome(selft, s:str):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True