class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i=len(a)-1
        j=len(b)-1
        carry=0
        result=""
        total=""

        while i>=0 or j>=0 or carry:
            digit_a=int(a[i]) if i>=0 else 0
            digit_b=int(b[j]) if j>=0 else 0

            total=digit_a+digit_b+carry
            carry=total//2  #if total is 1 carry is 0, if total is 2 carry is 1
            bit=total%2

            result=result+str(bit)

            i-=1
            j-=1


        return result[::-1] #we reverse because we are pushing the results to the left
