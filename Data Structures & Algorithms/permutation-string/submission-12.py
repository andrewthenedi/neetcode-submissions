class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # T: O(N) | S: O(1)
        # N = Max length of s1 and s2
        m, n = len(s1), len(s2)
        if m > n:
            return False
        ord_s1, ord_s2 = [0] * 26, [0] * 26
        for i in range(m):
            c = s1[i]
            ord_s1[ord(c) - ord('a')] += 1
            c = s2[i]
            ord_s2[ord(c) - ord('a')] += 1
        if ord_s1 == ord_s2:
            return True
        for r in range(m, n):
            c = s2[r - m]
            ord_s2[ord(c) - ord('a')] -= 1
            c = s2[r]
            ord_s2[ord(c) - ord('a')] += 1
            if ord_s1 == ord_s2:
                return True
        return False
