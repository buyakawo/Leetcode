class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        sum=0

        for i in range(0, len(nums)):
            sum+=nums[i]
            output.append(sum)

        return output


