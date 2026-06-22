class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for idx,num in enumerate(numbers):
            for n in range(len(numbers) -1, idx, -1):
                if num + numbers[n] == target:
                    result.append(idx +1)
                    result.append(n +1)
        return result