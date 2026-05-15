class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        while right - left > 1:
            
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            # left part
            if target <= nums[mid]:
                right = mid
            # right part
            else:
                left = mid

            
        return -1

        