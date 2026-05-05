# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        if not head or not head.next:
            return True
        
        mid = self.find_mid(head)
        new_head=self.reverse(mid.next)
        first = head
        second = new_head
        while second:
            if first.val != second.val:
                self.reverse(new_head)
                return False
            else:
                first = first.next
                second = second.next
        self.reverse(new_head)
        return True




    def find_mid(self,head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast = fast.next.next
        return slow

    def reverse(self,head):
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
        