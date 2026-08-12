class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # T: O(N) | S: O(1)
        longest = max_repeat = l = 0
        counter_s = {}
        for r in range(len(s)):
            counter_s[s[r]] = counter_s.get(s[r], 0) + 1
            max_repeat = max(max_repeat, counter_s[s[r]])
            if (r - l + 1) - max_repeat > k:
                counter_s[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
