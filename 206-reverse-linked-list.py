# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev=None
        curr=head

        while curr is not None: # while we still didn't get to the end
            next=curr.next # next will be whatever is the next of the current
            curr.next=prev  # and here we define what will be the next of current


            #make them of step ahead
            prev=curr
            curr=next

        return prev  # we retun prev because at the end of the loop the prev will be in the head of next liniked list



