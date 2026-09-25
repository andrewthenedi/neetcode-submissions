class Solution:

    def encode(self, strs: List[str]) -> str:
        # T: O(N) | S: O(1)
        # N = Size of strs
        encode = ""
        for s in strs:
            encode += f"{len(s)}#{s}"
        return encode

    def decode(self, s: str) -> List[str]:
        # T: O(M) | S: O(1)
        # M = Size of total characters in strs
        decode = []
        l = r = 0
        while l < len(s):
            while r < len(s) and s[r] != '#':
                r += 1
            length = int(s[l : r])
            r += 1
            decode.append(s[r : r + length])
            l = r = r + length
        return decode
