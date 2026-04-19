class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "-1"
        return "DeLiM".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []
        return s.split("DeLiM")