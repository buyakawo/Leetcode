class Solution(object):
    def removeDuplicates(self, nums):

        if not nums:
            return 0

        i=0 # slow pointer to where the unique element is

        for j in range(1,len(nums)): # fast pointer to find the next uniwue element
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]


        return i+1





