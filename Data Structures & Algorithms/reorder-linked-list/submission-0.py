# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        second = slow.next # u have to reverse it 
        prev = slow.next = None # we split into 2 lists

        # reverse 2nd portion of the list 
        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 

        # prev = last node will be the new head of the new list
        # second would be null 

        # merge 2 halfs
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2
           