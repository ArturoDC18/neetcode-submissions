# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val >= list2.val:
                copy = list2.next
                list2.next = self.mergeTwoLists(list1,copy)
                return list2
            else:
                copy = list1.next
                list1.next = self.mergeTwoLists(copy, list2)
                return list1
        elif list1:
            copy = list1.next
            list1.next = self.mergeTwoLists(copy, None)
            return list1
        elif list2:
            copy = list2.next
            list2.next = self.mergeTwoLists(None,copy)
            return list2

        