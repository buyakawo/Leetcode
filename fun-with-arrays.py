class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_count=0
        count=0

        for num in nums:
            if num==1:
                count+=1
                max_count=(max(max_count, count))

            else:
                count=0

        return max_count


    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        even=0

        for num in nums:
            count=len([_ for _ in str(abs(num))])
            if count%2==0:
                even+=1

            count=0

        return even


