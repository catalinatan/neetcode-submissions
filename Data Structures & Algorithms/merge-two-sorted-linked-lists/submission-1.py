class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy # you need a curr variable to keep the dummy in the head of the list while moving the
        # pointer curr forward then u return dummy.next

        # so basically 2 pointers
        
        # Edge Cases
        if not list1 and list2:
            return list2

        if not list2 and list1:
            return list1

        if not list1 and not list2:
            return None

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1 
                list1 = list1.next
                
            elif list2.val < list1.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list2:
            curr.next = list2 
        elif list1:
            curr.next = list1

        return dummy.next