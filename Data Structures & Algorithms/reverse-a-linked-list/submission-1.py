# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None

        while head: # head = 0
            tmp = head.next # tmp = 1
            head.next = prev # 0 --> null 
            prev = head # prev = 0
            head = tmp # head = 1 
           
        # 2nd iteration 
        # head = 1
        # tmp = 2 
        # 1 --> 0 --> null 
        # head = 2 

        return prev
           

        