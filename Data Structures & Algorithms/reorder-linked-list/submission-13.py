# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # T: O(N) | S: O(1)
        # N = Size of head
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next, prev, curr = prev, curr, nxt
        front, back = head, prev
        while back:
            nxt_front, nxt_back = front.next, back.next
            front.next, back.next = back, nxt_front
            front, back = nxt_front, nxt_back
