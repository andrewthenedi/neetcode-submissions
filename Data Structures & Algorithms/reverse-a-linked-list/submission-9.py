# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T: O(N) | S: O(1)
        # N = Size of head
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next, prev, curr = prev, curr, nxt
        return prev
