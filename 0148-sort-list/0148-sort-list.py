# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        middle = self.find_middle(head)
        left = head
        right = middle.next
        middle.next = None

        left_head = self.sortList(left)
        right_head = self.sortList(right)

        return self.mergeList(left_head,right_head)
    
    def find_middle(self,head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        return prev

    def mergeList(self,L1,L2):
        dummy = ListNode(0)
        temp = dummy
        while L1 and L2:
            if L1.val < L2.val:
                temp.next = L1
                L1=L1.next
            else:
                temp.next = L2
                L2=L2.next
            temp = temp.next
        
        if L1:
            temp.next = L1
        else:
            temp.next = L2
        
        return dummy.next