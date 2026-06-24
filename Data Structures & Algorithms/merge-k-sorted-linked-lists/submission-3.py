# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        def getmin(lists): 
            min_val = 10000 
            min_index = 0 
            for elem in range(len(lists)): 
                if lists[elem].val <= min_val:
                    min_val = lists[elem].val 
                    min_index = elem 
            val = lists[min_index] 
            lists[min_index] = lists[min_index].next 
            if lists[min_index] == None: 
                del lists[min_index] 
            return val, lists
        head = dummy
        while lists:
            minel, lists = getmin(lists)
            head.next = minel
            head = head.next
        return dummy.next
