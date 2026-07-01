# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # T: O(N) | S: O(1)
        # N = Size of head
        left = right = head
        prev = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right:
            prev = left
            left = left.next
            right = right.next
        prev.next = prev.next.next if prev.next else None
        return dummy.next
