class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # we use xor property, when an element is ^ with itself, it returns 0
        # 0 with a unique element = 0
        xor=0

        for i in nums:
            xor^=i

        return xor
