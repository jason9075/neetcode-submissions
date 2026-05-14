class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        basket = []

        def traverse(idx):
            
            if idx == len(nums):
                return
            
            # append
            basket.append(nums[idx])
            result.append(basket.copy())
            traverse(idx+1)

            # not append
            basket.pop()
            traverse(idx+1)

        traverse(0)

        return result

        