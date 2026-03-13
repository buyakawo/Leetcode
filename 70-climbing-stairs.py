class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # ways(n)=ways(n-1)+ways(n-2)

        #base cases
        if n==1:
            return 1
        if n==2:
            return 2

        prev = 1 # 1 way to reach step 1
        curr = 2 # 2 ways to reach step 2


        for i in range(3, n+1): # we start from step 3 since we already have step 1 and 2
            next_val=prev+curr #next val is sum of last 2
            prev=curr
            curr=next_val


        return next_val



