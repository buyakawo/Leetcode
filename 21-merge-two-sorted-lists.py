# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        current=dummy  #pointer that initially points to dummy

        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1  #attach current pointer to list 1
                list1=list1.next #move to the next value

            else:
                current.next=list2
                list2=list2.next

            current=current.next #move to newly added node

        current.next=list1 if list1 else list2

        return dummy.next # retun what dummy.next points to , so we don't have to return dummy





