class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = {}

        for n in nums:
            if record.get(n) is not None:
                return True
            record[n] = 1;
        
        return False
        