class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T: O(M + N) | S: O(1)
        # M = Size of s | N = Size of t
        counter_s = Counter(s)
        for c in t:
            if c not in counter_s:
                return False
            counter_s[c] -= 1
            if not counter_s[c]:
                del counter_s[c]
        return not counter_s
