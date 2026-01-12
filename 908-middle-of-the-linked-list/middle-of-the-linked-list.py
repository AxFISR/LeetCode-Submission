# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #one time we go through the linked list to save length
        #second time to find mid node
        curr = head

        listLength = 0
        while curr != None:
            listLength += 1
            curr = curr.next
        listLength = int(round(listLength/2))

        for i in range(listLength):
            head = head.next
        return head

        