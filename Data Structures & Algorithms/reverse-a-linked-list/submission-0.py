# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# prev, curr = None, head

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        # base case
        if not head:
            return None

        # start from the first node 
        newHead = head 
        
        # call recursively on the remaining nodes
        if head.next: # theres still nodes that need to be reversed
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None 

        return newHead 

        # A --> B --> null 
        # step 1: 
        # call reverseList(A)
        # newHead = head
        # head = A, newHead = A 

        # head.next = B 
        # newHead = reverseList(B)
            # head = B, newHead = B 
            # since head.next = null, recursion is skipped and newHead = B
        
        # B.next (head.next.next) = A 
        # A.next (head.next) = None 
        # return B only not A




