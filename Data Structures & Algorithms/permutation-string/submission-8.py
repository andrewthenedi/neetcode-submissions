class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # T: O(N + M) | S: O(1)
        # N = Length of s1
        # M = Length of s2
        n_s1, n_s2 = len(s1), len(s2)
        if n_s1 > n_s2:
            return False
        ord_s1 = [0] * 26
        ord_s2 = [0] * 26
        for i in range(n_s1):
            ord_s1[ord(s1[i]) - ord('a')] += 1
            ord_s2[ord(s2[i]) - ord('a')] += 1
        if ord_s1 == ord_s2:
            return True
        l = 0
        for r in range(n_s1, n_s2):
            ord_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            ord_s2[ord(s2[r]) - ord('a')] += 1
            if ord_s1 == ord_s2:
                return True
        return False
