
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def backtrack(curr, open_count, close_count):

            # Base case: Valid combination of length 2*n
            if len(curr) == 2 * n:
                result.append(curr)
                return

            # Add opening bracket
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add closing bracket
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result
