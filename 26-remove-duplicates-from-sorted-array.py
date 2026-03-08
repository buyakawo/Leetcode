class Solution(object):
    def removeDuplicates(self, nums):

        if not nums:
            return 0

        i=0 #slow pointer for where the unique element is

        for j in range(1, len(nums)): #fast pointer to loop through array to find next unique element
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]

        return i+1
