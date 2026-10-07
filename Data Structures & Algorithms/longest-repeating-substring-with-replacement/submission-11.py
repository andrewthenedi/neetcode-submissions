class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # T: O(N) | S: O(1)
        # N = Size of s
        counter_s = {}
        result = max_freq = l = 0
        for r, c in enumerate(s):
            counter_s[c] = counter_s.get(c, 0) + 1
            max_freq = max(max_freq, counter_s[c])
            if (r - l + 1) - max_freq > k:
                counter_s[s[l]] -= 1
                if not counter_s[s[l]]:
                    del counter_s[s[l]]
                l += 1
            result = max(result, r - l + 1)
        return result
