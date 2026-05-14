class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "EMPTY"
        return "||".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY":
            return []

        return s.split("||")