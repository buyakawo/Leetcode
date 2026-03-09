class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k=0 #slow pointer to track the element that doesn't have val

        for i in range(len(nums)): #fast pointer to go through nums
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k

