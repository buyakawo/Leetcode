class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # we think backwards and we use 3 pointers
        p1=m-1 # last valid position in nums1
        p2=n-1 #last position in nums2
        p= m+n -1 # last position in nums1

        while p2>-1 and p1>-1:
            if nums1[p1] > nums2[p2]:
                nums1[p]=nums1[p1]
                p1-=1
            else:
                nums1[p]=nums2[p2]
                p2-=1

            p-=1

        #we handle the leftover
        while p2>-1:
            nums1[p]=nums2[p2]
            p2-=1
            p-=1








