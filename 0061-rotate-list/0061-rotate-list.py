#Time Complexity : O(2N)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        length=0
        tail = head
        while tail.next:
            length+=1
            tail = tail.next
        length+=1
        if k%length == 0:
            return head
        else:
            shift = length - (k%length) - 1
            curr = head
            for _ in range(shift):
                curr = curr.next

            new_head = curr.next
            curr.next = None
            tail.next = head

        head = new_head
        return head        