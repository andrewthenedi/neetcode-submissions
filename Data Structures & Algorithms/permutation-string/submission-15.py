class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # T: O(M + N) | S: O(1)
        # M = Size of s1 | N = Size of s2
        if len(s1) > len(s2):
            return False
        ord_s1 = [0] * 26
        for c in s1:
            ord_s1[ord(c) - ord('a')] += 1
        ord_s2 = [0] * 26
        for i in range(len(s1)):
            c = s2[i]
            ord_s2[ord(c) - ord('a')] += 1
        if ord_s1 == ord_s2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            c_l = s2[l]
            ord_s2[ord(c_l) - ord('a')] -= 1
            l += 1
            c_r = s2[r]
            ord_s2[ord(c_r) - ord('a')] += 1
            if ord_s1 == ord_s2:
                return True
        return False
