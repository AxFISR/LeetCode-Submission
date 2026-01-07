# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(head is None or head.next is None):
            return head
        curr = head
        prev = None
        next = None
        
        while(curr is not None):
            next = curr.next    #save next node
            curr.next = prev    #connect to previous node
            prev = curr         #updates the prev node
            curr = next         #updates curr position
        return prev
        

        