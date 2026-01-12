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
        myNodes = []
        while curr != None:
            myNodes.append(curr)
            curr = curr.next
        return myNodes[int(round(len(myNodes)/2))]
