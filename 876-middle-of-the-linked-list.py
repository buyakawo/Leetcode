# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use slow and fast pointer, the fast pointer advances twice as the slow pointer
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        s=f=head

        while f and f.next:
            f=f.next.next
            s=s.next

        return s


