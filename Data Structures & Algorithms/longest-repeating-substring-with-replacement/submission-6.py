class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # T: O(N) | S: O(M)
        # N = Length of s
        # M = Unique characters of s
        max_length = l = max_count = 0
        counter_s = {}
        for r in range(len(s)):
            counter_s[s[r]] = counter_s.get(s[r], 0) + 1
            max_count = max(max_count, counter_s[s[r]])
            if (r - l + 1) - max_count > k:
                counter_s[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
