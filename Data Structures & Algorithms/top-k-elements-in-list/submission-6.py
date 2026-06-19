class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            count[num] = count.get(num,0) +1
        
        arr = [[] for _ in range(len(nums)+1)]
        for key, val in count.items():
            arr[val].append(key)
        print(arr)
             
        for i in range(len(arr)-1, 0, -1):
                for num in arr[i]:
                        result.append(num)
                        if len(result) == k:
                            return result
        return result
