class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const preVal = new Map();
        for(let j = 0; j<nums.length; j++) {
            const val = target - nums[j]
            if(preVal.has(val))
                return [preVal.get(val), j]
            preVal.set(nums[j], j)
        }
    }
}
