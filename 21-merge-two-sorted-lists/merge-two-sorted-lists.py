# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(list1 is None):
            return list2
        elif(list2 is None):
            return list1
        elif(list1 is None and list2 is None):
            return list1
        head1 = list1
        head2 = list2
        while(list1 != None and list2!= None):
            if(list1.val <= list2.val):
                while(list1.next is not None and list2.val >= list1.next.val):
                    list1 = list1.next        
                temp = list1.next
                list1.next = list2
                list1 = temp
  

            else:
                while(list2.next is not None and list1.val >= list2.next.val):
                    list2 = list2.next    
                temp = list2.next
                list2.next = list1
                list2 = temp


        if(head1.val <= head2.val):
            return head1
        return head2