from math import sqrt, floor

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        s=floor(sqrt(x))

        return s