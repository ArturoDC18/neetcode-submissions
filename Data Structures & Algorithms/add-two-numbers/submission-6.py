# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def compute (val, carry):
            if carry:
                val += 1
            carry = val // 10
            new = ListNode(val%10)
            return new,carry
        def rec(l1,l2,carry):
            if not l1 and not l2:
                if carry:
                    new = ListNode(1)
                    return new
                else:
                    return None
            elif not l1:
                val = l2.val
                new,carry = compute(val, carry)
                new.next = rec(l1,l2.next,carry)
                return new
            elif not l2:
                val = l1.val
                new,carry = compute(val, carry)
                new.next = rec(l1.next,l2,carry)
                return new
            else:
                val = l1.val + l2.val
                new,carry = compute(val, carry)
                new.next = rec(l1.next,l2.next,carry)
                return new
        
        return rec(l1,l2,0)
        