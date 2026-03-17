class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # clean the string
        cleaned=''.join(char for char in s if char.isalnum())

        #lower case
        cleaned=cleaned.lower()
        #reverse it
        reversed=cleaned[::-1]

        if reversed==cleaned:
            return True

        return False

