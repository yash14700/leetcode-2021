class Solution:
    def __init__(self):
        self.letters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        self.digits = ""
        self.all = []
        self.current = []
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return self.all
        self.digits = digits
        self.makeCombinationsFromIdx(0)
        return self.all
    
    def makeCombinationsFromIdx(self, idx):
        
        if idx == len(self.digits):
            self.all.append("".join(self.current))
            return
        
        digit = self.digits[idx]
        for letter in self.letters[digit]:
            self.current.append(letter)
            self.makeCombinationsFromIdx(idx+1)
            self.current.pop()
            
        return
        
        
       