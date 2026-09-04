# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # T: O(N) | S: O(1)
        # N = Size of head
        front = slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next, back = slow.next, None, None
        while mid:
            nxt = mid.next
            mid.next, back, mid = back, mid, nxt
        while back:
            front_nxt, back_nxt = front.next, back.next
            front.next, back.next = back, front_nxt
            front, back = front_nxt, back_nxt
