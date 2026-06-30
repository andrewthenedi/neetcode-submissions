# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # T: O(N) | S: O(1)
        # N = Number of nodes
        slow = fast = head
        prev = None
        while fast.next and fast.next.next:
            prev, slow = slow, slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        prev = None
        while mid:
            nxt = mid.next
            mid.next, prev, mid = prev, mid, nxt
        front, back = head, prev
        while back:
            nxt_front, nxt_back = front.next, back.next
            front.next, back.next = back, nxt_front
            front, back = nxt_front, nxt_back
