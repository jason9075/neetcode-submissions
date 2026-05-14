class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sRecord = {}
        tRecord = {}

        for char in s:
            if sRecord.get(char) is None:
                sRecord[char] = 1
            else:
                sRecord[char] += 1

        for char in t:
            if tRecord.get(char) is None:
                tRecord[char] = 1
            else:
                tRecord[char] += 1

        for k, _ in sRecord.items():
            if tRecord.get(k) is None or sRecord[k] != tRecord[k]:
                return False
        
        return True