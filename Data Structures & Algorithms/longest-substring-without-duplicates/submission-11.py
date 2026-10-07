class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T: O(N) | S: O(1)
        # N = Size of s
        result = l = 0
        visited = set()
        for r in range(len(s)):
            while l < r and s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            result = max(result, r - l + 1)
        return result
