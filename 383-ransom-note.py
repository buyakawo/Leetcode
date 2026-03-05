from collections import Counter #char:count

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransomNote_counter=Counter(ransomNote)
        magazine_counter=Counter(magazine)

        for char, count in ransomNote_counter.items():
            if magazine_counter[char] <count:
                return False


        return True

