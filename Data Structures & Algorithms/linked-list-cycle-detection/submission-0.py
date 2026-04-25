# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute force = use visited set, if its visited, there's a cycle 

        # Use Fast - Slow Pointers
        # fast pointer will reach the end of the linked list faster than the slow pointer
        # if theres a cycle then the fast and slow pointer will reach the same node in the 
        # same time
        slow, fast = head, head

        while fast and fast.next: # while fast and fast.next is not null 
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True

        return False

            
        