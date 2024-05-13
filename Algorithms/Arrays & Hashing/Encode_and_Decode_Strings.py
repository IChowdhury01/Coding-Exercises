# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for i in strs:
            s += i+'-abc+'
        return s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = s.split('-abc+')
        ans.pop()
        return ans
