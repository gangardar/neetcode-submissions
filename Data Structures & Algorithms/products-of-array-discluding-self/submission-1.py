class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result= [1] *len(nums)
        for key,val in enumerate(nums):
            for i,num in enumerate(nums):
                if key == i:
                    continue
                result[key] *= num

        return result    