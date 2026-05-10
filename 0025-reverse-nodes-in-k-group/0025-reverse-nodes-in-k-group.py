# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy1 = ListNode(-1)
        dummy1.next = head
        prev_group = dummy1

        curr = head

        while curr:
            cnt=1
            start = curr

            while cnt<k and curr:
                curr = curr.next
                cnt+=1
            
            if curr is None:
                break
            
            next_node = curr.next
            curr.next = None
            new_head = self.reverse(start)
            prev_group.next = new_head

            start.next=next_node
            prev_group = start

            curr = next_node
        
        head = dummy1.next
        return head

    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        


        