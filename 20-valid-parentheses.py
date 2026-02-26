class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parentheses = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for item in s:
            if item in parentheses.values():
                stack.append(item)
            elif item in parentheses.keys():
                if not stack or stack[-1]!=parentheses[item]:
                    return False
                stack.pop()
        return not stack  # if empty we return True, else False



