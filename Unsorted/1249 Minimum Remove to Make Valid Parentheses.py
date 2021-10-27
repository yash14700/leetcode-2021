class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        iterate through string
            add idx of open to stack
            pop when close paranthesis
            
            if nothing to pop
                add idx of closed to ignore set

        add remaining indexes to ignore set 

        go through string, and make new string out of everything not in ignore set
        """

        ignore_idx = set()
        idx_stack = []

        for idx in range(len(s)):
            if s[idx] == '(':
                idx_stack.append(idx)
            if s[idx] == ')':
                if len(idx_stack) == 0:
                    ignore_idx.add(idx)
                else:
                    idx_stack.pop()
        
        for idx in idx_stack:
            ignore_idx.add(idx)
        
        result = ""
        for idx in range(len(s)):
            if not idx in ignore_idx:
                result += s[idx]
        
        return result