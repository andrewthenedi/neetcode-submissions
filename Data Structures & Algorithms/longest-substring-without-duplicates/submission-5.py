class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T: O(N) | S: O(1)
        # N = Length of s
        max_length = length = l = 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                length -= 1
                l += 1
            visited.add(s[r])
            length += 1
            max_length = max(max_length, length)
        return max_length
