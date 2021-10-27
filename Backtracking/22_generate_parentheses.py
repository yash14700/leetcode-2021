class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        attempt to make all and cut out the invalid ones

        function that starts the process

        in the function thats called recursively:
            done
            add open
            if (open count >= closed_count)
                add closed
        """
        max_count = n
        open_count = 0
        closed_count = 0
        curr_str = ""
        results = []

        self.generateAll(curr_str, results, max_count, open_count, closed_count)

        return results

    def generateAll(self, curr_str: str, results: List[str], max_count, open_count, closed_count):
        if (closed_count == max_count):
            results.append(curr_str)
            return
        if (open_count < max_count):
            self.generateAll(curr_str+"(", results, max_count, open_count+1, closed_count)
        if (open_count > closed_count):
            self.generateAll(curr_str+")", results, max_count, open_count, closed_count+1)
        return