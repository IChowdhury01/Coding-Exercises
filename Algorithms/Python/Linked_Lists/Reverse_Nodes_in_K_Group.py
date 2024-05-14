# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        dummy node
        cur at dummy
        get k nodes from cur (end of cur group)
        get start of next group

        reverse nodes, but make old head of group point to head of next group
        make prev group head point to new cur group start
        '''
        dummy = ListNode(0, head)
        prevGroupTail = dummy
        
        while True:
            curGroupHead = prevGroupTail.next
            curGroupTail = self.getKthNode(prevGroupTail, k)
            if not curGroupTail:
                break
            nextGroupHead = curGroupTail.next
            
            cur, prev = curGroupHead, nextGroupHead

            while cur != nextGroupHead:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            prevGroupTail.next = prev
            prevGroupTail = curGroupHead
        
        return dummy.next


    def getKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while head and k > 0:
            head = head.next
            k -= 1
        return head
