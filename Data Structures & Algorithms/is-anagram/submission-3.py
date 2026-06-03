class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T: O(N + M) | S: O(1)
        # N = Number of characters in s
        # M = Number of characters in t
        counter_s = Counter(s)
        for c in t:
            if c not in counter_s:
                return False
            counter_s[c] -= 1
            if not counter_s[c]:
                del counter_s[c]
        return not counter_s
