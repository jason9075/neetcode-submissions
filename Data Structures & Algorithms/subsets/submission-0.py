class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        basket = []
        self.traverse(0, nums, basket,res)

        return res

    def traverse(self, idx, nums,basket,result):
        
        if idx == len(nums):
            return
        
        # append
        basket.append(nums[idx])
        result.append(basket.copy())
        self.traverse(idx+1, nums, basket, result)


        # not append
        basket.pop()
        self.traverse(idx+1, nums, basket, result)

        