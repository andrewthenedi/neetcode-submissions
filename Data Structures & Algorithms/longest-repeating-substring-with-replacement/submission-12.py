class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # T: O(N) | S: O(1)
        # N = Size of s
        result = max_freq = l = 0
        counter_s = {}
        for r, c_r in enumerate(s):
            counter_s[c_r] = counter_s.get(c_r, 0) + 1
            max_freq = max(max_freq, counter_s[c_r])
            if (r - l + 1) - max_freq > k:
                c_l = s[l]
                counter_s[c_l] -= 1
                if not counter_s[c_l]:
                    del counter_s[c_l]
                l += 1
            result = max(result, r - l + 1)
        return result
