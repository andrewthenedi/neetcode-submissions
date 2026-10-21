# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # T: O(M + N) | S: O(1)
        # M = Size of l1
        # N = Size of l2
        curr = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if total > 9:
                carry, num = divmod(total, 10)
            else:
                carry, num = 0, total
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
