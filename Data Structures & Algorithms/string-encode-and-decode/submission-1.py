class Solution:

    def encode(self, strs: List[str]) -> str:
        # T: O(N) | S: O(1)
        encode_strs = ""
        for s in strs:
            encode_strs += f"{len(s)}#{s}"
        return encode_strs

    def decode(self, s: str) -> List[str]:
        # T: O(N) | S: O(1)
        decode_s = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_c = int(s[i : j])
            j += 1
            c = s[j : j + len_c]
            decode_s.append(c)
            i = j + len_c
        return decode_s
