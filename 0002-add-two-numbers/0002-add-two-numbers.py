# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        L1= l1
        L2=l2
        carry = 0
        dummy1 = ListNode(-1)
        dum1 = dummy1
        while L1 is not None or L2 is not None or carry:
            sum1 = 0
            if L1 is not None:
                sum1+=L1.val
                L1 = L1.next
            if L2 is not None:
                sum1+=L2.val
                L2=L2.next
            
            sum1+=carry
            carry = sum1/10
            new_node = ListNode(sum1%10)
            dum1.next = new_node
            dum1 = dum1.next
        return dummy1.next
        