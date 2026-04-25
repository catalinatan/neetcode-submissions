class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = head
        curr = head.next
        dummy.next = None

        while curr != None:
            tmp1 = curr.next 
            tmp2 = dummy
            dummy = curr
            dummy.next = tmp2
            curr = tmp1

        return dummy