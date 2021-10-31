class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        figure out how many to remove - 

        backtracking function that removes all possible combinations of bad item n times
        - if ever reach invalid state -> prune

        """
        bad_closed, bad_open = self.getBadCount(s)
        #print(bad_closed, bad_open)
        idx = 0
        curr_str = ""
        curr_counter = 0
        results = set()

        self.tryAllCombinations(s,idx,bad_closed,bad_open,curr_str,curr_counter,results)

        return list(results)

    def tryAllCombinations(self, src_str, idx, bad_closed, bad_open, curr_str, curr_counter, results: set):
        """
        if string is not valid, return
            too many closed so far
            not enough closed left in the future to complete
        if string is complete -> add to results
        if its a character -> add to curr_str and move forward
        if open -> see if can be removed -> try removing and not removing
        if closed -> see if can be removed -> try removing and not removing
        """
        if curr_counter < 0:
            #todo: improve this pruning
            return
        if idx >= len(src_str):
            if bad_open == 0 and bad_closed == 0 and curr_counter == 0:
                results.add(curr_str)
            return
        if src_str[idx] == '(':
            #remove
            if bad_open > 0:
                self.tryAllCombinations(src_str, idx+1, bad_closed, bad_open-1, curr_str,curr_counter,results)
            #don't remove
            self.tryAllCombinations(src_str, idx+1, bad_closed, bad_open, curr_str+'(',curr_counter+1,results)
        elif src_str[idx] == ')':
            if bad_closed > 0:
                self.tryAllCombinations(src_str,idx+1,bad_closed-1,bad_open, curr_str,curr_counter,results)
            self.tryAllCombinations(src_str,idx+1,bad_closed,bad_open, curr_str+')',curr_counter-1,results)
        else:
            self.tryAllCombinations(src_str, idx+1, bad_closed, bad_open, curr_str+src_str[idx], curr_counter, results)
        return


    def getBadCount(self, s):
        bad_closed = 0
        bad_open = 0
        for c in s:
            if c == '(':
                bad_open+=1
            elif c == ')':
                if bad_open == 0:
                    bad_closed+=1
                else:
                    bad_open-=1
        
        return bad_closed, bad_open