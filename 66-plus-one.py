class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """


        # we can use a reverse loop
        for i in range(len(digits)-1, -1 ,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0

        return [1] + digits  # if all are 9 then we need to add a one

