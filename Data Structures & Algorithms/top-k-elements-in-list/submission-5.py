class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        arr = [[] for _ in range(len(nums)+1)]
        for key, val in count.items():
            arr[val].append(key)
        print(arr)
             
        for i in arr[::-1]:
            if len(i) != 0 or len(result) < k:
                for j in i:
                    if len(result) <k:
                        result.append(j)
            elif len(result) == 2:
                break
        return result
